# README for NotificationWatcherApp

## Introduction
NotificationWatcherApp is a Python application designed to monitor system notifications and capture specific information, such as two-factor authentication (2FA) codes. It automatically copies these codes to the clipboard for ease of use.

## Features
- **Notification Monitoring**: Watches for new system notifications.
- **2FA Code Detection**: Identifies and extracts 2FA codes from notifications.
- **Clipboard Integration**: Automatically copies detected 2FA codes to the clipboard.
- **Audio Feedback**: Plays a sound when a code is detected and copied.
- **Start/Stop Functionality**: User can start or stop the notification monitoring at any time.

## Requirements
- Python 3
- macOS (due to usage of AppleScript and specific macOS system features)
- `pyperclip` module
- `rumps` module for macOS status bar application support

## Installation
1. Ensure Python 3 is installed on your macOS.
2. Install required Python modules:
   ```bash
   pip3 install pyperclip rumps
3. Download the `main.py` and `get_notification.scpt` files to the same directory.

## Usage
1. Run the script using Python 3:
python3 NotificationWatcherApp.py

2. Once started, the app will appear in the macOS status bar with options to start or stop the notification monitoring.
3. When a notification containing a 2FA code arrives, the app will capture and copy the code to the clipboard and play a sound notification.

## How It Works
- The app uses AppleScript (`get_notification.scpt`) to access and read notifications from the Notification Center.
- Notifications are parsed for 2FA codes using regular expressions.
- Detected codes are copied to the clipboard and a sound is played to alert the user.

## Limitations
- Works only on macOS due to the use of AppleScript and macOS-specific system calls.
- Requires the notifications to be in a specific format to correctly extract 2FA codes.

## Contributing
Contributions to improve the app or extend its functionality are welcome. Please ensure to follow good coding practices and provide documentation for your changes.
