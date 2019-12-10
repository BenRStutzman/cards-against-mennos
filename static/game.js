var card_num = 0;
var selected_id = [];
var current_cards = [];
var played_card = -1
var border_color = "black";

"use strict";

function setBorders(){
    $(".white").css({'border':'3px solid ' + border_color});
}

$(function(){
    $(".white").mouseenter(function(){
        if(has_selected_card()){
          being_hovered($(this), 1);
        }
    });
    $(".white").mouseleave(function(){
        if(has_selected_card()){
          being_hovered($(this), 0);
        }
    });
    $(".white").click(function(){
      if(has_selected_card()){
          selected_id.push($(this).attr('id'));
          var card = $(this).attr('src');
          card_num = $(this).attr('id');
          var style = $(this).attr('Style').replace(/ /g,'');
          $("#selected_card").attr({src: card,
                                    alt : card_num,
                                    Style : style + "border:3px solid " + border_color,
                                    hidden: false});
          $(this).attr("hidden", "true");
          var selected = $("#selected_card");
          selected.css('border', '3px solid ' + border_color);
          $(selected).animate({
              left: "400",
              bottom: "+=200"
          },500,function(){});
        }
    });
});

function being_hovered(pic, x){
    if(x){
        pic.css({'border':'3px solid ' + border_color, 'z-index': '1','width':'270', 'height':'400'});
    } else {
        pic.css({'border':'3px solid ' + border_color, 'z-index': '-1','width':'200', 'height':'300'});
    }
}

function has_selected_card(){
    return $("#selected_card").attr("hidden");
}

$(function(){
    $("#selected_card").click(function(){
        console.log(1);
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
        // this implemetation doesn't work with the current project setup... it doesn't deal with reloads correctly.
        // if($("#play").text()=="PLAY"){
        //     played_card = 1;
        //     setTimeout(function(){$("#play").text("Play this card")},50);
        //     console.log(2);
        // } else {
            played_card = $("#selected_card").attr('src').match(/card(\d)/)[1];
            console.log(played_card)
            console.log("played card: " + played_card);
            $("#selected_card").attr("hidden", true);
        // }
    })
})


// $(function play_again(){
//   //begin new round
//     exchange();
//     console.log("They want to play again.");
// })
