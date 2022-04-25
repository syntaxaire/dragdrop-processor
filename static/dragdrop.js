'use strict';
// Sources drawn from:
// https://html.spec.whatwg.org/multipage/dnd.html#dnd
// https://www.smashingmagazine.com/2018/01/drag-drop-file-uploader-vanilla-js/

const postURL = '/submitfiles'
var dropArea = document.getElementById('droparea');
dropArea.addEventListener('dragenter', dragEnterHandler, false);
dropArea.addEventListener('dragleave', dragLeaveHandler, false);
dropArea.addEventListener('dragover', dragOverHandler, false);
dropArea.addEventListener('drop', dropHandler, false);

function addTargetTint() {
    // add darker shading to the drop area
    dropArea.classList.add("dropinprogress");
}

function removeTargetTint() {
    // remove the darker shading from the drop area
    dropArea.classList.remove('dropinprogress');
}

function dragEnterHandler(event) {
    // Called each time a drag in progress enters an applicable element, including transitioning
    // between elements inside the target div
    addTargetTint();
    // Cancelling the default indicates that we are willing to accept this drop
    event.preventDefault();
}

function dragLeaveHandler(event) {
    removeTargetTint();
}

function dragOverHandler(event) {
    // Called continuously when a drag in progress is over an applicable element
    addTargetTint(); // refresh this when cursor switches elements inside target
    event.preventDefault();
}

function dropHandler(event) {
    // Called when a drop is completed over an applicable element
    removeTargetTint();
    event.preventDefault(); // prevent browser from potentially loading the file
    let files = event.dataTransfer.files; // type: FileList
    handleFiles(files);
}

function handleFiles(files) {
    for (var i = 0; i < files.length; i++) {
        let file = files[i];
        uploadFile(file);
    }
}

function uploadFile(file) {
    let formData = new FormData();
    formData.append('file', file);
    fetch(postURL, {
      method: 'POST',
      body: formData,
    })
}
