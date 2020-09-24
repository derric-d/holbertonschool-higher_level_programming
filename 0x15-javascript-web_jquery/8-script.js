const $ = window.$;
window.fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((res) => res.json())
  .then((data) => {
    data = data.results;
    for (const ele of data) {
      $('ul#list_movies').append(`<li>${ele.title}</li>`);
    }
  });
