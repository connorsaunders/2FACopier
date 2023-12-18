#!/usr/bin/env python3
import subprocess
import time
import re
import pyperclip
import os


# Get notifications:
def get_notifications():
    # Apple script command:
    osascript_cmd = ["osascript", "get_notification.scpt"]
    result = subprocess.run(osascript_cmd, capture_output=True, text=True).stdout.strip()
    notifications = result.splitlines()
    split_notifications = [tuple(n.split("|||")) for n in notifications]
    return split_notifications


def main():
    last_notifications = []
    while True:
        current_notifications = get_notifications()
        new_notifications = [n for n in current_notifications if n not in last_notifications]
        for notification in new_notifications:
            print(notification)

            # Find the last non-empty element in the notification
            body = next((item for item in reversed(notification) if item), None)
            if not body:
                continue  
            if "code" in body.lower():
                #matches = re.findall(r'\b\d{4,8}\b', body)
                matches = re.findall(r'\b\d{1,4}-?\d{1,5}\b', body)

                for match in matches:
                    print(f"CODE FOUND: {match}")
                    pyperclip.copy(match)  # Copy the found code to clipboard
                    print("Code copied to clipboard.")
                    os.system('afplay /System/Library/Sounds/Glass.aiff')  # Play a sound on macOS


        last_notifications = current_notifications[:]
        time.sleep(1)

if __name__ == "__main__":
    main()