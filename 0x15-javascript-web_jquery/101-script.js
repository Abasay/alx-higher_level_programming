$('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>')
})

$('DIV#remove_item').on('click', function () {
    const lists = $('UL.my_list');

    $.lists[-1].remove()
})

$('DIV#clear_list').on('click', function () {
    $('li').remove()
})
