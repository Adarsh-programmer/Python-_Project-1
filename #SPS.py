import random
def game():
    uscore = 0
    cscore = 0
    options = ["Stone", "Paper", "Scissors"]
    while (uscore+cscore<5):
          user = input("Stone/Paper/Scissors : ")
          comp = random.choice(options)
          print("Computer : ",comp)
          if (user.lower() == "stone" and comp=="Scissors") or (user.lower() == "paper" and comp=="Stone") or (user.lower() == "scissors" and comp=="Paper"):
             print("User gains 1 point")
             uscore = uscore+1
             print("User Score : ",uscore)
             print("Computer Score : ",cscore)
          elif (comp== "Stone" and user.lower()=="scissors") or (comp == "Paper" and user.lower()=="stone") or (comp == "Scissors" and user.lower()=="paper"):
               print("Computer gains 1 point")
               cscore = cscore+1
               print("User Score : ",uscore)
               print("Computer Score : ",cscore)
          else:
               print("***INVALID*INPUT*BY*USER***")
          print("---------------------------")
    if uscore>cscore:
       print("User Wins")
    else:
         print("Computer Wins")
game()
