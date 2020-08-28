import numpy as np
import random
import os
import time
import csv

NOTES_PER_STRING = 12

NOTES_ARR = np.array(
    [
        "A",
        "A#",
        "B",
        "C",
        "C#",
        "D",
        "D#",
        "E",
        "F",
        "F#",
        "G",
        "G#"]
    )

TUNING = np.array(
    [
        "E",
        "A",
        "D",
        "G",
        "B",
        "E"
    ]
)

def readCSV():
    with open('highscore.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

def writeCSV(record):
    with open('highscore.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(record)

def notes_on_x_string(start_note, note_wanted):
    start_point = np.where(NOTES_ARR == start_note)

    string_beggining = NOTES_ARR[int(start_point[0]):12]
    string_ending = NOTES_ARR[0:int(start_point[0])]     

    string_notes = np.concatenate([string_beggining, string_ending])

    fret = 0
    note = 0
    fret_desired_note = np.array([])
    while fret < NOTES_PER_STRING:
        if note_wanted == string_notes[note]:
            fret_desired_note = np.append(fret_desired_note, int(fret))
        
        fret += 1
        note += 1
        if note > 11:
            note = 0
    return fret_desired_note


def notes_position(desired_note):
    
    aux = 0
    time_start = time.perf_counter()
    input("You will be finding all the " + desired_note + "'s in your fretboard, ready? \nPress Enter!!")
    os.system("clear")
    for x in TUNING:
        notes_position_array = np.array([])
        notes_position_array = np.append(notes_position_array, [[notes_on_x_string(x, desired_note)]])
        print(desired_note + "'s at " + TUNING[aux] + " string:")
        
        for y in notes_position_array:
            answer = -1
            # print("\t fret {}".format(int(y)))
            while answer == -1:
                answer = input("Insert fret: ")
                if int(answer) == int(y):
                    answer = 0
                else:
                    answer = -1
            
            os.system("clear")
        aux+=1
    time_end = time.perf_counter()
    time_total = time_end - time_start

    record_keeper = readCSV()
    auxX = 0
    while auxX < 13:
        if record_keeper[auxX][0] == desired_note:
            if float(record_keeper[auxX][1])>float(time_total) or record_keeper[auxX][1] == '0':
                print("NEW HIGHSCORE IN THE NOTE: " + desired_note)
                record_keeper[auxX][1] = round(time_total, 2)
                writeCSV(record_keeper)
        auxX += 1    

    print("It took you " + str(round(time_total, 2)) + " seconds!")
    input("Press Enter!")
    
def main():
    os.system("clear")
    opc = ''
    while opc != str(0):
        opc = input("Welcome \n1- Random note\n2- Choose a note\n\n0- Exit\n")
        if opc == str(1):
            notes_position(np.random.choice(NOTES_ARR))
        if opc == str(2):
            notes_position(input("Choose the note:\n")) 

main()