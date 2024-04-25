chrome.webNavigation.onHistoryStateUpdated.addListener(async function (details){
    if(details.url.includes("https://www.youtube.com/watch")){
        console.log("history state updated on youtube video");
    
    }
    if(details.url.includes("https://www.youtube.com/watch")){
        await sendMessageToActiveTab({message: "initRecordButton"});
    }


});

async function sendMessageToActiveTab(message) {
    const [tab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
    const response = await chrome.tabs.sendMessage(tab.id, message);
  }