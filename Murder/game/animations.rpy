##ANIMATIONS
transform page_button_left():
    subpixel True
    yalign 0.5
    xpos 60
    linear 1.0 xpos 45
    linear 1.0 xpos 60
    repeat

transform page_button_right():
    subpixel True
    yalign 0.5
    xpos 1825
    linear 1.0 xpos 1840
    linear 1.0 xpos 1825
    repeat

transform button0():
    subpixel True
    alpha -0.2
    xpos -50
    linear 0.5 xpos 0 alpha 1.0

transform button1():
    subpixel True
    alpha 0.0
    xpos -50
    linear 0.5 xpos 0 alpha 1.0

transform button2():
    subpixel True
    alpha 0.0
    xpos -50
    pause 0.2
    linear 0.5 xpos 0 alpha 1.0

transform button3():
    subpixel True
    alpha 0.0
    xpos -50
    pause 0.4
    linear 0.5 xpos 0 alpha 1.0

transform button4():
    subpixel True
    alpha 0.0
    xpos -50
    pause 0.6
    linear 0.5 xpos 0 alpha 1.0

transform button5():
    subpixel True
    alpha 0.0
    xpos -50
    pause 0.8
    linear 0.5 xpos 0 alpha 1.0

transform button6():
    subpixel True
    alpha 0.0
    xpos -50
    pause 1.0
    linear 0.5 xpos 0 alpha 1.0


##BODY SPRITES
##
## The body_<character> images are built by tools/build_character_sprites.py.
## They are 880px tall and stand on the bottom edge of the screen, so the waist
## sits just behind the text box.
##
## Convention: show the people the player is looking at, and hide them again
## before a timed menu opens, since the menu shows its own portraits.

## Three people spread across the room.
transform body_left:
    subpixel True
    xcenter 0.22
    yalign 1.0

transform body_center:
    subpixel True
    xcenter 0.5
    yalign 1.0

transform body_right:
    subpixel True
    xcenter 0.78
    yalign 1.0

## Two people, standing a little closer together.
transform body_pair_left:
    subpixel True
    xcenter 0.30
    yalign 1.0

transform body_pair_right:
    subpixel True
    xcenter 0.70
    yalign 1.0

## Lighting, added after the position so the two can be combined:
##     show body_captain at body_left, body_focus
## Only needed when several people are on screen and one of them holds the
## attention. A character shown on their own needs no lighting transform, and a
## character whose lighting does not change need not be shown again.
transform body_focus:
    matrixcolor BrightnessMatrix(-0.18)
    linear 0.25 matrixcolor BrightnessMatrix(0.0)

transform body_dim:
    matrixcolor BrightnessMatrix(0.0)
    linear 0.25 matrixcolor BrightnessMatrix(-0.18)
