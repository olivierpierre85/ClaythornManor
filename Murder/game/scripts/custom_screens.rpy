screen current_time:
    modal False

    $ current_hour = current_time.hour
    $ current_minutes = current_time.minute
    if current_hour >= 12:
        $ current_period = "Afternoon"
        $ current_hour = current_hour - 12
    else:
        $ current_period = "Morning"


    $ hours_angle = ((int(current_hour) * 60) + int(current_minutes))/2
    
    $ minutes_angle = int(current_minutes) * 6
    # Terrible quickfix to force clockwise rotation... (constant) TODO  replace???
    python:
        while old_minutes_angle > minutes_angle:
            minutes_angle = minutes_angle + 360

    add "images/ui/day_background.png"

    text "[current_day] [current_period]" xoffset 20

    imagebutton:
        xoffset 30
        yoffset 50
        idle "images/ui/clock_small.png" 

    add "images/ui/clock_hours.png" at rotate_hours(hours_angle)
    add "images/ui/clock_minutes.png" at rotate_minutes(minutes_angle)

    $ old_minutes_angle = minutes_angle
        
transform rotate_hours( angle = 0 ):
    xoffset -16
    yoffset 31
    linear 3.0 rotate angle 

transform rotate_minutes( angle = 0 ):
    xoffset -16
    yoffset 31 
    linear 3.0 rotate angle 

screen in_game_menu_btn:

    modal False

    zorder 1000

    style_prefix "confirm" # TODO use own style
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        ypadding 10
        textbutton _("Menu") action ShowMenu("manor_map")

# Display of storyline tree
screen objects:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Objects"), scroll="viewport"):

        style_prefix "object"

        vbox:
            text _("TODO imagemap with all objects, explanation on hover?")

# Display of storyline tree
screen storyline:
    tag menu

    ## TODO OLPI Add a image of the map
    ## add text with explanation of previously visited rooms if needed
    use game_menu(_("Storyline"), scroll="viewport"):

        style_prefix "map"

        vbox:
            text _("TODO story tree (One image map by user, possibility to change user with small button face")
