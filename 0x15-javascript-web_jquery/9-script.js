const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

window.addEventListener('DOMContentLoaded', (event) => {
  $.get(url, function (data, textStatus) {
    $('div#hello').text(data.hello);
  });
});
