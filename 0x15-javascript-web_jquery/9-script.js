const $ = window.$;

window.fetch('https://fourtonfish.com/hellosalut/?lang=fr')
  .then((res) => res.json())
  .then((data) => {
    $('div#hello').text(data.hello);
  });
