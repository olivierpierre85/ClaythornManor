# Custom Menu System Guide

This guide explains how to use and extend the custom menu system in your project.

## 1. Defining a New Menu

Menus are created using the `TimedMenu` class. Each menu has a unique ID and a list of choices.

```python
menu = TimedMenu(
    id="example_menu",
    choices=[
        TimedMenuChoice("Ask about the weather", "weather_label", time_spent=5),
        TimedMenuChoice("Leave", "leave_label", early_exit=True)
    ]
)
```

## 2. Adding Choices

Choices are instances of `TimedMenuChoice`. You can specify:
- `text`: The button text
- `redirect`: The label or function to call
- `time_spent`: Minutes spent on this choice
- `early_exit`: If true, menu closes after this choice
- `condition`: Python expression (as a string) for visibility
- `keep_alive`: If true, choice remains visible after selection
- `linked_choice`: For chaining completion logic

Example:
```python
TimedMenuChoice(
    "Ask about the weather", "weather_label", time_spent=5, condition="current_day == 'Friday'"
)
```

## 3. Advanced Features

### Conditional Choices
Use the `condition` argument to show/hide choices based on game state. Conditions are evaluated safely.

```python
TimedMenuChoice("Secret Option", "secret_label", condition="player_has_key")
```

### Chaining and Linked Choices
Use `next_menu` or `linked_choice` to chain menus or require completion of another choice.

### Map Menus
Set `is_map=True` in `TimedMenu` to use the map interface. Assign `room` to choices.

## 4. UI Feedback
- **Completed choices**: Grayed out with a checkmark.
- **Hidden choices**: Not shown.
- **Locked choices**: (Optional) Add a `locked` property and a lock icon in the UI.

## 5. Running a Menu
Call the `run_menu` label with your menu:
```renpy
call run_menu(menu)
```

## 6. Tips
- Use docstrings and comments in your menu definitions for clarity.
- Use the `MenuManager` class to manage menu state.
- Avoid using unsafe code in conditions; only use whitelisted variables.

---
For more details, see the code in `scripts/custom_menu_classes.rpy` and `scripts/custom_menus.rpy`. 