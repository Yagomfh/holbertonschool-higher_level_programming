const url = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.get(url, function (data, textStatus) {
  console.log(data);
  $('div#hello').text(data.hello);
});
