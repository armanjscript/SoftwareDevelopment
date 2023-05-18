window.onload = function () {
    const url = document.getElementById('yturl');
    const quality = document.getElementById('quality');
    const filename = document.getElementById('filename');
    const format = document.getElementById('format');
    const downloadBtn = document.getElementById('download');

    downloadBtn.onclick = function () {
        console.log("button clicked");
        downloadBtn.innerText = "Download file ...";
        var message = {
            'url': url.value,
            'quality': quality.value,
            'filename': filename.value,
            'format': format.value
        };
        chrome.runtime.sendMessage(message);
    }
}