#Midterm
import random



#MENU STRING
def main():
    USD=200


    while True:
        def readysetgo():
            horses = [1, 2, 3, 4]
            betlist = random.sample(horses, len(horses))
            return betlist

        horsewinners = readysetgo()
        print(f"The winning list is {horsewinners}")

        # BET FUNCTIONS
        def exacta(picks, results=horsewinners):
            if picks == horsewinners[:2]:
                return True
            else:
                return False

        def exactabox(picks, result=horsewinners):
            if sorted(picks) == sorted(horsewinners[:2]):
                print(True)
                return True
            else:
                print(False)
                return False

        def trifecta(picks, result=horsewinners):
            if picks == horsewinners[:3]:
                print(True)
                return True
            else:
                print(False)
                return False

        def trifectabox(picks, result=horsewinners):
            if sorted(picks) == sorted(horsewinners[:3]):
                print(True)
                return True
            else:
                print(False)
                return False

        print("Welcome to The Horse Race Betting Program! Choose your bet!")
        print("1. Exacta        Cost:$15  Win:$150")
        print("2. Exacta Box    Cost:$10  Win:100")
        print("3. Trifecta      Cost:$20  Win:$250")
        print("4. Trifecta Box  Cost:$18  Win:$180")
        print(f"Balance:{USD}")
        print("5. Exit")

        choice = int(input("Please enter your choice[1-5] : "))
        if choice==1:
            USD-=15
            print("Please chose the exact order the first two winning horses are:",end="")
            pick=input().split()
            p1=int(pick[0])
            p2=int(pick[1])
            picks=[p1,p2]

            if exacta(picks)==True:
                USD+=150
                print("Congrats! You won the bet!")
            elif exacta(picks)==False:
                print("Sorry, You lost the bet...")

        elif choice==2:
            USD-=10
            print("Please choose who you think the top two winning horses are:", end="")
            pick = input().split()
            p1 = int(pick[0])
            p2 = int(pick[1])
            picks = [p1, p2]
            if exactabox(picks)==True:
                USD+=100
                print("Congrats! You won the bet!")
            elif exactabox(picks)==False:
                print("Sorry, you lost the bet...")

        elif choice==3:
            USD-=20
            print("Please chose the exact order the first three winning horses are:", end="")
            pick = input().split()
            p1 = int(pick[0])
            p2 = int(pick[1])
            p3= int(pick[2])
            picks = [p1, p2,p3]
            if trifecta(picks)==True:
                USD+=250
                print("Congrats! You won the bet!")
            elif trifecta(picks)==False:
                print("Sorry, you lost the bet...")

        elif choice==4:
            USD-=18
            print("Please choose who you think the top three winning horses are:", end="")
            pick = input().split()
            p1 = int(pick[0])
            p2 = int(pick[1])
            p3= int(pick[2])
            picks = [p1, p2,p3]
            if trifectabox(picks)==True:
                USD+=180
                print("Congrats! You won the bet!")
            elif trifecta(picks)==False:
                print("Sorry, you lost the bet...")

        elif choice==5:
            #tally goes here!
            break

main()