print("Hello there! Welcome to my game")
name = input("What is your name? ")
age = input("How old are you? ")
## print("type of age: ", type(age))
if age >= "18":
    print("Hello", name, "you are", age, "years old. You are old enough to play")
    want_to_play = input("Would you like to proceed? (yes/no) ").lower().strip()
    if want_to_play == "yes":
        lives = 20
        print("You are starting the game with", lives, "lives")
        first_question = input("You wake up to find an intruder in your house. Do you hide or attack? (hide/attack) ").lower().strip()
        if first_question == "hide":
            print("Good Choice. You better find a good spot")
            need_help = input("You need to call for help. Who do you call?(police/neighbour) ").lower().strip()
            if need_help == "police":
                print("You've called the police and they are 10 minutes away. Hang in there")
                hiding_place = input("You need a better hiding spot as you wait for the police. Where do you hide? (wardrobe/door) ").lower().strip()
                if hiding_place == "wardrobe":
                    print("Good choice. The intruder will never guess")
                    insects = input("While hiding, you see a spider. How do you respond? (scream/freeze) ").lower().strip()
                    if insects == "freeze":
                        print("Good! This is scary but you need to stay calm")
                        police_arrival = input("You can hear the siren. What do you do? (stay/run) ").lower().strip()
                        if police_arrival == "stay":
                            print("Good Job! The police break into the house and arrest the intruder. You are now safe.")
                            print("Congratulations! You still have", lives, "lives")
                        else:
                            print("The intruder grabs you and holds you hostage. You lose 20 lives.")
                            if lives == 0:
                                print("You've lost the game. Try again next time")
                    else:
                        print("Damn it", name, "you literally alarmed the intruder. You lose 20 lives " )
                        lives -= 20
                        if lives == 0:
                            print("You've lost the game. Try again next time")
                else:
                    print("The intruder sees you the minute he walks in and attacks you. You lose 20 lives")
                    lives -= 20
                    if lives == 0:
                        print("You've lost the game. Try again next time")
            else:
                print("You call your neighbour but the call goes to voicemail. You lose 20 lives")
                lives -= 20
                if lives == 0:
                    print("You've lost the game. Try again next time")
        else:
            print("Not very smart", name, "the intruder is much bigger and stronger than you. You lose 20 lives")
            lives -= 20
            if lives == 0:
                print("You've lost the game. Try again next time")
    else:
        print("Too bad! Maybe next time")
else:
    print("Sorry", name, "you are a little too young to play")