$(function(){
  $("img").mouseenter(function(){
      $(this).css('border', '3px solid black');
  });
  $("img").mouseleave(function(){
    $(this).css('border-width', '0');
  });
  $("img").click(function(){
    $(this).animate({
      marginLeft: "+=400px",
      marginTop: "-300px"
    },1000,function(){
    });
  });
});

$(function(){
  $("#draw").click(function(){
    card_num++;
    $("body").append(`<img src = "test_pic1.jpg" alt = "a hand of cards" Style = "height:300px; width: 200px; top:500px; left:${card_num*400}px")>`)
  })
})
