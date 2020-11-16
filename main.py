import random 
name = input(" enter your name: ")
print("good luck "  + name +  "!" )

file = open("name.txt")
name = file.readlines()
name = random.choice(name)
name = name.lower()
name = str(name).strip('\n')
name = str(name).strip('\r')
print("guess the characters:")
guesses = str()
if ' ' in name:
    guesses += ' '
turns = 6
while turns > 0:
    failed = 0
    for char in name:
        if char in guesses:
            print(char, end=' ')
        else:    
            print('_', end= ' ')
            failed += 1
    if failed == 0:
        print("\nyou win!")
        exit()
    guess = input("\n\n guess a character: ")
    guesses += guess 
    if guess not in name:
        turns -= 1
        print("wrong")
        print("you have " + str(turns) + " more guesses")
    if turns == 0:
        print("you lose")
        print("the movie was: ", name)
        
