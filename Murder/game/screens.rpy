﻿################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    mouse "hover"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0 yoffset -310 xoffset 220


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos - 250
    xanchor gui.name_xalign
    xsize gui.namebox_width - 30
    ypos gui.name_ypos  + 15
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 1.0
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos - 17


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice
screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action
            


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu and not renpy.get_screen('choice'):
        # TODO OLPI => configure menu to remove save/load, add map and character,...
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            imagemap:
                ground "gui/textbox_ground.png"
                idle "gui/textbox_ground.png"
                hover "gui/textbox_hover.png"
                selected_hover "gui/textbox_selected_hover.png"
                selected_idle "gui/textbox_hover.png"

                hotspot (1307, 282, 52, 52) action Skip() alternate Skip(fast=True, confirm=True)
                hotspot (1392, 282, 52, 52) action Preference("auto-forward", "toggle")
                hotspot (1475, 282, 52, 52) action Rollback()

                hotspot (517, 282, 52, 52) action ShowMenu('history')
                hotspot (355, 282, 52, 52) action ShowMenu('save')
                hotspot (435, 282, 52, 52) action ShowMenu('load')
                hotspot (597, 282, 52, 52) action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation(tag="menu"):
    modal True

    style_prefix "navigation"

    hbox:

        yalign 0.15
        xalign 0.5
        spacing 25
        xoffset -25
        # Menu from start screen
        if main_menu:
            textbutton _("Load") action ShowMenu("load")
            textbutton _("Options") action ShowMenu("preferences")
            textbutton _("Help") action ShowMenu("help")
            textbutton _("Return") action Return() 
        # In game menu
        else:
            textbutton _("Resume"):
                if not tutorial_on:
                    action Return() 
            if seen_tutorial_map: # TODO: Not working because map default first view
                textbutton _("Map"):
                    if not tutorial_on:
                        action [SetVariable("last_menu_screen", "manor_map"), ShowMenu("manor_map")]
            if seen_tutorial_description_hidden:
                textbutton _("Characters"):
                    if not tutorial_on:
                        action [SetVariable("last_menu_screen", "characters"), ShowMenu("characters")]
            # textbutton _("Objects") action ShowMenu("objects")
            if seen_tutorial_progress:
                textbutton _("Progress"):
                    if not tutorial_on:
                        action [SetVariable("last_menu_screen", "progress"), ShowMenu("progress")]
            textbutton _("Log"):
                if not tutorial_on:
                    action [SetVariable("last_menu_screen", "history"), ShowMenu("history")]
            # textbutton _("About") action ShowMenu("about")
            textbutton _("Help"):
                if not tutorial_on:
                    action [SetVariable("last_menu_screen", "help"), ShowMenu("help")]
            textbutton _("Options"):
                if not tutorial_on:
                    action [SetVariable("last_menu_screen", "preferences"), ShowMenu("preferences")]
            # textbutton _("Save") action ShowMenu("save") 
            # textbutton _("Save") action FileSave(None)
            textbutton _("Save"):
                if not tutorial_on:
                    action QuickSave()
            textbutton _("Quit"):
                if not tutorial_on:
                    action [QuickSave(),Show("confirmbutton")]

    #textbutton _("Return") action Return() xalign 0.95 yalign 0.93


style navigation_button
style navigation_button_text:
    size 60
    hover_color u"#715e46"
    selected_idle_color u"#715e46"
    idle_color u"#3d3d3d"

style navigation_button

style navigation_button_text



## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu
    style_prefix "main_menu"

    add gui.main_menu_background

    frame:
        style "main_menu_frame"
    vbox:
        xpos 280
        ypos 330
        # $ last_save = renpy.newest_slot(r"auto+")
        # $ last_save = renpy.newest_slot()
        $ last_save = renpy.newest_slot(r"quick+")
        # $ print(str(last_save))
        if last_save is not None:
        #     $ name, page = last_save.split("-")
            # $ print(name, page)
            # textbutton _("Continue") action FileLoad(name, page)
            # textbutton _("Continue") action FileLoad (1, confirm = False, page = "auto", newest = True)
            textbutton _("Continue") action QuickLoad()

        # textbutton _("Continue") action Start() at button0
        textbutton _("New Game") action Start() at button1
        # textbutton _("Load") action ShowMenu("load") at button2
        textbutton _("Debug") action Start("start_debug") at button2
        textbutton _("Options") action ShowMenu("preferences")at button3
        textbutton _("Help") action ShowMenu("help") at button4
        # textbutton _("About") action ShowMenu("about") at button5
        textbutton _("Quit") action Quit(confirm=not main_menu) at button5
        

    # add "gui/overlay/main_menu_logo.png"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text
style main_menu_button_text:
    size 70
    idle_color u"#4e4e4e"
    hover_color u"#766249"
style main_menu_button:
    spacing -20
    bottom_margin -28

style main_menu_frame:
    background "gui/overlay/main_menu.png"

style main_menu_vbox


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        xoffset -250
                        yoffset 100
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude
                elif scroll == "fixed": # OLPI changes
                    fixed:
                        xoffset -450
                        yoffset 115

                        transclude

                else:

                    transclude

    use navigation

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text
style about_text:
    text_align 0.5

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))

    add "gui/overlay/save_overlay.png"


screen load():

    tag menu

    use file_slots(_("Load"))

    add "gui/overlay/save_overlay.png"


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:
            xpos -250

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                yalign 1.0
                yoffset -50
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                            yoffset 20
                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)



            ## Buttons to access other pages.

    imagebutton auto "gui/button/page_button_left_%s.png" yalign 0.5 xoffset 100 yoffset 50 action FilePagePrevious() at page_button_left
    imagebutton auto "gui/button/page_button_right_%s.png" yalign 0.5 xalign 1.0 xoffset -100 yoffset 50 action FilePageNext() at page_button_right

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text:
    color u"#2b2b2b"

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    yoffset 15

style slot_button_text:
    properties gui.button_text_properties("slot_button")

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu
    style_prefix "pref"

    # $ _game_menu_screen = "preferences"

    if main_menu:
        add gui.main_menu_background
    add "gui/overlay/game_menu.png"
    use navigation
    imagemap:
        ground 'gui/overlay/pref_overlay_ground.png'
        idle 'gui/overlay/pref_overlay_ground.png'
        hover 'gui/overlay/pref_overlay_ground.png'
        selected_idle 'gui/overlay/pref_overlay_hover.png'
        selected_hover 'gui/overlay/pref_overlay_hover.png'
        cache False


        ##BARS

        hotbar (264, 452, 499, 42) mouse "hover" value Preference('music volume')
        hotbar (264, 563, 499, 42) mouse "hover" value Preference('sound volume')
        hotbar (264, 674, 499, 42) mouse "hover" value Preference('text speed')
        hotbar (264, 785, 499, 42) mouse "hover" value Preference('auto-forward time')

        ##BAR LABELS
        text _("Music") xpos 264 ypos 411
        text _("Sound") xpos 264 ypos 521
        text _("Text speed") xpos 264 ypos 631
        text _("Auto-forward") xpos 264 ypos 741


    imagemap:
        idle 'gui/overlay/pref_overlay_ground.png'
        hover 'gui/overlay/pref_overlay_hover.png'
        cache False


        ##Display button
        hotspot (1087, 415, 584, 65) action If(preferences.fullscreen==False, Preference('display', 'fullscreen'), Preference('display', 'window'))
        ##Display labels
        if preferences.fullscreen == False:
            label _("Window") xpos 1290 ypos 410
        else:
            label _("Fullscreen") xpos 1280 ypos 410

        ##Rollback button
        hotspot (1087, 548, 584, 65):
            if preferences.desktop_rollback_side == "disable":
                action Preference("rollback side", "left")
            elif preferences.desktop_rollback_side == "left":
                action Preference("rollback side", "right")
            else:
                action Preference("rollback side", "disable")

        ##Rollback labels
        if preferences.desktop_rollback_side == "disable":
            label _("Disabled") xpos 1290 ypos 542
        elif preferences.desktop_rollback_side == "left":
            label _("Left") xpos 1345 ypos 542
        else:
            label _("Right") xpos 1330 ypos 542

        text _("Display") xpos 1087 ypos 375
        text _("Rollback") xpos 1087 ypos 508

    vbox:
        xsize 500
        xpos 1170
        ypos 650
        style_prefix "check"
        textbutton _("Skip Unseen Text") action Preference("skip", "toggle") xalign 1.0
        textbutton _("Skip After Choices") action Preference("after choices", "toggle") xalign 1.0
        textbutton _("Skip Transitions") action InvertSelected(Preference("transitions", "toggle")) xalign 1.0


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button
style check_button_text:
    size 40
    idle_color u"#4e4c49"
    hover_color u"#6d5d4a"
    selected_hover_color u"#977956"
    selected_idle_color u"#6d5d4a"
style check_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label

style pref_label_text:
    yalign 0.5
    size 50
    color u"#2a2928"
style pref_text:
    color u"#4e4c49"

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu
    if main_menu:
        add gui.main_menu_background
    add "gui/overlay/game_menu.png"
    use navigation

    ## Avoid predicting this screen, as it can be very large.
    predict False

    vbox:
        xalign 0.5
        ypos 350
        viewport id "vpgrid":
            yinitial 1.0
            draggable True
            scrollbars "vertical"
            mousewheel True
            xmaximum 1000
            ymaximum 600
            yfill True
            vbox:
                xsize 960

                for h in _history_list:

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        substitute False

                    if h.who:
                        text "— " + h.who xalign 1.0 text_align 1.0
                    add "gui/divider.png" xalign 0.5 xoffset 20

                if not _history_list:
                    label _("The dialogue history is empty.") xalign 0.5
    add "gui/overlay/history_overlay.png"

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }

style history_vscrollbar:
    unscrollable gui.unscrollable

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu
    style_prefix "help"
    if main_menu:
        add gui.main_menu_background
    add "gui/overlay/game_menu.png"
    use navigation

    add "gui/overlay/help_overlay.png"

    viewport:
        xpos 228
        ypos 415
        xsize 579
        ysize 448

        scrollbars "vertical"
        draggable True
        mousewheel True
        vbox:
            vbox:
                label _("Enter")
                text _("Advances dialogue and activates the interface.")

            vbox:
                label _("Space")
                text _("Advances dialogue without selecting choices.")

            vbox:
                label _("Arrow Keys")
                text _("Navigate the interface.")

            vbox:
                label _("Escape")
                text _("Accesses the game menu.")

            vbox:
                label _("Ctrl")
                text _("Skips dialogue while held down.")

            vbox:
                label _("Tab")
                text _("Toggles dialogue skipping.")

            vbox:
                label _("Page Up")
                text _("Rolls back to earlier dialogue.")

            vbox:
                label _("Page Down")
                text _("Rolls forward to later dialogue.")

            vbox:
                label "H"
                text _("Hides the user interface.")

            vbox:
                label "S"
                text _("Takes a screenshot.")

            vbox:
                label "V"
                text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    viewport:
        xpos 1121
        ypos 415
        xsize 579
        ysize 448

        scrollbars "vertical"
        draggable True
        mousewheel True
        vbox:
            vbox:
                label _("Left Click")
                text _("Advances dialogue and activates the interface.")

            vbox:
                label _("Middle Click")
                text _("Hides the user interface.")

            vbox:
                label _("Right Click")
                text _("Accesses the game menu.")

            vbox:
                label _("Mouse Wheel Up/Click Rollback Side")
                text _("Rolls back to earlier dialogue.")

            vbox:
                label _("Mouse Wheel Down")
                text _("Rolls forward to later dialogue.")



style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text
style help_hbox:
    spacing 30

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label

style help_label_text:
    size gui.text_size



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style clock_frame:
    background Frame(["images/ui/clock_frame_white_2.png"], Borders(60, 60, 60, 60), tile=gui.frame_tile)
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

##IN-game quit button

screen confirmbutton():

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Are you sure you want to quit?\n{color=#AAAAAA}{i}Your progress has been saved automatically{/i}{/color}"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Quit game") action Quit(confirm=False)
                textbutton _("Quit to main menu") action MainMenu(confirm=False)
                textbutton _("No          ") action Null


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 1000
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 5 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
