var card_num = 0;
var selected_id = 0;
var current_cards = [];
var played_card = -1
var border_color = "black";

"use strict";

// This sets up some css styling of the cards
function setBorders(){
    $(".white").css({'border':'3px solid ' + border_color});
}

$(function(){
    // This sets up most of the interactions with the cards

    $(".white").mouseenter(function(){
        // This calls a convenince method that makes the card bigger and brings it forward
        if(has_selected_card()){
            being_hovered($(this), 1);
        }
    });
    $(".white").mouseleave(function(){
        // This calls a convenince method that reverts those changes
        if(has_selected_card()){
            being_hovered($(this), 0);
        }
    });
    $(".white").click(function(){
        // This is what allows you to select a card
        if(has_selected_card()){
            // This finds all of the variables that need to be submitted
            selected_id = ($(this).attr('id'));
            var card = $(this).attr('src');
            card_num = $(this).attr('alt');
            var style = $(this).attr('Style').replace(/ /g,'');

            // This applies these variables to the card that card that actually moves
            $("#selected_card").attr({src: card,
                                      alt : card_num,
                                      Style : style + "border:3px solid " + border_color,
                                      hidden: false});

            // This sets up the visuals for what is happening
            $(this).attr("hidden", "true");
            var selected = $("#selected_card");
            selected.css('border', '3px solid ' + border_color);
            $(selected).animate({
                left: "400",
                bottom: "+=200"
                // width: "50px;"
            },500,function(){
            });
        }
    });
});


// convience method for hovering over the card.
function being_hovered(pic, x){
    if(x){
        pic.css({'border':'3px solid ' + border_color, 'z-index': '1','width':'270', 'height':'400'});
    } else {
        pic.css({'border':'3px solid ' + border_color, 'z-index': '-1','width':'200', 'height':'300'});
    }
}

// convience method for being able to tell if a card has already been selected or not.
function has_selected_card(){
    return $("#selected_card").attr("hidden");
}


// method for deslecting a card
$(function(){
    $("#selected_card").click(function(){
        //figures out where the prev_card was, then animate the selected card to that position and hide the selected card while revealing the actual card.
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



// Handling of the play button.
$(function(){
    $("#play").click(function(){
        played_card = $("#selected_card").attr('alt').match(/card(\d)/)[1];
        console.log("played card: " + played_card);
        $("#selected_card").attr("hidden", true);
    })
})


// $(function play_again(){
//     //begin new round
//         exchange();
//         console.log("They want to play again.");
// })
