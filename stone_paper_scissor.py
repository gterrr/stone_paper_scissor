import random

def game(bot,you):
    if bot==you:
        return None
    elif bot=="a":
        if you=="b":
            return False
        elif you=="c":
            return True
    elif bot=="b":
        if you=="c":
            return False
        elif you=="a":
            return True
    elif bot=="c":
        if you=="a":
            return False
        elif you=="b":
            return True
print("paper(a) stone(b) or scissor(c) ?")
randno=random.randint(1,3)
if randno==1:
    bot="a"
elif randno==2:
    bot="b"
elif randno==3:
    bot="c"

you=input("your turn: paper(a) stone(b) or scissor(c)\n")
z=game(bot,you)
print(f"bot chose {bot}")
print(f"you chose {you}")

if z==None:
    print("this game is a tie!")
elif z:
    print("you win!")
else:
    print("you lose!")