
chrome.runtime.onMessage.addListener((message) => {
    var url = "http://localhost:4000/download?";
    var queryString = Object.keys(message).map(key => key + "=" + message[key]).join('&');
    url += queryString;

    chrome.downloads.download({
        url: url,
        filename: "ArgonzYoutubeDl/" + message.filename + '.' + message.format
    }, function (downloadID) {
        chrome.downloads.show(downloadID);
    })
})