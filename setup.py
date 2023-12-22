from setuptools import setup

APP = ['main.py']
DATA_FILES = [('resources', ['get_notification.scpt'])] 
OPTIONS = {
    'argv_emulation': False,
    'iconfile':'2fac.png',
    'packages': ['rumps', 'pyperclip'],
    'resources': ['get_notification.scpt'],  
    'plist': {
        'CFBundleName': 'testrun1',
        'CFBundleDisplayName': 'testrun1',
        'CFBundleIdentifier': 'com.yourdomain.testrun1',  
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0'
    }
}

setup(
    app=APP,
    name='testrun1',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
