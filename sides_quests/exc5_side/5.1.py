import winsound

freqs = {"la": 220,
        "si": 247,
        "do": 261,
        "re": 293,
        "mi": 329,
        "fa": 349,
        "sol": 392,
        }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,\
        250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

    
def main():
    split_notes = notes.split("-")
    # check if the split_notes is a list
    print(type(split_notes)) 
    print('*'*20)
    # __iter__ is in the list
    print(dir(split_notes)) 

    # iterate over the split_notes
    for note in split_notes:
        # split the note and duration
        note, duration = note.split(",")
        # get the frequency of the note
        frequency = freqs[note]
        # convert the duration to int
        duration = int(duration)
        # play the note (yonatan hakatan)
        winsound.Beep(frequency, duration)


if __name__ == "__main__":
    main()