function initDeepFakeButtonInPlayer(){
    const buttonAvailableInterval = setInterval(function (){
        var animControlsButton = document.getElementsByClassName("ytp-right-controls");
        if (animControlsButton !== undefined){
            if(document.getElementById("deepfake") === null || document.getElementById("deepfake") === undefined){
                var button = document.createElement('button');
                button.id="deepfake";
                button.className = 'ytp-button it-player-button';
                button.dataset.title = "Deepfake detection";
                animControlsButton[0].insertBefore(button, animControlsButton[0].childNodes[0]);
                let playerImage = new Image();
                playerImage.src = chrome.runtime.getURL("/images/deepfake-icon.png")
                playerImage.onload = () => {
                    var imgTag = document.createElement('img');
                    imgTag.src=playerImage.src;
                    button.appendChild(imgTag);
                }

                // Attach event listener to the button
                button.addEventListener('click', function() {
                    console.log('Deepfake button clicked');
                    captureFrameFromVideo();
                });
            }
            clearInterval(buttonAvailableInterval);
        }
    }, 100);

}

function captureFrameFromVideo() {
    var videoElement = document.querySelector("video");
    if (videoElement) {
        var canvas = document.createElement('canvas');
        canvas.width = videoElement.videoWidth;
        canvas.height = videoElement.videoHeight;
        canvas.getContext('2d').drawImage(videoElement, 0, 0, canvas.width, canvas.height);
        var frameDataUrl = canvas.toDataURL(); // Data URL of the captured frame
        
        // Make a call to your FastAPI backend at the endpoint /model_info
        fetch('http://localhost:8000/save_frame', {
            method: 'POST', // or 'POST' if your backend expects POST requests
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({
                'image_data': frameDataUrl
            })
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


    } else {
        console.error('Video element not found');
    }
}

chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
       if(request.message === "initRecordButton"){
           initDeepFakeButtonInPlayer()
       }
    }
);