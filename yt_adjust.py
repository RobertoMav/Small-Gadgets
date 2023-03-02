
import pyautogui
import time

def main():
    #Locate yt search button to max screen
    try:
        x, y = pyautogui.locateCenterOnScreen('./pics/top.png', grayscale=True, confidence=0.3)
    except TypeError:
        print("Yt page not found, only identified on main display")
        return

    # activate the Chrome window
    pyautogui.moveTo(x/2, y=(y/2)-50)
    pyautogui.click()

    # wait for the window to activate
    time.sleep(.2)
    pyautogui.hotkey('ctrl', 'option', 'enter')

    #Click on 'c' -- subtitles
    time.sleep(0.2)
    pyautogui.press('c')

    #Click on 'settings' button
    pyautogui.moveTo(x=700, y=550, duration=1)
    time.sleep(0.2)

    pyautogui.moveTo(x=1100, y=878)
    pyautogui.click()

    time.sleep(0.2)

    #click on annotations
    pyautogui.moveTo(x=1240, y=693)
    pyautogui.click()

    time.sleep(0.2)

    #click on playback speed
    pyautogui.moveTo(x=1240, y=733)
    pyautogui.click()

    time.sleep(0.2)
        #click on 2x
    pyautogui.moveTo(x=1200, y=815)
    pyautogui.click()

    time.sleep(0.2)

    #click on quality
    pyautogui.moveTo(x=1240, y=815)
    pyautogui.click()

    time.sleep(0.2)

    # find if video has 4k on it
    try:
        x4k, y4k = pyautogui.locateCenterOnScreen('./pics/4K.png', confidence=0.5, grayscale=True)
        pyautogui.moveTo(x=x4k/2, y=y4k/2)
        pyautogui.click()
    
    #if not found, sets to HD
    except TypeError:
        pyautogui.moveTo(x=1200, y=570)
        pyautogui.click()


if __name__=='__main__':
    main()