import random
import datetime as dt
import json


ready=True
while ready:
    print("="*30,"Stone-Paper-Scissor","="*30)
    while True:
        name=input("Enter your name :").capitalize()
        if len(name)>=3 and name.isalpha():
            break
        else:
            print("In-valid name..!")
    chance=["Stone","Paper","Scissor"]

    try:
        with open("user_list.json","r") as file:
            user_list=json.load(file)
    except FileNotFoundError :
            user_list = []
            with open("user_list.json", "w") as file:
                json.dump(user_list, file, indent=4)

    c_win=0
    u_win=0
    winner=""
    i=0
    while i<5:
    # for i in range(5):
        print("""
                1.Stone🪨
                2.Paper🗞️
                3.Scissor✂️
                    """)
        i+=1
        computer=random.choice(chance)
        ch=0
        while ch<3:
            try:
                user=int(input("\nenter the choice 🚀 :"))
                if user in[1,2,3]:
                    break
                ch+=1
                print("In-valid input..!")
                if ch<3:
                    print(f"Your have last {3-ch} chance ")
                elif ch==3:
                    print(" Beter luck next time 🙌\n")
            except ValueError :
                print ("Enter the correct value :")
            except Exception as err:
                print(err)

        if user==1: user="Stone"
        elif user==2: user="Paper"
        elif user==3: user="Scissor"
        else :exit()

        print("computer choice =",computer)
        print("user choice =",user)

        if user==computer:
            print("match draw..")
            i=i-1
            
        elif (computer =="Stone" and user=="Scissor")or\
            (computer =="Paper" and user=="Stone")or\
            (computer =="Scissor" and user=="Paper"):

            print("computer win..!")
            c_win+=1
        else:
            print("user win..!")
            u_win+=1

    print("-"*60)

    print(f"{name} =",u_win)
    print("Computer =",c_win)

    if u_win>=3:
        winner=f"{name}"
        print(f"So,the winer is {name} 🎉🙌")
    elif c_win>=3:
        winner="Computer"
        print("So,the winer is computer 🎉🙌")
    else:
        print("match draw 👍..!")

    play_time=(dt.datetime.now().strftime("%I:%M:%S %p"))
    play_date=(dt.datetime.now().strftime("%d-%m-%Y"))

    user_list.append({"Name":name,
                    "Time":play_time,
                    "Date":play_date,
                    "computer":c_win,
                    f"{name}":u_win,
                    "Winner":winner
                    })

    with open ("user_list.json","w") as file:
        json.dump(user_list,file,indent=4)

    enter=True
    while enter:
        check=input("do you want to continue..?(yes/no)  ").lower()
        if check=="no":
            ready=False
            enter=False
            print("Thank you..! ")
                              
        elif check=="yes":
            enter=False
        else:
            print("Enter valid input..!")



"""
=>ithula user wrng a input kudutha 3 times la exit agidum.
=>match draw achina +1 times loop agum for every draw match.
=>for loop use panuna draw match ku extra loop agathu, so i am use while loop.
=>ithula data va store panuvom like user name,winner,score,playing time.
"""