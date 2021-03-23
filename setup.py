from setuptools import setup

APP = [gui_suchmaschine.py]
DATA_FILES = [bavaria.xlsx, beijing.xlsx, california.xlsx, catalonia.xlsx, estonia.xlsx, lower_saxony.xlsx, scotland.xlsx, sweden.xlsx]
OPTIONS = {
    'argv_emulation': True,
    'packages': ['certifi'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app'],
)   
