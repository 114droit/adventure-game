import time
# Definieren der Funktion zum Beschreiben des aktuellen Raumes/
def enter_room(room):
    print(f"\n----------{room['name']}----------")
    time.sleep(2)
    print(f"\n{room['description']}")


# Definieren der Funktion zum Präsentieren der Rätsel/Überprüfen der Antworten
def solve_riddle(room):
    while True:
        answer = input(print(f"\n{room['riddle']['question']}"))
        if not answer.strip().lower() == room['riddle']['answer']:
            print("\nWrong! Try again.")
            time.sleep(1)
        else:
            print("\nCorrect answer")
            time.sleep(1)
            print(f"\n{room['response']}")
            break

# Definieren einer Funktion zum Beenden des Spiels
def end_game():
    print("\nQuitting game... See you soon!")
    exit()