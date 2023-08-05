"""Main application function"""

# pylint: disable=fixme
# pylint: disable=too-many-nested-blocks
# pylint: disable=too-many-statements
# pylint: disable=too-many-branches
# pylint: disable=import-outside-toplevel
# ToDo: fix this

# todo: only import pygame if on graphical

import getopt
import sys
import time

from neopolitan.board_functions.board import Board
# from board_functions.colors import OFF, ON
from neopolitan.board_functions.board_data import default_board_data
from neopolitan.writing.data_transformation import str_to_data
from neopolitan.os_detection import on_pi
# pylint: disable=wildcard-import
from neopolitan.const import *


def main(events=None):
    """Make a very simple display"""

    board_data = process_arguments()

    width = WIDTH
    height = HEIGHT
    size = width*height
    board = None
    display = None
    board_display = None

    # todo: make better
    if board_data.graphical:
        from neopolitan.display.graphical_display import GraphicalDisplay
        board = Board(size)
        display = GraphicalDisplay(board=board)
    else:
        from neopolitan.display.hardware_display import HardwareDisplay
        display = HardwareDisplay(WIDTH*HEIGHT)
        board_display = display.board_display
        board = board_display.board

    board.set_data(str_to_data(board_data.message))

    while not display.should_exit:
        # process events
        # todo: make better
        while events and not events.empty():
            event = events.get()
            print('event:', event)
            event_list = event.split()
            first = event_list[0]
            if first == 'exit':
                return
            if first == 'say':
                print('e:', event)
                message = event_list[1]
                board.set_data(str_to_data(message))
                print('set message:', message)
            else: # try board data events
                board_data = process_board_data_events(board_data, event_list)
            # todo: error handling
        display.loop()
        if board_data.scroll_speed:
            board.scroll(wrap=board_data.should_wrap)

        time.sleep(board_data.scroll_wait)

    del display

def process_arguments():
    """Process the command line arguments and return them as a BoardData object"""
    board_data = default_board_data

    argument_list = sys.argv[1:]
    options = 'm:g:s:w:'
    long_options = ['message=', 'graphical=', 'scroll=', 'wrap=']
    try:
        # args, vals
        args = getopt.getopt(argument_list, options, long_options)
        if len(args[0]) > 0:
            for arg, val in args[0]:
                if arg in ('-m', '--message'):
                    board_data.message = val
                elif arg in ('-g', '--graphical'):
                    if val == 'True':
                        if on_pi():
                            print('This code cannot be run in graphical mode on a Raspberry Pi,'\
                                ' setting graphical to False')
                            board_data.graphical = False
                        else:
                            board_data.graphical = True
                    elif val == 'False':
                        if not on_pi():
                            print('This code cannot be run in hardware mode when not run'\
                            ' on a Raspberry Pi, setting graphical to True')
                            board_data.graphical = True
                        else:
                            board_data.graphical = False
                    else:
                        print('Could not parse "graphical" argument:', val)
                elif arg in ('-s', 'scroll'):
                    if val in ('slow', 'medium', 'fast'):
                        board_data.scroll_speed = val
                        if val == 'slow':
                            board_data.scroll_wait = SCROLL_FAST
                        elif val == 'medium':
                            board_data.scroll_wait = SCROLL_MED
                        else: # fast
                            board_data.scroll_wait = SCROLL_SLOW
                    else:
                        print('Invalid scroll speed:', val)
                elif arg in ('-w', 'wrap'):
                    if val == 'True':
                        board_data.should_wrap = True
                    elif val == 'False':
                        board_data.should_wrap = False
                    else:
                        print('Could not parse "wrap" argument:', val)
        print('message set to:', board_data.message)
        print('graphical set to:', board_data.graphical)
        print(f'scroll speed set to: {board_data.scroll_speed} ({board_data.scroll_wait})')
        print('wrap set to:', board_data.should_wrap)

    except getopt.error as err:
        print('getopt error:', str(err))

    return board_data

def process_board_data_events(board_data, event_list):
    """Manipulate board data according to events"""

    first = event_list[0]
    if first == 'speed':
        speed = event_list[1]
        if speed == 'slow':
            board_data.scroll_slow()
            print('set speed: slow')
        elif speed == 'medium':
            board_data.scroll_medium()
            print('set speed: medium')
        elif speed == 'fast':
            board_data.scroll_fast()
            print('set speed: fast')
        else:
            try:
                speed = float(speed)
                board_data.set_scroll_wait(speed)
                print('set speed: ', speed)
            except ValueError:
                print('Cannot parse speed: ', speed)

    return board_data

if __name__ == '__main__':
    main()
