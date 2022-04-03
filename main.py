"""
Cookie Clicker Bot.
This will be the main logic.

Hold down to kill program when running!
"""
import keyboard
import pyautogui
import time
from bot import CookieBot

running = True
upgrade_count = 1
upgrade_limit = 50000

bot = CookieBot()

bot.find_click_special_cookie()
while running:
    bot.click_cookie()

    if upgrade_count % upgrade_limit == 0:
        print("Upgrading Stuff")
        upgrade_count = 0
        for location in bot.active_locations:
            pyautogui.click(location["x"], location["y"])
            time.sleep(.5)
    elif upgrade_count % 100 == 0:
        print(f"Upgrade Count: {upgrade_count} / {upgrade_limit}")

    if keyboard.is_pressed('down'):
        running = False
        print('Killing Program.........')

    upgrade_count += 1
    time.sleep(.0001)
