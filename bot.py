"""
Main bot class for program.
Will handle finding click locations and pyautogui functions
"""

import cv2
import numpy as np
import mss
import pyautogui
import random

sct = mss.mss()

class CookieBot():

    def __init__(self):
        self.cookie = {
            "name": "Cookie",
        }
        self.special_cookie = {
            "name": "SpecialCookie",
        }
        self.click_locations = [
            {
                "name": "Cursor",
            }, {
                "name": "Grandma",
            }, {
                "name": "Farm",
            }, {
                "name": "Mine",
            }, {
                "name": "Factory",
            }, {
                "name": "Bank",
            }, {
                "name": "Temple",
            }, {
                "name": "Wizard",
            }, {
                "name": "Shipment",
            }, {
                "name": "Alchemy",
            }, {
                "name": "Portal",
            }, {
                "name": "Time",
            }, {
                "name": "Anti",
            },{
                "name": "Store",
            },
        ]
        self.find_click_locations()

    def find_click_locations(self):
        """
        When called determine location of cookie and Menu Items.
        """

        # Find location of cookie.
        location = find_locations(self.cookie["name"])
        if location is not None:
            self.cookie["location"] = location
            self.cookie["found"] = True
        else:
            self.cookie["found"] = False

        for click_location in self.click_locations:
            location = find_locations(click_location["name"])
            if location is not None:
                click_location["location"] = location
                click_location["found"] = True
            else:
                click_location["found"] = False

    def active_locations(self):
        active_list = []
        for click_location in self.click_locations:
            if click_location["found"]:
                active_list.append(click_location)

        return active_list

    def find_main_cookie(self):
        if self.cookie["found"]:
            return True
        return False

    def find_click_special_cookie(self):
        location = find_locations(self.special_cookie["name"], .5)
        print(f"{location}HEY")
        if location is not None:
            self.special_cookie["location"] = location
            self.special_cookie["found"] = True
            pyautogui.click(bot.cookie["location"])
        else:
            self.special_cookie["found"] = False

    def click_cookie(self, jiggle=True):
        if self.find_main_cookie():
            if jiggle:
                x = self.cookie["location"][0] + random.randint(-5, 5)
                y = self.cookie["location"][1] + random.randint(-5, 5)
                pyautogui.click((x, y))
            else:
                pyautogui.click(self.cookie["location"])


def find_locations(needle, threshold=.95, debug=False):
    dimensions = {
        'left': 0,
        'top': 0,
        'width': 1920,
        'height': 1080
    }

    # Cut off alpha
    scr = np.array(sct.grab(dimensions))
    scr_remove = scr[:, :, :3]

    max_val = 0

    try:
        needle_img = cv2.imread(f'.\images\{needle}.jpg', cv2.IMREAD_UNCHANGED)
        result = cv2.matchTemplate(scr_remove, needle_img, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #print(f"Max Val: {max_val} Max Loc: {max_loc}")
    except Exception: 
        print(f"Couldn't Find file for .\images\{needle}.jpg")

    if debug:
        print(max_val, threshold, needle)

    if max_val > threshold:
        return max_loc
    else:
        return None


if __name__ == "__main__":
    bot = CookieBot()
    print(bot.active_locations())