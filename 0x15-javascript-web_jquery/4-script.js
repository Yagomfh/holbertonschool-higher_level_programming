$('div#toggle_header').click(function () {
  if ($('header').attr('class') === 'red') {
    $('header').attr('class', 'green');
  } else {
    $('header').attr('class', 'red');
  }
});
