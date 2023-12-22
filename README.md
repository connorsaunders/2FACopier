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
Either use the app inside the dist folder (currently named testrun1) or build your own app by running the setup.py file with py2app 

## How It Works
- The app uses AppleScript (`get_notification.scpt`) to access and read notifications from the Notification Center.
- Notifications are parsed for 2FA codes using regular expressions.
- Detected codes are copied to the clipboard and a sound is played to alert the user.

## Limitations
- Works only on macOS due to the use of AppleScript and macOS-specific system calls.
- Requires the notifications to be in a specific format to correctly extract 2FA codes.

## Contributing
Contributions to improve the app or extend its functionality are welcome. Please ensure to follow good coding practices and provide documentation for your changes.
