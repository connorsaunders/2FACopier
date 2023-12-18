from setuptools import setup

APP = ['main.py']
DATA_FILES = [('resources', ['get_notification.scpt'])] 
OPTIONS = {
    'argv_emulation': False,
    'packages': ['rumps', 'pyperclip'],
    'resources': ['get_notification.scpt'],  
    'plist': {
        'CFBundleName': 'test',
        'CFBundleDisplayName': 'test',
        'CFBundleIdentifier': 'com.yourdomain.test',  
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0'
    }
}

setup(
    app=APP,
    name='test',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
