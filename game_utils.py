import time

# Definieren der Funktion zum Beschreiben des aktuellen Raumes/
def enter_room(room):
    print(f"\n----------{room['name']}----------")                                       # Gib leere Zeile und den in der main zugeorndeten wert vom string 'name' des aktuellen Raumes (room) aus rooms aus
    time.sleep(2)
    print(f"\n{room['description']}")                                                    # "" "" "" vom string 'description' "" "" "" 


# Definieren der Funktion zum Präsentieren der Rätsel/Überprüfen der Antworten
def solve_riddle(room):
    while True:                                                                          # während true wahr -> unendliche Schleife
        answer = input(print(f"\n{room['riddle']['question']}"))                         # definiere die var answer als input des users auf die frage aus dem Rätsel aus dem momentanen Raum
        if not answer.strip().lower() == room['riddle']['answer']:                       # wenn die antwort mit beglichenen leerstellen und auf klein gesetzten Buchstaben der antwort aus dem rätsel des aktuellen raumes nicht entspricht
            print("\nWrong! Try again.")
            time.sleep(1)
        else:                                                                            # wenn answer der antwort entspricht
            print("\nCorrect answer")
            time.sleep(1)
            print(f"\n{room['response']}")                                               # gib leere zeile und den wert des strings 'response' des aktuellen raumes aus
            break                                                                        # Beende unendliche Schleife und somit solve_riddle() funktion

# Definieren einer Funktion zum Beenden des Spiels
def end_game():
    print("\nQuitting game... See you soon!")
    exit()