#importing module 
from cx_Freeze import setup, Executable

setup(
      version = 1,
      description = "A Cli based Torrent Searching Script",
      executables = [Executable("torget.py",
      targetName = 'TorGet.exe',
      icon='./Assets/logo.ico')],)