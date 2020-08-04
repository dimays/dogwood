"""Module containing the UI elements of Dogwood, including a set of
default color palettes and urwid widgets for handling all display
elements."""

import urwid


class GameWindow:
    """This is the topmost widget, a placeholder that wraps the game's
    current screen.

    By default, the first widget to occupy GameWindow is SplashScreen.
    """
    def __init__():
        pass


class SplashScreen:
    """An optional widget to load before starting the game.

    By default, this widget shows a brief Dogwood animation. It covers
    the screen and can animate a series of frames.

    By default, the SplashScreen's min_duration is 5s, and any click of
    keystroke will skip it. Both of these settings can be changed.

    If Playsound functionality is added, also include the ability to
    play a sound wth the SplashScreen.
    """
    def __init__():
        pass


class TitleScreen:
    """The initial screen of the game, before the player starts a new
    game or loads a saved file.

    By default, this widget shows the title of the game in BigText,
    with Menu items [New Game], [Load Game], [Settings], [How to Play]
    in the bottom-left corner, left justified.

    You may change the style of the title and the menu items, and you
    may exclude menu items from this list.
    """
    def __init__():
        pass


class FileSelectScreen:
    """A screen with up to three SaveFiles to select. The player may
    select a file then load or delete the file, or if the file is
    empty, may begin a new game.

    If SaveFiles are used, this screen appears at the selection of
    [Load Game] from the TitleScreen.
    """
    def __init__():
        pass


class MainGameScreen:
    """The primary screen of the game, where the player can read
    the game's story as they play, enter commands, and navigate the
    main menu selections.

    By default, this widget shows the title of the game in the
    upper-left corner, the [HELP] button in the upper-right corner,
    the StoryBox, CommandLine, and four buttons in the footer:
    [MAP], [INVENTORY], [SETTINGS], and [QUIT].

    You may exclude any items from this list.
    """
    def __init__():
        pass


class HelpScreen:
    """Get some basic tips about how to play the game.

    By default, the help text details how to do essential Dogwood
    actions, such as entering commands to explor the world of each
    game.

    You may add additiona help instructions specific to your game,
    or completely replace the default help text with your own.
    """
    def __init__():
        pass


class SettingsMenu:
    """An optional menu available to the player for changing certain
    game settings, such as disabling AutoComplete, setting text speed,
    disabling color coding, changing the color palette, changing the
    color mode.

    This menu also contains options to export the current story as a
    text file.
    """
    def __init__():
        pass


class BattleScreen:
    """A variation on the MainGameScreen in which the CommandLine is
    replaced with customizable button menus for selecting your actions.

    The Button menu can be replaced with a CommandLine if the developer does
    not wish to have button menu navigation in their game.

    Once the battle is finished, the summary of the battle is added to the
    Story, and the MainGameScreen is loaded again.
    """
    def __init__():
        pass
