from sqlalchemy import (
    Column, Integer, String, Float, Date, DateTime, ARRAY, JSON,
    ForeignKey, Numeric, Boolean, func
)
from sqlalchemy.orm import relationship
from ..database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    country = Column(ARRAY(String))
    created_at = Column(DateTime, server_default=func.now())  # Use DateTime for timestamps

    models = relationship("Model", back_populates="organization")


class Model(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True)
    model_name = Column(String, unique=True, nullable=False)
    organization_id = Column(Integer, ForeignKey("organizations.id"))
    publication_date = Column(Date)
    domain = Column(ARRAY(String))
    training_compute_flop = Column(Numeric)
    parameters = Column(Numeric)
    training_dataset_size = Column(Numeric)
    hardware_used = Column(ARRAY(String))
    confidence = Column(String)
    citation_count = Column(Integer)
    notability_criteria = Column(ARRAY(String))
    link = Column(String)
    metadata = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    organization = relationship("Organization", back_populates="models")
    scores = relationship("ModelBenchmarkScore", back_populates="model")


class Benchmark(Base):
    __tablename__ = "benchmarks"

    id = Column(Integer, primary_key=True)
    benchmark_name = Column(String, unique=True, nullable=False)
    description = Column(String)
    benchmark_type = Column(String)
    citation = Column(String)

    scores = relationship("ModelBenchmarkScore", back_populates="benchmark")


class ModelBenchmarkScore(Base):
    __tablename__ = "model_benchmark_scores"

    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey("models.id", ondelete="CASCADE"))
    benchmark_id = Column(Integer, ForeignKey("benchmarks.id", ondelete="CASCADE"))
    score = Column(Float, nullable=False)
    score_date = Column(Date)
    is_state_of_the_art = Column(Boolean, default=False)
    metadata = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())

    model = relationship("Model", back_populates="scores")
    benchmark = relationship("Benchmark", back_populates="scores")


class CompositeHistory(Base):
    __tablename__ = "composite_history"

    id = Column(Integer, primary_key=True)
    snapshot_date = Column(Date, nullable=False)
    compute_component = Column(Float)
    capability_component = Column(Float)
    papers_component = Column(Float)
    composite_value = Column(Float)
    metadata = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())