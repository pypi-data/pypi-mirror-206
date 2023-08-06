# This file is imported from __init__.py and exec'd from setup.py

MAJOR = 2
MINOR = 2
MICRO = 0
RELEASE = False

__version__ = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

if not RELEASE:
    # if it's a rcx release, it's not proceeded by a period. If it is a
    # devx release, it must start with a period
    __version__ += 'rc1'


_kivy_git_hash = '22fd80d79f9ca66324018430e54232a4bf6cdbd4'
_kivy_build_date = '20230504'
