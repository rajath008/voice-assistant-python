from Main import speak,takeCommand
import random
def gameplay():
    speak("Let's play rock paper scissor ")
    i=0
    pl=0
    cm=0

    while(i<5):
        choose = ("rock","paper","scissors") #Tuple
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- YOU :- {pl} : AI :- {cm}")
            elif (com_choose == "paper"):
                speak("paper")
                cm += 1
                print(f"Score:- YOU :- {pl} : AI :- {cm}")
            else:
                speak("Scissors")
                pl += 1
                print(f"Score:- YOU:- {pl} : AI :- {cm}")

        elif (query == "paper" ):
            if (com_choose == "rock"):
                speak("ROCK")
                pl += 1
                print(f"Score:- YOU :- {pl+1} : AI :- {cm}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- YOU :- {pl} : AI :- {cm}")
            else:
                speak("Scissors")
                cm += 1
                print(f"Score:- YOU :- {pl} : AI :- {cm}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                cm += 1
                print(f"Score:- YOU :- {pl} : AI :- {cm}")
            elif (com_choose == "paper"):
                speak("paper")
                pl += 1
                print(f"Score:- YOU :- {pl} : AI :- {cm}")
            else:
                speak("Scissors")
                print(f"Score:- YOU :- {pl} : AI :- {cm}")
        i += 1

    print(f"FINAL SCORE :- YOU :- {pl} : AI :- {cm}")
gameplay()
