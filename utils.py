# imports
import string
from functools import partial
from pathlib import Path

import keyboard
import pygame

import consts

# initializations
pygame.init()
sequences = Path('sequences')
if not sequences.exists():
    sequences.mkdir()

elif sequences.is_file():
    sequences.unlink()
    sequences.mkdir()

# functions
def load_sound_bank(bank_name, from_dir='.', extension='wav'):
    """Load a sound bank containing A-Z sound files."""
    bank_dir = Path(from_dir) / bank_name

    if not bank_dir.is_dir():
        return None

    bank = {
        letter: pygame.mixer.Sound(bank_dir / f'{letter}.{extension}')
        for letter in string.ascii_uppercase
    }
    bank['SPACE'] = pygame.mixer.Sound(buffer=bytes(24696))

    return bank

def clear_screen():
    print(f'\033[2J\033[H', end='\r')

def play_sequence(seq):
    for note in seq:
        print(note.replace('SPACE', ' '), end='', flush=True)
        channel = sounds[note.replace(' ', 'SPACE')].play()
        while channel.get_busy():
            pygame.time.wait(1)

def play_key(event, sounds, seq=None):
    create = seq is not None

    if seq is None:
        seq = []
    
    key = '`' if event == 'load' else event.name.upper()
    
    if key == '`' and create:
        clear_screen()
        play_sequence(seq)

    elif key == 'BACKSPACE' and create:
        clear_screen()
        if seq:
            seq.pop()
        print(''.join(seq), end='', flush=True)

    elif key in sounds:
        seq.append(key.replace("SPACE", ' '))
        sounds[key].play()
        print(key.replace('SPACE', ' '), end='', flush=True)
        
def live_keyboard():
    seq = []
    keyboard.on_press(
        partial(play_key, sounds=sounds)
    )
    keyboard.wait('esc')
    keyboard.unhook_all()
    print()  # newline

if __name__ == "utils":
    sounds = load_sound_bank('normal')
