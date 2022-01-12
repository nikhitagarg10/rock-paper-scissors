
def again():
    print("to play again type yes")
    print("to exit type no")
    
    ans = input(": ")
    ans = ans.lower()
    
    if (ans == "yes"):
        return True
    elif(ans == "no"):
        return False
    
#..............................................................................

def check(user_lives, com_lives, user_score, com_score, draw):
    
    if (user_lives != 0 and com_lives != 0):
        return True
    
    print("\n")
    flag = True
    if (user_lives == 0):
        flag = False
    
    if (flag):
        print("YOU WIN")
    else:
        print("you ran out of lives, you lost")
        
    print("your score: ", user_score)
    print("COM score: ", com_score)
    print("total draws: ",draw)
    print("thank you for playing")  
    
#..............................................................................

def status(user_lives, com_lives, user_score, com_score, draw):
    print("your score: ", user_score)
    print("COM score: ", com_score)
    print("total draws: ",draw)
    print("Number of your lives left: ", user_lives)
    print("Number of COM lives left: ", com_lives)
    
#..............................................................................

def Exit(user_score, com_score, draw):
    print("your score: ", user_score)
    print("COM score: ", com_score)
    print("total draws: ",draw)
    print("thank you for playing")

#..............................................................................

def Input():
    user = input("choose rock paper or scissors: ")
    user = user.lower()
    return user

#..............................................................................

def rules():
    print("user and COM starts with 3 lives.") 
    print("If you want to check the score type \"status\"")
    print("If you want to exit type \"exit\"")

#..............................................................................