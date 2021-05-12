const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
let Name = '';

$.get(url, function (data, textStatus) {
  Name = data.name;
  $('div#character').text(Name);
});
