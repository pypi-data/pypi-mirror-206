from setuptools import setup, find_packages

setup(
    name="MotionSense",
    version="0.1.0",
    description='A Python library for Motion Detection',
    author='Lyova',
    author_email='lev.avyan17@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
    ],
)