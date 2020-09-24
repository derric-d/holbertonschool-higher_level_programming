const $ = window.$;
window.fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((res) => res.json())
  .then((data) => {
    $('div#character').text(data.name);
  });
