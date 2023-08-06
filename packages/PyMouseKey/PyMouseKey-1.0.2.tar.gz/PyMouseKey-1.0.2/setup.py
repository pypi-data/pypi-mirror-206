import setuptools

VERSION = '1.0.2'
DESCRIPTION = 'A python package for sending keyboard and mouse inputs'
LONG_DESCRIPTION = 'pymousekey is made for sending keyboard and mouse inputs simular to how pyautogui does but using the ctypes module only\nKeep in mid their is no failsafe wrapper for any function so use with caution\nNo extra dependencies are needed to use this module'


setuptools.setup(
    name="PyMouseKey",
    version=VERSION,
    author="Chasss",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
)
