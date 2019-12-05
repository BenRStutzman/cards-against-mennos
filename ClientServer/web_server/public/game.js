var card_num = 0;
var selected_id = [];

"use strict";

$(function(){
  $("img").mouseenter(function(){
    if(has_selected_card()){
      being_hovered($(this), 1);
    }
  });
  $("img").mouseleave(function(){
    if(has_selected_card()){
      being_hovered($(this), 0);
    }
  });
  $("img").click(function(){
    if(has_selected_card()){
      selected_id.push($(this).attr('id'));
      var card = $(this).attr('src');
      card_num = $(this).attr('alt');
      var style = $(this).attr('Style').replace(/ /g,'');
      $("#selected_card").attr({src: card,
                                alt : card_num,
                                Style : style + "border:3px solid black",
                                hidden: false});
      $(this).attr("hidden", "true");
      var selected = $("#selected_card");
      selected.css('border', '3px solid black');
      $(selected).animate({
        left: "400",
        bottom: "+=300"
        // width: "50px;"
      },500,function(){
      });
    }
  });
});

function being_hovered(pic, x){
  if(x){
    pic.css({'border':'3px solid black', 'z-index': '1','width':'270', 'height':'400'});
  } else {
    pic.css({'border':'0px solid black', 'z-index': '-1','width':'200', 'height':'300'});
  }
}

function has_selected_card(){
  return $("#selected_card").attr("hidden");
}

$(function(){
  $("#selected_card").click(function(){
    var prev_card = $(`#${selected_id}`);
    var left = prev_card.attr("Style").match(/left: (\d+)/)[1]
    $(this).animate({
      left: left,
      bottom: "-=300",
      height: "300",
      width: "200"
    },500,function(){
      prev_card.attr({hidden: false});
      being_hovered(prev_card, 0);
      $(this).attr('hidden','true');
      });
  })
})




$(function(){
  $("#play").click(function(){
    //get the information about this card and push it to the server as an event
    data = {name: 'id', text:`A card with the id of ${selected_id[selected_id.length-1]} was just played.`}
    $.get(`/${selected_id[selected_id.length-1]}`, function(data, status){
      console.log(`${data} and ${status}`);
    })
    //for testing above
    $("#selected_card").attr("hidden", true);
  })
})
$(function(){
  $("#draw").click(function(){
    selected_id.forEach(function(id){
      // Get new card info and put the new pic in essentially
      if(has_selected_card()){if(being_hovered($(`#${id}`).attr("hidden", false)));}
    })
  })
})
