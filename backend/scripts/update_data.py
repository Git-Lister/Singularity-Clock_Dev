#!/usr/bin/env python
"""
Updated script to fetch and parse Epoch AI datasets using correct URLs.
"""

import os
import sys
import json
import zipfile
import requests
import pandas as pd
from pathlib import Path
from datetime import datetime
import logging
from typing import Dict, Any, Optional

# Add parent directory to path so we can import app modules
sys.path.insert(0, str(Path(__file__).parent.parent))
from app.services.data_store import DATA_DIR

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# CORRECTED Epoch AI data URLs (based on search results)
# These follow the pattern from epoch.ai/data page [citation:3]
EPOCH_MODELS_URL = "https://epoch.ai/data/ai-models/ai-models.zip"
EPOCH_BENCHMARKS_URL = "https://epoch.ai/data/benchmarks/benchmarks.zip"

# Alternative URLs if the above don't work
ALTERNATIVE_URLS = {
    "models": [
        "https://epoch.ai/data/ai-models-download",
        "https://epoch.ai/data/download/ai-models"
    ],
    "benchmarks": [
        "https://epoch.ai/data/benchmarks-download",
        "https://epoch.ai/data/download/benchmarks"
    ]
}

# Local paths
RAW_DATA_DIR = DATA_DIR / "raw"
RAW_DATA_DIR.mkdir(exist_ok=True)

def download_file(url: str, local_path: Path) -> bool:
    """Download a file from URL to local path with better error handling."""
    try:
        logger.info(f"Attempting to download from: {url}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, stream=True, timeout=30, headers=headers)
        response.raise_for_status()
        
        # Check if we got HTML instead of ZIP (common redirect issue)
        content_type = response.headers.get('Content-Type', '')
        if 'text/html' in content_type and not url.endswith('.zip'):
            logger.warning(f"Got HTML response, might be a redirect page")
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Verify it's a valid zip file
        if zipfile.is_zipfile(local_path):
            logger.info(f"✅ Successfully downloaded valid ZIP: {local_path}")
            return True
        else:
            logger.error(f"Downloaded file is not a valid ZIP: {local_path}")
            return False
            
    except Exception as e:
        logger.error(f"Download failed: {e}")
        return False

def try_alternative_urls(dataset_type: str, local_path: Path) -> bool:
    """Try alternative URLs if the primary one fails."""
    urls = ALTERNATIVE_URLS.get(dataset_type, [])
    for url in urls:
        logger.info(f"Trying alternative URL for {dataset_type}: {url}")
        if download_file(url, local_path):
            return True
    return False

def extract_zip(zip_path: Path, extract_to: Path) -> bool:
    """Extract ZIP file to destination."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logger.info(f"✅ Extracted {zip_path} to {extract_to}")
        return True
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        return False

def find_csv_file(directory: Path, name_pattern: str) -> Optional[Path]:
    """Find first CSV file in directory matching pattern."""
    for file in directory.glob("*.csv"):
        if name_pattern.lower() in file.name.lower():
            return file
    # If no match, return first CSV
    csv_files = list(directory.glob("*.csv"))
    return csv_files[0] if csv_files else None

def parse_models_dataset(csv_path: Path) -> Dict[str, Any]:
    """
    Parse AI Models CSV and extract compute-relevant fields.
    Based on Epoch AI documentation [citation:8]
    """
    logger.info(f"Parsing models dataset: {csv_path}")
    
    df = pd.read_csv(csv_path)
    
    # Log available columns for debugging
    logger.info(f"Available columns: {df.columns.tolist()}")
    
    # Standardise column names based on Epoch AI schema [citation:8]
    column_mapping = {
        'Training compute (FLOP)': 'compute_flop',
        'Training Compute (FLOP)': 'compute_flop',
        'Compute (FLOP)': 'compute_flop',
        'Parameters': 'parameters',
        'Domain': 'domain',
        'Organization': 'organization',
        'Publication date': 'publication_date',
        'Publication Date': 'publication_date',
        'Model': 'model_name',
        'Model name': 'model_name',
        'Notability criteria': 'notability',
        'Confidence': 'confidence'
    }
    
    # Rename columns that exist
    df_renamed = df.rename(columns={col: new for col, new in column_mapping.items() if col in df.columns})
    
    # Filter to language models (our primary interest)
    if 'domain' in df_renamed.columns:
        language_models = df_renamed[df_renamed['domain'].str.contains('Language|LLM', na=False, case=False)]
    else:
        language_models = df_renamed
        logger.warning("Domain column not found, using all models")
    
    # Extract key statistics
    result = {
        'last_updated': datetime.now().isoformat(),
        'total_models': len(df_renamed),
        'language_models': len(language_models),
        'models_with_compute': 0,
        'compute_stats': {},
        'recent_models': []
    }
    
    # Compute statistics if column exists
    if 'compute_flop' in df_renamed.columns:
        # Convert to numeric, coerce errors to NaN
        compute = pd.to_numeric(df_renamed['compute_flop'], errors='coerce')
        valid_compute = compute.dropna()
        result['models_with_compute'] = int(len(valid_compute))
        
        if not valid_compute.empty:
            result['compute_stats'] = {
                'min_flop': float(valid_compute.min()),
                'max_flop': float(valid_compute.max()),
                'mean_flop': float(valid_compute.mean()),
                'median_flop': float(valid_compute.median()),
                'total_models_with_compute': int(len(valid_compute))
            }
    
    # Sample recent notable models (for reference)
    if 'publication_date' in df_renamed.columns and 'model_name' in df_renamed.columns:
        df_renamed['publication_date'] = pd.to_datetime(df_renamed['publication_date'], errors='coerce')
        recent = df_renamed.nlargest(10, 'publication_date')[
            ['model_name', 'publication_date', 'compute_flop'] if 'compute_flop' in df_renamed.columns else ['model_name', 'publication_date']
        ]
        result['recent_models'] = recent.to_dict('records')
    
    return result

def parse_benchmarks_dataset(csv_path: Path) -> Dict[str, Any]:
    """
    Parse AI Benchmarking CSV for capabilities index.
    Based on Epoch AI Benchmarking Hub [citation:1]
    """
    logger.info(f"Parsing benchmarks dataset: {csv_path}")
    
    df = pd.read_csv(csv_path)
    
    # Log available columns
    logger.info(f"Benchmark columns: {df.columns.tolist()}")
    
    result = {
        'last_updated': datetime.now().isoformat(),
        'total_entries': len(df),
        'benchmarks': {},
        'top_scores': {}
    }
    
    # Identify benchmark columns (common ones from documentation [citation:1])
    benchmark_patterns = ['mmlu', 'glue', 'superglue', 'hellaswag', 'truthfulqa', 
                          'gpqa', 'math', 'frontiermath']
    
    for pattern in benchmark_patterns:
        matching_cols = [col for col in df.columns if pattern.lower() in col.lower()]
        if matching_cols:
            for col in matching_cols:
                # Try to get max score for this benchmark
                scores = pd.to_numeric(df[col], errors='coerce')
                valid_scores = scores.dropna()
                if not valid_scores.empty:
                    result['benchmarks'][col] = {
                        'max': float(valid_scores.max()),
                        'mean': float(valid_scores.mean()),
                        'count': int(len(valid_scores)),
                        'latest_date': None
                    }
                    
                    # Try to get date information if available
                    if 'date' in df.columns:
                        date_col = df[df[col].notna()]['date']
                        if not date_col.empty:
                            result['benchmarks'][col]['latest_date'] = date_col.iloc[-1]
    
    return result

def fetch_epoch_data():
    """Main function to download and parse Epoch datasets."""
    logger.info("Starting Epoch AI data fetch")
    
    datasets_fetched = 0
    
    # Try models dataset
    models_zip = RAW_DATA_DIR / "ai-models.zip"
    if download_file(EPOCH_MODELS_URL, models_zip) or try_alternative_urls("models", models_zip):
        extract_to = RAW_DATA_DIR / "models"
        extract_to.mkdir(exist_ok=True)
        if extract_zip(models_zip, extract_to):
            csv_file = find_csv_file(extract_to, "models")
            if csv_file:
                models_data = parse_models_dataset(csv_file)
                
                # Save parsed data
                with open(DATA_DIR / "epoch_models.json", 'w') as f:
                    json.dump(models_data, f, indent=2, default=str)
                logger.info("✅ Saved models data to epoch_models.json")
                datasets_fetched += 1
    else:
        logger.error("❌ Failed to download models dataset after trying all URLs")
    
    # Try benchmarks dataset
    benchmarks_zip = RAW_DATA_DIR / "benchmarks.zip"
    if download_file(EPOCH_BENCHMARKS_URL, benchmarks_zip) or try_alternative_urls("benchmarks", benchmarks_zip):
        extract_to = RAW_DATA_DIR / "benchmarks"
        extract_to.mkdir(exist_ok=True)
        if extract_zip(benchmarks_zip, extract_to):
            csv_file = find_csv_file(extract_to, "benchmark")
            if csv_file:
                benchmarks_data = parse_benchmarks_dataset(csv_file)
                
                # Save parsed data
                with open(DATA_DIR / "epoch_benchmarks.json", 'w') as f:
                    json.dump(benchmarks_data, f, indent=2, default=str)
                logger.info("✅ Saved benchmarks data to epoch_benchmarks.json")
                datasets_fetched += 1
    else:
        logger.error("❌ Failed to download benchmarks dataset after trying all URLs")
    
    # Update current.json with placeholder until we implement composite
    current = {
        "data_hand": 42.0,  # Placeholder
        "vibe_hand": 50.0,   # Placeholder
        "timestamp": datetime.now().isoformat(),
        "metadata": {
            "datasets_fetched": datasets_fetched,
            "fetch_status": "partial" if datasets_fetched < 2 else "complete",
            "last_attempt": datetime.now().isoformat()
        }
    }
    
    from app.services.data_store import write_current
    write_current(current)
    logger.info(f"Updated current.json with placeholder values (fetched {datasets_fetched}/2 datasets)")

def main():
    """Entry point for the script."""
    try:
        fetch_epoch_data()
        logger.info("Data fetch completed")
    except Exception as e:
        logger.error(f"Data fetch failed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()