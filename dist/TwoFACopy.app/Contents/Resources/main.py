#!/usr/bin/env python3
import subprocess
import time
import re
import pyperclip
import os
import threading
import rumps

class NotificationWatcherApp(rumps.App):
    def __init__(self):
        super(NotificationWatcherApp, self).__init__("2FA")
        self.start_menu = rumps.MenuItem("Start")
        self.stop_menu = rumps.MenuItem("Stop", callback=None)  # Disabled initially
        self.menu = [self.start_menu, self.stop_menu]
        self.is_running = False
        self.notification_thread = None

    @rumps.clicked("Start")
    def start(self, _):
        if not self.is_running:
            self.is_running = True
            self.start_menu.set_callback(None)  # Disable the start menu item
            self.stop_menu.set_callback(self.stop)  # Enable the stop menu item
            rumps.notification(title="Notification Watcher", subtitle="Started", message="")
            self.notification_thread = threading.Thread(target=self.watch_notifications)
            self.notification_thread.start()

    @rumps.clicked("Stop")
    def stop(self, _):
        self.is_running = False
        self.start_menu.set_callback(self.start)  # Enable the start menu item
        self.stop_menu.set_callback(None)  # Disable the stop menu item
        if self.notification_thread:
            self.notification_thread.join()
        rumps.notification(title="Notification Watcher", subtitle="Stopped", message="")


    def watch_notifications(self):
        last_notifications = []
        while self.is_running:
            current_notifications = get_notifications()
            new_notifications = [n for n in current_notifications if n not in last_notifications]
            for notification in new_notifications:
                print(notification)
                self.handle_notification(notification)

            last_notifications = current_notifications[:]
            time.sleep(1)

    def handle_notification(self, notification):
        # Process each notification
        body = next((item for item in reversed(notification) if item), None)
        if not body:
            return  
        if "code" in body.lower():
            matches = re.findall(r'\b\d{1,4}-?\d{1,5}\b', body)
            for match in matches:
                print(f"CODE FOUND: {match}")
                pyperclip.copy(match)
                print("Code copied to clipboard.")
                os.system('afplay /System/Library/Sounds/Glass.aiff')

# Existing functions outside the class
def get_notifications():
    osascript_cmd = ["osascript", "get_notification.scpt"]
    result = subprocess.run(osascript_cmd, capture_output=True, text=True, encoding='utf-8').stdout.strip()
    notifications = result.splitlines()
    split_notifications = [tuple(n.split("|||")) for n in notifications]
    return split_notifications

if __name__ == "__main__":
    app = NotificationWatcherApp()
    app.run()