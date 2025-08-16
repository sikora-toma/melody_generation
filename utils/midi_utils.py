import mido
import torch

from utils.melody_helpers import Melody, keys



def read_midi_file(filename, return_tensor=False, verbose=False):
    mid = mido.MidiFile(filename)


    if verbose:
        print(f"Midi file with {len(mid.tracks)} tracks.")
    notes = []
    durations = []
 
    for i, track in enumerate(mid.tracks):
        # this used to work, but dalmacija dataset has weird track naming conventions
        # if 'Track' in track.name or 'Voice' in track.name:
        if len(track.name)>0:

           
            for msg in track:
                if msg.type=='note_on':
                    notes.append(msg.note)
                elif msg.type=='note_off':
                    durations.append(msg.time)
            if verbose:
                print(f"Notes: {notes}\nDurations: {durations}")
        # meta messages
        else:
            for msg in track:
                if msg.type=='key_signature':
                    key = keys[msg.key]
                    if verbose:
                        print(f"Key: {key}")
 
    if return_tensor:
        return torch.tensor([notes, durations], dtype=torch.float16)
   
    return Melody(key=key, notes=notes, durations=durations)


if __name__=="__main__":
    melody = read_midi_file('../res/zvira voda.mid')
    print(melody)