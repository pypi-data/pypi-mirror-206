from setuptools import setup, find_packages

setup(
    name='khruang-lyrics-load-bar',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'khruang-lyrics-load-bar = khruang_lyrics_load_bar.main:main'
        ]
    }
)
