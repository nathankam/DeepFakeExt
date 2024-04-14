document.addEventListener('DOMContentLoaded', function() {

    // callApi Button is the link to the button we createed
    document.getElementById('showModelInfo').addEventListener('click', function() {

        // Make a call to your FastAPI backend at the endpoint /model_info
        fetch('http://localhost:8002/model_info', {
            method: 'GET', // or 'POST' if your backend expects POST requests
            headers: {
                'Content-Type': 'application/json'
                
            }
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Do something with the data you received
            console.log(data);
        })
        .catch(error => {
            console.error('There was a problem with your fetch operation:', error);
        });
    });
});