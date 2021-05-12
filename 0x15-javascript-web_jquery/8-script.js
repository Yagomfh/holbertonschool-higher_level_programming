const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.get(url, function (data, textStatus) {
  const movies = data.results;
  for (const movie in movies) {
    const html = '<li>' + movies[movie].title + '</li>';
    $('ul#list_movies').append(html);
  }
});
