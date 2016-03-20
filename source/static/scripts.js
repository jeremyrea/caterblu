$(document).ready(function(){
  displayProperDiv();
});

$(window).on("load", function() {
  dropResult();
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
  $(':input:not(:button)').each(function(index, element) {
    if (element.value != '') {
      $(".jumbotron").addClass("focus");
    }
  });
}
