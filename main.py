import time

from game_utils import enter_room, solve_riddle, end_game

# Definieren der Funktion zum Begrüßen/Erklären der Spielregeln
def greeting():
    print("Hello, new Player! This is a text-based adventure game.")
    time.sleep(2)
    print("\nJust read what's written on the screen and solve the riddles you will encounter!")

# Definieren der Main-Funktion
def main ():
    greeting()
    time.sleep(3)
    rooms = [
        {
            'name':"Entrance Hall",
            'description':"You're standing inside a huge Hall. You can see a dim torch close to a trapdoor on the bottom of the floor in front of you.",
            'riddle':{
                'question':"Would you like to open the trapdoor and climb down the ladder?",
                'answer':"yes"
            },
            'response':"Half way down the ladder you hear the noise of wood that's cracking and suddenly you fall down into the dark..."
        },
        {
            'name':"Basement",
            'description':"Looks like you fell into the basement of a small house. While checking your bones you hear a voice whispering to you out of a sudden...",
            'riddle':{
                'question':'"What has roots as nobody sees, is taller than trees, up, up, up it goes, and yet, never grows?"',
                'answer':"mountain"
            },
            'response':"As you speak those words another trapdoor opens right beneath your feet"
        },
        {
            'name':"Cellar",
            'description':"You already assumed a cellar under that basement you fell into the first time, now you know for sure.",
            'riddle':{
                'question':'Again you hear the voice speaking: "Thirty white horses on a red hill. First they champ, then they stamp, then they stand still."',
                'answer':"teeth"
            },
            'response':"This time you're prepared! In the exact same moment you start to speak the words, you also start to jump to the side...... only to see a trapdoor opening right at the spot where you aimed to jump leading you into the dark again."
        },
        {
            'name':"Cave",
            'description':"Coming back to conciousness, you find yourself at the bottom of a cave. You can't see anything and all you can feel is the cold stone and your head hurting.",
            'riddle':{
                'question':'...and again you can hear the voice speaking to you: "It cannot be seen, cannot be felt, cannot be heard, cannot be smelt. It lies behind stars and under hills, and empty holes it fills. It comes first and follows after, ends life, kills laughter."',
                'answer':"darkness"
            },
            'response':"Congratulations! You found the treasure...or not?"
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
if __name__ == "__main__":
    main()