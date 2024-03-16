transform smaller:
    zoom 0.5

define a = Character("Alisa")
define m = Character("Mom")

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black 
    with dissolve
    pause(0.5)

    scene bedroom
    with dissolve

    play sound "alarm.wav" volume(0.35) loop
    "It was just a regular morning when my alarm clock pierced through the silence, jolting me awake."
    play sound "click.wav" volume(0.9)
    "I groggily turned it off and walked over to the kitchen to meet my mom."

    ""
    return
