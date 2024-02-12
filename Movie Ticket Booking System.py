flist=[]
def t_movie():
    list3=["Name of the Movie: Rangasthalam","Name of the Movie: Salaar","Name of the Movie: Hari Hara Veera Mallu"]
    print("which movie do you want to watch :")
    print("1:Rangasthalam")
    print("2:Salaar")
    print("3:Hari Hara Veera Mallu")
    print("4.back")
    movie = int(input("choose your movie: "))
    flist.append(list3[movie-1])
    if movie != 4:
        theater()
        return 0


def theater():
    list4=["SCREEN No: 1","SCREEN No: 2","SCREEN No: 3"]
    print("which screen do you want to watch movie: ")
    print("1.SCREEN 1")
    print("2.SCREEN 2")
    print("3.SCREEN 3")
    a = int(input("choose your screen: "))
    flist.append(list4[a-1])
    timing(a)
    

def timing(a):
    if a == 1:
        time1=["Time: 10:00am to 1:00pm","Time: 1:10pm to 4:10pm","Time: 4:20pm to 7:20pm","Time: 7:30pm to 10.30pm"]
        print("choose your movie time:")
        print("1)10:00am to 1:00pm")
        print("2)1:10pm to 4:10pm")
        print("3)4:20pm to 7:20pm")
        print("4)7:30pm to 10.30pm")
        t = int(input("select your time:"))
        x = time1[t-1]
        flist.append(x)
        print("price of each ticket is 100 rupees")
        ticket = int(input("number of ticket do you want : "))
        print("Total price is : ",ticket*100)
    elif a == 2:
        time2=["Time: 10:15am to 1:15pm","Time: 1:25pm to 4:25pm","Time: 4:35pm to 7:35pm","Time: 7:45pm to 10.45pm"]
        print("choose your movie time:")
        print("1)10:15am to 1:15pm")
        print("2)1:25pm to 4:25pm")
        print("3)4:35pm to 7:35pm")
        print("4)7:45pm to 10.45pm")
        t = int(input("select your time:"))
        x = time2[t-1]
        flist.append(x)
        print("price of each ticket is 100 rupees")
        ticket = int(input("number of ticket do you want : "))
        print("Total price is : ",ticket*100)
    elif a == 3:
        time3=["Time: 10:30am to 1:30pm","Time: 1:40pm to 4:40pm","Time: 4:50pm to 7:50pm","Time: 8:00pm to 10:45pm"]
        print("choose your movie time:")
        print("1)10:30am to 1:30pm")
        print("2)1.40:pm to 4:40pm")
        print("3)4:50pm to 7:50pm")
        print("4)8:00pm to 10:45pm")
        t = int(input("select your time:"))
        x = time3[t-1]
        flist.append(x)
        print("price of each ticket is 100 rupees")
        ticket = int(input("number of ticket do you want : "))
        print("Total price is : ",ticket*100)
    print("\n\nMovie Booking Details :")
    print("*********\n")
    for i in range(len(flist)):
        print(flist[i])
    print("\n*********\n")    
    return 0


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")


def center():
    list2=["Theatre Name: Inox","Theatre Name: Icon","Theatre Name: pvp"]
    print("which theater do you wish to see movie : ")
    print("1.Inox")
    print("2.Icon")
    print("3.pvp")
    print("4.back")
    a = int(input("choose your option: "))
    flist.append(list2[a-1])
    movie(a)
    return 0


def city():
    list1=["Location: Vijayawada","Location: Vizag","Location: Mangalgiri"]
    print("Hi welcome to movie ticket booking: ")
    print("where you want to watch movie?:")
    print("1.Vijayawada")
    print("2.Vizag")
    print("3.Mangalagiri")
    place = int(input("choose your option: "))
    flist.append(list1[place-1])
    if place == 1:
        center()
    elif place == 2:
        center()
    elif place == 3:
        center()
    else:
        print("wrong choice")

temp=1;
while(1):
    if(temp==1):
        city()
        flist.clear()
    print("Do you want to continue the process....(y/n):")
    flag=input("")
    if(flag=='n'):
        temp=0
        break
