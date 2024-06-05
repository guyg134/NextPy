notes = {
    "La": [ 55, 110, 220, 440, 880 ],
    "Si": [ 61, 123, 246, 493, 987 ],
    "Do": [ 65, 131, 262, 523, 1046 ],
    "Re": [ 73, 147, 294, 587, 1175 ],
    "Mi": [ 82, 165, 330, 659, 1319 ],
    "Fa": [ 87, 175, 349, 698, 1397 ],
    "Sol": [ 98, 196, 392, 784, 1568 ]
}

class MusicNotes:
    def __init__(self):
        self.note_order = list(notes.keys())
        self.note_index = 0
        self.octave_index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        # check if we have reached the end of the octave
        if self.octave_index >= len(self.note_order):
            raise StopIteration
        
        current_note = self.note_order[self.note_index]
        current_octave = notes[current_note][self.octave_index]

        # increment note index
        self.note_index += 1 

        # check if we have reached the end of the notes
        if self.note_index >= len(self.note_order):
            self.note_index = 0
            self.octave_index += 1
        
        if self.octave_index >= len(notes[current_note]):
            raise StopIteration

        return current_octave
    
def main():
    notes_iter = iter(MusicNotes())

    for freq in notes_iter:
        print(freq)


if __name__ == "__main__":
    main()