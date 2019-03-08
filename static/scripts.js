$(document).ready(function () {
  // Load the first 3 list items from another HTML file
  //$('#myList').load('externalList.html li:lt(3)');
  num =1;
  $('#myList li:lt(1)').show();
  $('#loadMore').click(function () {
    num++;
    $('#myList li:lt(' + num + ')').show();
  });
});