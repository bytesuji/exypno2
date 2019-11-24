// Auto-size portrait
$("#about").click(function() {
  if ($("#line2").css('margin-bottom') == 0) {
    $("#line2").css('margin-bottom', "8%");
  } else {
    $("#line2").css('margin-bottom', 0);
  }

  $("#about-text").slideToggle("slow");
  window.scrollBy(0, 290);
});

$("#portfolio").click(function() {
  $(".portfolio").slideToggle("slow");
  window.scrollBy(0, 400);
});

// function randomInt(min, max) {
//   return Math.floor(Math.random() * Math.floor(max) + min);
// }

// $("html, body").click(function() {
//   var hueShift = randomInt(40, 180);
//
//   var newBG = chroma($("body").css('background-color')).set('hsl.h', hueShift);
//   var newBorder = chroma("#8aafc4").set('hsl.h', hueShift);
//   var textShadowColor =  "-3px 0 " + newBorder + ", 0 3px " + newBorder +
//    ", 3px 0 " + newBorder + ", 0 -3px " + newBorder;
//
//   $("h1").css('text-shadow', textShadowColor);
//   $("body").css('background-color', newBG);
//   $('.portrait').css('border', '3px solid '+newBorder);
//   $('.fakelink, a').hover(function() {
//     $(this).css('color', newBorder);
//   })
// });
