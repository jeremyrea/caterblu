$(window).on("load", function() {
  $(".jumbotron").addClass("focus");
});

function hideSmallContainer() {
  $.ajax({
    url: "/?",
    type: "get",
    data:{title: $("#search_form").value()}
  });
}
