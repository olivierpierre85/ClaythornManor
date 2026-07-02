# Threads & Endings overview screens
#
# Both screens share the same layout: portrait on the left, three day columns
# (Friday / Saturday / Sunday) with one subtitle per chapter and info cards.
#
# Threads view modes:
#   - "chapters"          : chapters where the thread can be unlocked
#   - "relevant_chapters" : chapters where the thread is used (Impact view)
# The Impact view is disabled for now - set show_impact_toggle to True to
# bring back the Unlocks/Impact toggle.

define threads_day_layout = [
    ("Friday", ["friday_afternoon", "friday_evening"]),
    ("Saturday", ["saturday_morning", "saturday_afternoon", "saturday_afternoon_no_hunt", "saturday_evening"]),
    ("Sunday", ["sunday_morning", "sunday_afternoon", "end"]),
]

# Share of the width given to each day column, in the order of
# threads_day_layout (values should add up to 1.0). Saturday holds the most
# threads, so it gets the widest column. To try another balance
# (e.g. 0.25 / 0.50 / 0.25), edit these values and press Shift+R in the
# running game to reload. The number of cards per row adapts automatically.
define threads_screen.day_widths = [0.25, 0.45, 0.30]

define threads_screen.area_width = 1300      # total width of the columns area
define threads_screen.column_spacing = 40    # gap between day columns
define threads_screen.card_slot = 88         # 75px card + 13px grid spacing

define threads_screen.day_title_size = 40
define threads_screen.chapter_title_size = 28

define threads_screen.show_impact_toggle = False


# Left column shared by both overview screens: name, portrait, progress bar
screen overview_portrait_column(selected_char, bar_value):

    vbox:
        spacing 10
        yalign 0.0

        text selected_char.real_name:
            size 48
            font gui.name_text_font
            color gui.accent_color
            outlines [ (absolute(1), "#140303", absolute(0), absolute(0)) ]

        add "images/characters/side/side " + selected_char.text_id + ".png"

        bar:
            value bar_value
            range 100
            xmaximum 260
            style 'progress_bar'


# The three day columns, filled with threads or endings depending on source
screen overview_day_columns(selected_char, source="threads", threads_view="chapters"):

    $ usable_width = threads_screen.area_width - threads_screen.column_spacing * (len(threads_day_layout) - 1)

    viewport:
        xmaximum threads_screen.area_width
        ymaximum 680
        draggable True
        mousewheel True
        scrollbars "vertical"
        # Only show the scrollbar when the content overflows
        vscrollbar_unscrollable "hide"

        hbox:
            spacing threads_screen.column_spacing

            for day_index, (day_label, day_chapters) in enumerate(threads_day_layout):
                $ column_width = int(usable_width * threads_screen.day_widths[day_index])
                $ cards_per_row = max(1, (column_width + 13) // threads_screen.card_slot)
                if source == "endings":
                    $ day_items = [(key, selected_char.get_endings_for_chapter(key)) for key in day_chapters]
                else:
                    $ day_items = [(key, selected_char.get_threads_for_chapter(key, threads_view)) for key in day_chapters]
                $ day_items = [(key, items) for key, items in day_items if items]

                vbox:
                    xminimum column_width
                    xmaximum column_width
                    spacing 15

                    text day_label:
                        font gui.name_text_font
                        color gui.accent_color
                        size threads_screen.day_title_size

                    if not day_items:
                        text _("Nothing here"):
                            font gui.name_text_font
                            color gui.insensitive_color
                            size threads_screen.chapter_title_size
                    else:
                        for key, items in day_items:
                            $ found = len([item for item in items if item.discovered])
                            $ subtitle = chapters_names[key] + "   " + str(found) + "/" + str(len(items))

                            text subtitle:
                                font gui.name_text_font
                                size threads_screen.chapter_title_size
                                if found == len(items):
                                    color gui.insensitive_color
                                else:
                                    color "#FFFFFF"

                            $ number_of_rows = ((len(items) + cards_per_row - 1) // cards_per_row)
                            grid cards_per_row number_of_rows:
                                spacing 13
                                for item in items:
                                    if source == "endings":
                                        use info_card(item, 'ending')
                                    else:
                                        use info_card(item, item.type, dimmed=(threads_view == "relevant_chapters" and key not in item.chapters))


screen character_threads(selected_char):

    tag menu

    # info_card computes lock state from current_checkpoint when it is set,
    # and the progress screen leaves it populated
    on "show" action SetVariable("current_checkpoint", None)

    default threads_view = "chapters"

    use game_menu(_("Storyline"), scroll="fixed"):

        fixed:
            hbox:
                xpos 80
                ypos 20
                spacing 60
                yalign 0.0

                use overview_portrait_column(selected_char, selected_char.get_character_progress_choices_and_discoveries())

                # Right side: the three day columns
                vbox:
                    spacing 20
                    yalign 0.0

                    if threads_screen.show_impact_toggle:
                        hbox:
                            spacing 50

                            textbutton _("Unlocks"):
                                text_font gui.name_text_font
                                text_size 36
                                action SetScreenVariable("threads_view", "chapters")
                                if threads_view == "chapters":
                                    text_color gui.highlight_color
                                else:
                                    text_color gui.accent_color
                                text_hover_color gui.hover_color

                            textbutton _("Impact"):
                                text_font gui.name_text_font
                                text_size 36
                                action SetScreenVariable("threads_view", "relevant_chapters")
                                if threads_view == "relevant_chapters":
                                    text_color gui.highlight_color
                                else:
                                    text_color gui.accent_color
                                text_hover_color gui.hover_color

                    use overview_day_columns(selected_char, "threads", threads_view)

        fixed:
            textbutton _("Return"):
                align (1.0, 1.0)
                xoffset 400
                yoffset -150
                if not tutorial_on:
                    action ShowMenu("progress")

    use tooltip_display

    use tutorial_with_steps(tutorial_steps_threads, tutorial_step_threads, "tutorial_step_threads")


screen character_endings(selected_char):

    tag menu

    # info_card computes lock state from current_checkpoint when it is set,
    # and the progress screen leaves it populated
    on "show" action SetVariable("current_checkpoint", None)

    use game_menu(_("Storyline"), scroll="fixed"):

        fixed:
            hbox:
                xpos 80
                ypos 20
                spacing 60
                yalign 0.0

                use overview_portrait_column(selected_char, selected_char.get_character_progress_endings())

                vbox:
                    spacing 20
                    yalign 0.0

                    use overview_day_columns(selected_char, "endings")

        fixed:
            textbutton _("Return"):
                align (1.0, 1.0)
                xoffset 400
                yoffset -150
                if not tutorial_on:
                    action ShowMenu("progress")

    use tooltip_display

    use tutorial_with_steps(tutorial_steps_endings, tutorial_step_endings, "tutorial_step_endings")
