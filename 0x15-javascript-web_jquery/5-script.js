const $ = window.$;
$('div#add_item').click(() => {
  $('ul.mylist').append('<li>Item</li>');
});
