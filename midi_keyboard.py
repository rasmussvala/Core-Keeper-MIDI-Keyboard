import mido
from pynput.keyboard import Controller

# Create a Keyboard controller
keyboard = Controller()

# Create a dictionary to map MIDI notes to keyboard keys
midi_to_key = {
    48: "z",  # C3
    49: "s",  # C#3/D♭3
    50: "x",  # D3
    51: "d",  # D#3/E♭3
    52: "c",  # E3
    53: "v",  # F3
    54: "g",  # F#3/G♭3
    55: "b",  # G3
    56: "h",  # G#3/A♭3
    57: "n",  # A3
    58: "j",  # A#3/B♭3
    59: "m",  # B3
    60: "q",  # C4
    61: "2",  # C#4/D♭4
    62: "w",  # D4
    63: "3",  # D#4/E♭4
    64: "e",  # E4
    65: "r",  # F4
    66: "5",  # F#4/G♭4
    67: "t",  # G4
    68: "6",  # G#4/A♭4
    69: "y",  # A4
    70: "7",  # A#4/B♭4
    71: "u",  # B4
}

# Get a list of all MIDI input names
input_names = mido.get_input_names()

# Check if there are any MIDI inputs
if not input_names:
    print("No MIDI inputs found")
else:
    # Open the first MIDI input
    with mido.open_input(input_names[0]) as inport:
        for msg in inport:
            # If this is a note_on message with a velocity > 0 and the note is in our dictionary...
            if msg.type == "note_on" and msg.velocity > 0 and msg.note in midi_to_key:
                # Trigger the equivalent keyboard key press
                keyboard.press(midi_to_key[msg.note])
            # If this is a note_off message or a note_on message with a velocity of zero and the note is in our dictionary...
            elif (
                msg.type == "note_off" or (msg.type == "note_on" and msg.velocity == 0)
            ) and msg.note in midi_to_key:
                # Release the equivalent keyboard key
                keyboard.release(midi_to_key[msg.note])
