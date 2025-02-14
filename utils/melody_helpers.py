import numpy as np
from scipy.io.wavfile import write
import csv
import argparse

# Constants for generating the tones
SAMPLE_RATE = 44100  # samples per second (standard for CD quality)
DURATION = 0.5  # duration of each note in seconds

def piano_key_to_frequency(key_number):
    """
    Convert a piano key number (1-88) to the corresponding frequency (Hz).
    1 corresponds to the first key (A0) and 88 to the last key (C8).

    :param key_number: int, the number of the piano key (1 to 88)
    :return: float, the frequency of the note in Hz
    """
    # Middle A (A4) is the 49th key and has a frequency of 440 Hz
    # The formula is f(n) = 440 * 2^((n - 49) / 12), where n is the key number
    # TODO key_number is sometimes float, should be fine, but in theory is supposed to be int
    if 1 <= key_number <= 88:
        return 440 * 2 ** ((key_number - 49) / 12)
    else:
        raise ValueError("Key number must be between 1 and 88.")

# Define a function to generate a sine wave for a note
def generate_sine_wave(frequency, duration, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Sine wave at the given frequency
    return wave

# Read melody from a .csv file
def read_melody_from_csv(input_file):
    with open('melody.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)

def generate_maj_scale(key):
    major_scale_offsets = np.array([0, 2, 4, 5, 7, 9, 11, 12])

    maj = key*np.ones(8)
    melody = maj + major_scale_offsets
    return melody

def generate_min_scale(key):
    minor_scale_offsets = np.array([0, 2, 3, 5, 7, 8, 10, 12])

    min = key*np.ones(8)
    melody = min + minor_scale_offsets
    return melody


def generate_min_harmonic_scale(key):
    minor_harmonic_scale_offsets = np.array([0, 2, 3, 5, 7, 8, 11, 12])

    min = key*np.ones(8)
    melody = min + minor_harmonic_scale_offsets 
    return melody


def generate_min_melodic_scale(key):
    minor_melodic_scale_offsets = np.array([0, 2, 3, 5, 7, 8, 10, 12])

    min = key*np.ones(8)
    melody = min + minor_melodic_scale_offsets 
    return melody


def generate_pentatonic_scale(key):
    pentatonic_scale_offsets = np.array([0, 3, 5, 7, 10, 12])

    min = key*np.ones(6)
    melody = min + pentatonic_scale_offsets 
    return melody

def generate_random_pentatonic_melody(key, length=8):
    pentatonic_scale_offsets = np.array([0, 3, 5, 7, 10, 12])

    min = key*np.ones(length)
    melody = min + [pentatonic_scale_offsets[i] for i in np.random.randint(0,high=5, size=length)]
    return melody



def write_melody_to_wav(melody, output_file):
    # Create a numpy array to hold the full audio data
    full_audio = np.array([])

    # Generate each note and append it to the full audio
    for note in melody:
        wave = generate_sine_wave(piano_key_to_frequency(note), DURATION)
        full_audio = np.concatenate((full_audio, wave))

    # Convert the numpy array to 16-bit PCM (pydub requires this format)
    full_audio = np.int16(full_audio * 32767)  # Scale to 16-bit PCM range

    # Write to a .wav file using scipy's write function
    write(output_file, SAMPLE_RATE, full_audio)

    print(f"Melody saved to {output_file}")



def main():
    # Parsing command line arguments:
    # TODO make a list defining all arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", help="name of the output file to write the melody in")
    args = parser.parse_args()
    output_file = args.output_file

    # Define the melody (a list of frequencies)
    # melody = [i for i in range(40,50)]
    major_scale_offsets = np.array([0, 2, 4, 5, 7, 9, 11, 12])

    c_maj = 40*np.ones(8)
    melody = c_maj + major_scale_offsets
    write_melody_to_wav(melody=melody, output_file=output_file)
    
if __name__=="__main__":
    generate_random_pentatonic_melody(1)
    # main()