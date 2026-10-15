# imports
import utils
import consts
import sequencer


# functions
def test1():
    test = utils.load_sound_bank('normal')
    for k, v in test.items():
        input(f"Press Enter to play {k}")
        v.play()

def test2():
    sequencer.create()

def test3():
    bank = utils.load_sound_bank('normal')
    seq = sequencer.load('test')
    utils.play_key('load', bank, seq=seq)
    print()

def test4():
    sequencer.interactive()

def main():
    utils.live_keyboard()

# main section
if __name__ == "__main__":
    if consts.DEBUG['on']:
        print("Debug enabled. To disable, edit consts.py to set the 'on' value to False.")
        if consts.DEBUG['sound_test']:
            test1()
        if consts.DEBUG['sequencer_tests']['create']:
            test2()
        if consts.DEBUG['sequencer_tests']['load']:
            test3()
        if consts.DEBUG['sequencer_tests']['interactive']:
            test4()
    main()

