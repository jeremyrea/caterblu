$(document).ready(function(){
  // Trigger inputfit()
  $("#id_title").trigger(jQuery.Event("keydown"));
  displayProperDiv();

  $(window).resize(function() {
    resizeBigContainer();
  }).resize();

  $("#id_country").change(function() {
      $.ajax({
        'url' : '/api/price',
        'type' : 'GET',
        'data' : $('#search-form').serialize(),
        'success' : function(data) {
          var obj = $.parseJSON(data);
          $('#price').text("Price: " + obj._Price__price[1] + "$" + obj._Price__price[0]);
          $('#listing').text("Listing: " + obj._Price__list_price[1] + "$" + obj._Price__list_price[0]);
          $("#buy-button").attr("href", obj._Price__link);
        }
      });
  });
});

$(window).on("load", function() {
  dropResult();
  resizeBigContainer();
});

function displayProperDiv() {
  var status = $('body').data('status');
  if (status == 200) {
    $("#search-error").addClass("hidden");
    $("#data-display").show();
  } else {
    $("#search-error").show();
    $("#data-display").addClass("hidden");
  }
}

function dropResult() {
  $(':input:not(:button, select)').each(function(index, element) {
    if (element.value != '') {
      $(".jumbotron").addClass("focus");
    }
  });
}

function resizeBigContainer() {
  var jh = $('.jumbotron').height();
  var ch = $('.small-container').height();
  var eh = $('#search-error').height();
  var h = jh+ch+eh+220;
  $('.big-container').height(h);
}
