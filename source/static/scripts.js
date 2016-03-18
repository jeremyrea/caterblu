$(window).on("load", function() {
  $(':input:not(:button)').each(function(index, element) {
    if (element.value != '') {
      $(".jumbotron").addClass("focus");
    }
  });
});

function hideSmallContainer() {
  $.ajax({
    url: "/?",
    type: "get",
    data:{title: $("#search_form").value()},
  });
}
