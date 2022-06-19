






print('PIETER')

print('WELCOME USER , Please Enter Your Login Information')

print('WELCOME USER , Please Enter Your Login Information')

class Login:
    def __init__(self):
        self.data = {}
        self.username = input('Username : ')
        self.password = input('Password : ')


    def login_check(self):
        key1, value1 = self.username , self.password

        if key1 in self.data and value1 == self.data[key1]:
            print(f'\nWelcome Back {self.username}')

        else:
            print("\nWrong Username Or Password")
            ask = input("\nAre You A New User? Y/N : ")

            if ask == "y":
                self.new_user()

            if ask == 'n':
                check_username = input("\nUsername : ")
                check_password = input("Password : ")
                key, value = check_username , check_password

                if key in self.data and value == self.data[key]:
                    print(f"\nWELCOME {check_username}!!")

    def new_user(self):
        new_username = input('\nPlease Enter A New Username : ')
        new_password = input('Please Enter A New Password : ')

        self.data[new_username] = new_password

        check_username = input("\nUsername : ")
        check_password = input("Password : ")

        key , value = check_username , check_password

        if key in self.data and value == self.data[key] :
            print(f"\nWELCOME {check_username}!!")
        else:
            self.login_check()


main = Login()
main.login_check()

import time, random

continued = 'no'
print("guess thy number")
guess = input("what do you think the number is between 1-10? ")
number = random.randint(1, 10)
if guess.lower() not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    print("What part of enter a NUMBER between 1-10 do you not understand?")
    quit()
while continued == 'no':
    continue1 = input("type 1 to continue: ")
    if continue1.lower() in ["1", "1 to continue", ]:
        continued == 'yes'
        if int(guess) == number:
            print("Lucky child")
            print("You just got lucky")
            print("go win the lottery")
            quit()
        else:
            print("LOL, SO BAD.")
            print("GET GOOD")
        break
again = input("Do you want to do this again? Say yes, y or no, n: ")
while again.lower() in ['yes', 'y']:
    print("guess thy number")
    guess = input("what do you think the number is between 1-10? ")
    number = random.randint(1, 10)
    if guess.lower() not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        print("What part of enter a NUMBER between 1-10 do you not understand?")
        quit()
    while continued == 'no':
        continue1 = input("type 1 to continue: ")
        if continue1.lower() in ["1", "1 to continue", ]:
            continued == 'yes'
            if int(guess) == number:
                print("Lucky child")
                print("You just got lucky")
                print("go win the lottery")
                break
            else:
                print("LOL, SO BAD.")
                print("GET GOOD")
                break
    again = input("Do you want to do this again? Say yes, y or no, n: ")












