import mido

from melody_helpers import Melody, keys



def read_midi_file(filename, verbose=False):
    mid = mido.MidiFile(filename)


    if verbose:
        print(f"Midi file with {len(mid.tracks)} tracks.")
    for i, track in enumerate(mid.tracks):
        if 'Track' in track.name:

            notes = []
            durations = []
            
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
    return Melody(key=key, notes=notes, durations=durations)


if __name__=="__main__":
    melody = read_midi_file('../res/Free-trial-Moje-prve-222-pjesme-17-pdf.mid')
    print(melody)