document.addEventListener('DOMContentLoaded', function () {
  const statusElement = document.getElementById('status');
  const resultElement = document.getElementById('result');
  const reasonElement = document.getElementById('reason');

  chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    const currentUrl = tabs[0].url;
    statusElement.textContent = `Analyzing...`;

    fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: currentUrl }),
    })
      .then(response => response.json())
      .then(data => {
        statusElement.style.display = 'none';
        resultElement.textContent = data.prediction;
        reasonElement.textContent = data.reason;
      })
      .catch(error => {
        resultElement.textContent = 'Connection Error';
        reasonElement.textContent = 'Ensure the Flask server is running.';
      });
  });
});