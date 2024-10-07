import time
from game_utils import enter_room, solve_riddle, end_game

# Definieren der Funktion zum Begrüßen/Erklären der Spielregeln
def greeting():
    print("Hello, new Player! This is a text-based adventure.")
    time.sleep(2)
    print("\nJust read what's written on the screen and solve the riddles you will encounter.")

# Definieren der Main-Funktion
def main ():
    greeting()
    time.sleep(3)
    rooms = [
        {
            'name':"Entrance Hall",
            'description':"You`re standing inside a dark Hall. You can see a dim torch close to a trapdoor on the bottom of the floor in front of you.",
            'riddle':{
                'question':"Would you like to open the trapdoor and climb down the ladder?",
                'answer':"yes"
            },
            'response':"Half way down the ladder you hear the noise of wood that's cracking and suddenly you fall down into the dark"
        },
        {
            'name':"Basement",
            'description':"Looks like you fell into a casual cellar, suddenly you hear a Voice whispering to you:",
            'riddle':{
                'question':"What has roots as nobody sees, is taller than trees, up, up, up it goes, and yet, never grows?",
                'answer':"mountain"
            },
            'response':"xx"
        },
        {
            'name':"Cellar",
            'description':"aa",
            'riddle':{
                'question':"aa?",
                'answer':"aa"
            },
            'response':"xx"
        },
        {
            'name':"Cave",
            'description':"bb",
            'riddle':{
                'question':"bb?",
                'answer':"bb"
            },
            'response':"xx"
        }
    ]
    current_room = 0
    while current_room < len(rooms):
        room = rooms[current_room]
        enter_room(room)
        time.sleep(6)
        solve_riddle(room)
        time.sleep(4)
        current_room += 1
    end_game()


main()