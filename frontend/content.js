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

        chrome.runtime.sendMessage(
            {action: 'fetchData', frameDataUrl: frameDataUrl}, 
            function(response) {console.log('Response from background script:', response);}
        );

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