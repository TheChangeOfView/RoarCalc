from distutils.core import setup
import py2exe

setup(
    windows = [
        {
            "script": "RoarCalc.py",
            "icon_resources" : [(1, "files\img\ico_logo.ico")]
        }
    ]
)