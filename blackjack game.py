import random
def calsum(user,comp):
    a=sum(user)
    b=sum(comp)
    if a==21 or a-10==21:
        return 1  #win
    elif b==21 or b-10==21:
        return 0   #lose
    else:
        if a>21:
            if 11 in user:
                if a-10>21:
                    return 0  #lose
                else:
                    return 2  #ask another card
            else:
                return 0
        else:
            return 2  #ask another card

nums=[11,2,3,4,5,6,7,8,9,10,10,10,10]
while True:
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)
    print("Welcome to blackjack game!!!")
    print("Here are your initial cards")
    user=list(random.choices(nums,k=2))
    comp=list(random.choices(nums,k=2))
    print("Your deck: ",user)
    print("Computer's deck: [",comp[0],' , --- ]')
    choice=calsum(user,comp)
    c=""
    while True:
        if choice==1:
            print()
            print("Congratulations, You won the game!!!")
            print("You have a blackjack!!!")
            print()
            print("Your final deck:", user)
            print("Your final score:",sum(user))
            print()
            print("Computer's final deck:",comp)
            print("Computer's final score:",sum(comp))
            c="finish"
            break
        elif choice==0:
            print()
            print("You lost the game!!!")
            print("You scored above 21")
            print()
            print("Your final deck:", user)
            print("Your final score:",sum(user))
            print()
            print("Computer's final deck:",comp)
            print("Computer's final score:",sum(comp))
            c="finish"
            break
        else:
            chs=input("Do you want to choose another card?? (Y/N) :")
            if chs in ["Y","y"]:
                user.append(int(random.choice(nums)))
                print("Your new deck: ",user)
                choice=calsum(user,comp)
            else:
                c="on"
                break
    if c=="on":
        print("Your current deck: ",user)
        compchs=["y","n"]
        choice=calsum(comp,user)
        while True:
            if choice==0:
                print()
                print("Congratulations, You won the game!!!")
                print("The computer scored more than 21")
                print()
                print("Your final deck:", user)
                print("Your final score:",sum(user))
                print()
                print("Computer's final deck:",comp)
                print("Computer's final score:",sum(comp))
                c="finish"
                break
            elif choice==1:
                print()
                print("You lost the game!!!")
                print("The computer have a blackjack")
                print()
                print("Your final deck:", user)
                print("Your final score:",sum(user))
                print()
                print("Computer's final deck:",comp)
                print("Computer's final score:",sum(comp))
                c="finish"
                break
            else:
                if sum(comp)<17:
                    comp.append(int(random.choice(nums)))
                    choice=calsum(comp,user)
                else:
                    chs=random.choices(compchs,weights=[1,4])
                    if chs=="y":
                        comp.append(int((random.choice(nums))))
                        choice=calsum(comp,user)
                    else:
                        c="on"
                        break
    if c=="on":
        if sum(user)==sum(comp):
            print()
            print("Draw")
            print("Your final deck:", user)
            print("Your final score:",sum(user))
            print()
            print("Computer's final deck:",comp)
            print("Computer's final score:",sum(comp))
        elif sum(user)>sum(comp):
            print()
            print("Congratulations, You won the game!!!")
            print("You scored more than the computer!!!")
            print()
            print("Your final deck:", user)
            print("Your final score:",sum(user))
            print()
            print("Computer's final deck:",comp)
            print("Computer's final score:",sum(comp))
        else:
            print()
            print("You lost the game!!!")
            print("You scored less than the computer!!!")
            print()
            print("Your final deck:", user)
            print("Your final score:",sum(user))
            print()
            print("Computer's final deck:",comp)
            print("Computer's final score:",sum(comp))
    print()
    plag=input("Do you want to play the game again?? (y/n): ")
    if plag in ["y","Y"]:
        continue
    else:
        print("Thank you for playing!!!")
        break











