# Core-Keeper-MIDI-Keyboard

MIDI Keyboard input for Core Keeper Instruments. Original script created by **Steam user Minihat**. Improvements by me.

## Run script on your machine

### Prerequisites

- Python (download here: https://www.python.org/downloads/, **note**: important to add Python to $PATH during installation, it's a checkbox option)
- pip (package installer for Python, gets installed with Python)

**Note**: No other active program can use the MIDI keyboard while running the script.

### Setup - First time

1. Open terminal
2. Clone repository `git clone https://github.com/rasmussvala/Core-Keeper-MIDI-Keyboard.git`
3. Move into directory: `cd .\Core-Keeper-MIDI-Keyboard\` 
4. Create virtual environment: `py -m venv .venv`
5. Activate virtual environment: `.\.venv\Scripts\activate`
6. Install packages: `pip install -r .\requirements.txt`
7. Run the script: `py .\midi_keyboard.py`

### Setup - All the other times

1. Open terminal
2. Move into `Core-Keeper-MIDI-Keyboard` directory
3. Activate virtual environment: `.\.venv\Scripts\activate`
4. Run the script: `py .\midi_keyboard.py`

### MIDI Demo

![MIDI Demo](demo.gif)
