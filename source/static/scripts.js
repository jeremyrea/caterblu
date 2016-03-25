$(document).ready(function(){
  // Trigger inputfit()
  $("#id_title").trigger(jQuery.Event("keydown"));
  displayProperDiv();

  $(window).resize(function() {
    resizeBigContainer();
  }).resize();
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
