from pynput import keyboard
import time
import video.yt_adjust

controller = keyboard.Controller()

def time_it(func):
    def funct(*args, **kwargs):
        name = func.__name__
        #print(f"Executing {name}")
        t0 = time.time()
        run = func(*args, **kwargs)
        runtime = (time.time() - t0) * 1000
        if runtime > 0.1:
            print(f"Function {name} ran in: {runtime:.2f}")
        return run
    return funct

@time_it
def store_contents(char, string):
    ''' Store alphanum charact on a string'''
    try:
        string += char
    except TypeError:
        pass
    return string

@time_it
def remove_contents(string):
    '''Removes the last digit of the string'''
    try:
        string = string.rstrip(string[-1])
    except IndexError:
        pass

    return string

@time_it
def alter(string):
    ''' When space is pressed we read the data from store_content 
        and return bool = True == 1st digit is lower, remaining are upper
    '''

    if len(string) > 1 and string[0].islower() and string[1:].isupper():
        return True

    return False

@time_it
def alter_cont(string):
    '''Read string and alter its lower/upper to its opposite'''

    updated_string = string[0].upper()
    updated_string += string[1:].lower()

    return updated_string

@time_it
def run_backspace(string):
    #press delete key len(string) times

    for _ in range(len(string) + 1):
        controller.tap(keyboard.Key.backspace)

    return

@time_it
def write_string(string): 
    '''writes string with controler module'''

    for letter in string:
        controller.tap(letter)

    return

@time_it
def clear_string():

    string = ''

    return string




word = clear_string()

def on_press(key):
    try:

        global word
        word = store_contents(key.char, word)

    except AttributeError:

        if key == keyboard.Key.space: 

            if alter(word):
                word = alter_cont(word)
                run_backspace(word)
                write_string(word)
                controller.tap(keyboard.Key.space)
            word = clear_string()

        elif key == keyboard.Key.backspace:
            word = remove_contents(word)
        
        elif key == keyboard.Key.enter:
            word = clear_string()


def on_release(key):
    if key == keyboard.Key.f5:
        return False
    elif key == keyboard.Key.f6:
        video.yt_adjust.main()

with keyboard.Listener(on_press=on_press, on_release=on_release) as liste:
    liste.join()
