chrome.webNavigation.onHistoryStateUpdated.addListener(async function (details){
    if(details.url.includes("https://www.youtube.com/watch")){
        console.log("history state updated on youtube video");
    
    }
    if(details.url.includes("https://www.youtube.com/watch")){
        await sendMessageToActiveTab({message: "initRecordButton"});
    }


});


chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {

    console.log('Message from content script:', message);

    if (message.action === 'fetchData') {

        const frameDataUrl = message.frameDataUrl;

        fetch('http://localhost:8000/process_frame', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            body: JSON.stringify({
                'image_data': frameDataUrl
            })
        })
        .then(response => {
            console.log('Response', response);
            if (!response.ok) {throw new Error('Network response was not ok');}
            return response.json();

        })
        .then(data => {
            sendResponse({data: data});
               
            chrome.runtime.sendMessage({ action: 'updateResponse', content: data.message});
            chrome.runtime.sendMessage({ action: 'updateImage', content: data.face_image});

            console.log('Response Data', data);
        })
        .catch(error => {
            sendResponse({ error: error.toString() });
        });


        return true;
    }
});

async function sendMessageToActiveTab(message) {
    const [tab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
    const response = await chrome.tabs.sendMessage(tab.id, message);
  }