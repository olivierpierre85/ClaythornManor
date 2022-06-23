screen current_time:
     zorder 1
     modal False

     text "[current_time], [current_day]"

screen in_game_menu_btn:
     imagebutton:
          xalign 1.0
          yalign 0.0
          xoffset -30
          yoffset 30
          idle "images/ui/menu_btn.png"
          action ShowMenu("in_game_menu")



screen in_game_menu:
     zorder 2
     modal False

     text "MENU"

     imagebutton:
          xalign 1.0
          yalign 0.0
          xoffset -30
          yoffset 30
          idle "images/ui/back_btn.png"
          action Return()