# imports
import json
from functools import partial
from pathlib import Path

import keyboard

import utils
import consts

# constants
WELCOME_CREATE = \
"""Welcome to the sequence creator!
Press ` to replay your sequence.
To exit, press Esc."""

INTERACTIVE_MENU = \
"""Choose an option from the menu below:
1. Create a new sequence
2. Load a sequence
3. Load and play a sequence
"""

INTERACTIVE_LOAD = \
"""What would you like to do with the current sequence?
1. Play
2. Edit
3. Play, then exit
"""
OPTIONS = ('1', '2', '3')

# functions
def create(seq=None):
    print(WELCOME_CREATE)
    if seq is None:
        seq = []
    else:
        print(''.join(seq), end='', flush=True)
    keyboard.on_press(
        partial(utils.play_key, seq=seq, sounds=utils.sounds)
    )
    while True:
        keyboard.wait('esc')
        keyboard.unhook_all()
        break
    print()
    confirm = input('Would you like to save this sequence (y/n)? ').lower().strip()
    if confirm == 'y':
        name = input(
            'Type a name for this sequence (note: this will'\
            ' overwrite any sequence with the same name!): '
        )
        save(seq, name)

def save(seq, name):
    seq_path = Path(__file__).resolve().parent / 'sequences' / f'{name}.json'
    with open(seq_path, 'w') as f:
        json.dump(seq, f)

def load(seq_path):
    with open(seq_path) as f:
        seq = json.load(f)

    return seq

def interactive():
    option = input(INTERACTIVE_MENU).strip()
    if not option.isdigit():
        print("No.")
        return
    elif option not in OPTIONS:
        print("Choose a valid option.")
        return
    elif option == '1':
        create()
    elif option == '2':
        seq_name = input("What is the name of the sequence (do not use the full path)? ").strip(consts.STRIP_FILENAME)
        seq_path = Path(__file__).resolve().parent / 'sequences' / f"{seq_name}.json"
        seq = load(seq_path)
        while True:
            option_seq = input(INTERACTIVE_LOAD).strip()
            if not option_seq.isdigit():
                print("No.")
                return
            elif option_seq not in OPTIONS:
                print("Choose a valid option.")
                return
            elif option_seq == '1':
                utils.play_key('load', sounds=utils.sounds, seq=seq)
                print()
            elif option_seq == '2':
                create(seq)
            

    elif option == '3':
        pass