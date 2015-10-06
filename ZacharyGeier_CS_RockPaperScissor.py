import random

choice = eval(input("rock (0), paper(1), scissor(2): "))

rand = random.randint(0,2);

if rand == 0 and choice == 0:
    print("The computer is rock. You are rock too. It is a draw.")
elif rand == 1 and choice == 1:
    print("The computer is paper. You are paper too. It is a draw.")
elif rand == 2 and choice == 2:
    print("The computer is scissor. You are scissor too. It is a draw.")

elif rand == 0 and choice == 2:
    print("The computer is rock. You are scissor. You lose.")
elif rand == 1 and choice == 0:
    print("The computer is paper. You are rock. You lose.")
elif rand == 2 and choice == 1:
    print("The computer is scissor. You are paper. You lose.")


elif rand == 2 and choice == 0:
    print("The computer is scissor. You are rock. You won.")  
elif rand == 0 and choice == 1:
    print("The computer is rock. You are paper. You won.")
elif rand == 1 and choice == 2:
    print("The computer is paper. You are scissor. You won.")



