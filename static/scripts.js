$(document).ready(function () {
  // Load the first 3 list items from another HTML file
  //$('#myList').load('externalList.html li:lt(3)');
  num =1;
  $('#myList li:lt(1)').show();
  $('#loadMore').click(function () {
    num++;
    $('#myList li:lt(' + num + ')').show();
  });

  // $.ajax({
  //   xhr: function() {
  //     var xhr = new window.XMLHttpRequest();
  //     //Upload progress
  //     xhr.upload.addEventListener("progress", function(evt) {
  //       if (evt.lengthComputable) {
  //         var percentComplete = evt.loaded / evt.total;
  //         //Do something with upload progress
  //         console.log("Hello from js: " + percentComplete);
  //       }
  //     }, false);
  //     //Download progress
  //     xhr.addEventListener("progress", function(evt) {
  //       if (evt.lengthComputable) {
  //         var percentComplete = evt.loaded / evt.total;
  //         //Do something with download progress
  //         console.log("hi from js: " + percentComplete);
  //         $( "#progressbar" ).progressbar({
  //           value: percentComplete
  //         });
  //       }
  //     }, false);
  //     return xhr;
  //   },
  //   type: 'POST',
  //   url: "/",
  //   data: {},
  //   success: function(data) {
  //     //Do something success-ish
  //   }
  // });
});

