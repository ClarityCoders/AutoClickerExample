"""
Cookie Clicker Bot.
This will be the main logic.

Hold down to kill program when running!
"""
import keyboard
import pyautogui
import random
import time

click_locations = [
    {
        "name": "Cursor",
        "x": 1722,
        "y": 325,
    }, {
        "name": "Grandma",
        "x": 1722,
        "y": 390,
    }, {
        "name": "Farm",
        "x": 1722,
        "y": 456,
    }, {
        "name": "Mine",
        "x": 1722,
        "y": 522,
    }, {
        "name": "Factory",
        "x": 1722,
        "y": 585,
    }, {
        "name": "Bank",
        "x": 1722,
        "y": 650,
    }, {
        "name": "Temple",
        "x": 1722,
        "y": 717,
    }, {
        "name": "Wizard Tower",
        "x": 1722,
        "y": 775,
    }, {
        "name": "Shipment",
        "x": 1722,
        "y": 840,
    }, {
        "name": "Alchemy lab",
        "x": 1722,
        "y": 902,
    }, {
        "name": "Portal",
        "x": 1722,
        "y": 925,
    }, {
        "name": "Time Machines",
        "x": 1722,
        "y": 1032,
    }, {
        "name": "Store",
        "x": 1632,
        "y": 216,
    },
]

running = True
upgrade_count = 1
upgrade_limit = 1000

time.sleep(5)

while running:

    pyautogui.click(random.randint(200, 380), random.randint(400, 580))

    if upgrade_count % upgrade_limit == 0:
        print("Upgrading Stuff")
        upgrade_count = 0
        for location in click_locations[::-1]:
            pyautogui.click(location["x"], location["y"])
            time.sleep(.5)
    elif upgrade_count % 100 == 0:
        print(f"Upgrade Count: {upgrade_count} / {upgrade_limit}")

    if keyboard.is_pressed('down'):
        running = False
        print('Killing Program.........')

    upgrade_count += 1
    time.sleep(.0001)
