from setuptools import setup

APP = ['main.py']
DATA_FILES = [('resources', ['get_notification.scpt'])] 
OPTIONS = {
    'argv_emulation': False,
    'packages': ['rumps', 'pyperclip'],
    'resources': ['get_notification.scpt'],  
    'plist': {
        'CFBundleName': 'TwoFACopy',
        'CFBundleDisplayName': 'TwoFACopy',
        'CFBundleIdentifier': 'com.yourdomain.TwoFACopy',  
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0'
    }
}

setup(
    app=APP,
    name='TwoFACopy',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
