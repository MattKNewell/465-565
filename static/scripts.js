$(document).ready(function () {
  num =3;
  $('#myList li:lt(3)').css('display', 'inline-block');
  $('#loadMore').click(function () {
    num++;
    $('#myList li:lt(' + num + ')').css('display', 'inline-block');
  });
});

