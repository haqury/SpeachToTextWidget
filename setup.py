from setuptools import setup

setup(
    name='SpeachToTextWidget',
    version='1.0',
    description='A useful module',
    author='Author Name',
    author_email='haqury@gmail.com',
    packages=['SpeachToTextWidget'],  # same as name
    install_requires=['pyperclip', 'PyQt5'],  # external packages as dependencies
)