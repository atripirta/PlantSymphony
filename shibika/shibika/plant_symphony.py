import serial
import numpy as np
import time
import matplotlib.pyplot as plt
import rtmidi
import threading
import serial
from IPython.display import display, Javascript


class MidiPlayer(threading.Thread):
    def __init__(self, note_velocities, duration, port_number, is_minor):
        super().__init__()
        self.note_velocities = note_velocities
        self.duration = duration
        self.port_number = port_number
        self.is_minor = is_minor

    def run(self):
        # Define MIDI notes for C major scale
        C_MAJOR_SCALE = [60-12, 62-12, 64-12, 65-12, 67-12, 69-12, 71-12, 72-12]

        # Define MIDI notes for C minor scale
        C_MINOR_SCALE = [60+24, 62+24, 63+24, 65+24, 67+24, 68+24, 70+24, 72+24]
        
        # Choose the scale
        scale = C_MINOR_SCALE if self.is_minor else C_MAJOR_SCALE

        # Create a MIDI output port
        midi_out = rtmidi.MidiOut()
        midi_out.open_port(self.port_number)  # Adjust the port number as needed

        try:
            # Send note-on messages with delay
            for note, velocity in self.note_velocities:
                note_on = [0x90, scale[note % len(scale)], velocity]
                midi_out.send_message(note_on)

                # Introduce delay based on duration
                time.sleep(self.duration)

                # Send note-off messages
                note_off = [0x80, scale[note % len(scale)], 0]
                midi_out.send_message(note_off)
                
        finally:
            # Close the MIDI output port
            del midi_out

def send_midi_notes(note_velocities, duration=1, port_number=1, is_minor=False):
    """
    Send MIDI note-on messages followed by note-off messages after a specified duration.

    Parameters:
        note_velocities (list of tuples): List of tuples containing (note_number, velocity) pairs.
        duration (float): Duration in seconds to hold the notes before sending the note-off messages.
        port_number (int): Index of the MIDI output port to use.
        is_minor (bool): Flag indicating whether to use the C minor scale.
    """
    player = MidiPlayer(note_velocities, duration, port_number, is_minor)
    player.start()

# Establish serial connection with Arduino
ser = serial.Serial('/dev/cu.usbmodem141101', 9600)  # Change 'COM3' to the appropriate port

# Initialize empty lists for data
x_data = []
y_data = []

i = 0
try:
    while True:
        data = ser.readline().decode().strip()
        if data:
            # Convert data to integer
            value = int(data)
            # Append data to lists
            x_data.append(i)
            y_data.append(value)
            i += 1
            # Sound generation
            # Signal check
            is_major = value == 0  # Assuming value 0 indicates major, otherwise minor
            
            print("Major" if is_major else "Minor")
            
            tempo_range = (1, 3) if is_major else (4, 6)  # Adjust tempo based on scale
            
            # Generate random notes within the range of C major or C minor scale
            notes = [(np.random.randint(0, 8), np.random.randint(40, 90))]
            duration = np.random.randint(*tempo_range)  # Adjust duration based on tempo
            if is_major:
                if i%2==0:
                    send_midi_notes(notes, duration=duration, is_minor=not is_major)
            else:
                send_midi_notes(notes, duration=duration, is_minor=not is_major)

            # If it's a major key, introduce a one-note silence
#             if is_major:
#                 time.sleep(duration)

except KeyboardInterrupt:
    # Close serial connection
    ser.close()
