import pyautogui
import time

time.sleep(1)

pyautogui.hotkey("alt", "tab")
pyautogui.hotkey("ctrl", "shift", "n")
pyautogui.write("youtube")
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=1056, y=560)

time.sleep(2)
pyautogui.click(x=894, y=119)

pyautogui.write("i will find")
pyautogui.press("enter")

time.sleep(2)
pyautogui.click(x=1277, y=819)