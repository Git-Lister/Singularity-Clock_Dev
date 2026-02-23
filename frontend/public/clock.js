// Clock rendering logic
const canvas = document.getElementById('clock');
const ctx = canvas.getContext('2d');

function drawClock(dataHand, sentimentHand, vibeHand) {
    // TODO: draw clock face and hands
    console.log('Drawing clock...');
}

// On load, fetch data and draw
fetch('/api/current')
    .then(r => r.json())
    .then(data => {
        // For now, just draw with placeholder values
        drawClock(42, 30, 50);
    });
