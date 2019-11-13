// Auto-size portrait
var logoWidth = document.getElementsByTagName('h1')[0].offsetWidth;
var portrait = document.getElementsByClassName('portrait')[0];
var portraitWidth = logoWidth * 0.61804 // inverse golden ratio
portrait.setAttribute('style', 'width:' + portraitWidth + 'px');

// expand about text
$("#about").click(function() {
  if ($("#line2").css('margin-bottom') == 0) {
    $("#line2").css('margin-bottom', "8%");
  } else {
    $("#line2").css('margin-bottom', 0);
  }

  $(".about").slideToggle("slow");
})
