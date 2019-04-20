$('body').on('click', '.sandwitch .icon', function () {
  $(this).toggleClass('opened');
  $('.menu-full').toggleClass('opened');
  $('body').toggleClass('opened');
});

$('body').on('click', '.menu-full a', function () {
  $('.sandwitch .icon').click()
});

$('body').on('click', '.filter span', function() {
  var filter_name = $(this).data('filter');

  $('.filter span').removeClass('selected');
  $(this).addClass('selected');

  if (filter_name == 'all') {
    $('.result').show();
    return false;
  }


  $('.result').not('.' + filter_name).hide();
  $('.' + filter_name).show();

});

$('[data-to]').on('click', function(e) {
  e.preventDefault();

  var to = $(this).data('to'),
    position = $(to).offset().top;

  $('html, body').stop().animate({scrollTop: position - 50}, 400);
});

$('.show-more').on('click', function () {
  var is_closed = $('.animals-table').hasClass('closed');

  if (is_closed) {
    $('.animals-table').removeClass('closed').addClass('opened');
    $(this).removeClass('closed').addClass('opened');
  } else {
    $('.animals-table').removeClass('opened').addClass('closed');
    $(this).removeClass('opened').addClass('closed');
  }

});

var $input = $('.select-date').pickadate({
  container: 'body',
  closeOnSelect: true,
  max: Date.now(),
  format: 'dd/mm/yyyy',
  clear: false,
  onSet: function(context) {
    if((this.get() != '') && (this.get() != $('.select-date').html())){
      $('.select-date').html(this.get());
      window.location.href = '/passados/' + (this.get()).replace(/\//g, '-')
    }

  }
});
var picker = $input.pickadate('picker')
picker.set('select', $('.select-date').html(), { format: 'dd/mm/yyyy' });
