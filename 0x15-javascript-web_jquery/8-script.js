$(function () {
  $.get({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (result) {
      $.each(result.results, function (index, title) {
        $('#list_movies').append('<li>' + title.title + '</li>')
      })
    },
  })
})
