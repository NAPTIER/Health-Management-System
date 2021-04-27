def getdate():
    import datetime
    return datetime.datetime.now()
date=str(getdate())
def shubham():
    print("**********@ Hello Shubham @**********")
    print("Press 1 to goto Diet Section")
    print("Press 2 to goto Execise Section")
    c=int(input("Enter a value from above options : "))
    if c>2:
        print("Please Enter an Option From above listed Choices!!!")
        shubham()
    else:
        if c==1:
            print("**********@Welcome to Diet Section@**********")
            print("Press 1 to Retrieve data ")
            print("Press 2 to log/update data")
            c1 = int(input("Enter a value from above options : "))
            if c1==1:
                with open("shubham diet.txt") as s1:
                    print(s1.read())
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm=int(input("Enter value : "))
                if mm==1:
                    main()
                else:
                    exit()
            else:
                s2=open("shubham diet.txt","a")
                data=input("Enter Food Item : ")
                s2.write(data)
                s2.write(" : ")
                s2.write(date)
                s2.write("\n")
                s2.close()
                print("Log Sucessfully Updated at {}".format(date))
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
        else:
            print("**********@Welcome to Exercise Section@**********")
            print("Press 1 to Retrieve data ")
            print("Press 2 to log/update data")
            c1 = int(input("Enter a value from above options : "))
            if c1 == 1:
                with open("shubham ex.txt") as s1:
                    print(s1.read())
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
            else:
                s2 = open("shubham ex.txt", "a")
                data = input("Enter Exercise Name : ")
                s2.write(data)
                s2.write(" : ")
                s2.write(date)
                s2.write("\n")
                s2.close()
                print("Log Sucessfully Updated at {}".format(date))
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()

def tpt():
    print("**********@ Hello Tejasv Pratap Tyagi @**********")
    print("Press 1 to goto Diet Section")
    print("Press 2 to goto Execise Section")
    c = int(input("Enter a value from above options : "))
    if c > 2:
        print("Please Enter an Option From above listed Choices!!!")
        tpt()
    else:
        if c == 1:
            print("**********@Welcome to Diet Section@**********")
            print("Press 1 to Retrieve data ")
            print("Press 2 to log/update data")
            c1 = int(input("Enter a value from above options : "))
            if c1 == 1:
                with open("tpt diet.txt") as s1:
                    print(s1.read())
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
            else:
                s2 = open("tpt diet.txt", "a")
                data = input("Enter Food Item : ")
                s2.write(data)
                s2.write(" : ")
                s2.write(date)
                s2.write("\n")
                s2.close()
                print("Log Sucessfully Updated at {}".format(date))
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
        else:
            print("**********@Welcome to Exercise Section@**********")
            print("Press 1 to Retrieve data ")
            print("Press 2 to log/update data")
            c1 = int(input("Enter a value from above options : "))
            if c1 == 1:
                with open("tpt ex.txt") as s1:
                    print(s1.read())
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
            else:
                s2 = open("tpt ex.txt", "a")
                data = input("Enter Exercise Name : ")
                s2.write(data)
                s2.write(" : ")
                s2.write(date)
                s2.write("\n")
                s2.close()
                print("Log Sucessfully Updated at {}".format(date))
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
def gaytri():
    print("**********@ Hello Gaytri @**********")
    print("Press 1 to goto Diet Section")
    print("Press 2 to goto Execise Section")
    c = int(input("Enter a value from above options : "))
    if c > 2:
        print("Please Enter an Option From above listed Choices!!!")
        gaytri()
    else:
        if c == 1:
            print("**********@Welcome to Diet Section@**********")
            print("Press 1 to Retrieve data ")
            print("Press 2 to log/update data")
            c1 = int(input("Enter a value from above options : "))
            if c1 == 1:
                with open("gaytri diet.txt") as s1:
                    print(s1.read())
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
            else:
                s2 = open("gaytri diet.txt", "a")
                data = input("Enter Food Item : ")
                s2.write(data)
                s2.write(" : ")
                s2.write(date)
                s2.write("\n")
                s2.close()
                print("Log Sucessfully Updated at {}".format(date))
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
        else:
            print("**********@Welcome to Exercise Section@**********")
            print("Press 1 to Retrieve data ")
            print("Press 2 to log/update data")
            c1 = int(input("Enter a value from above options : "))
            if c1 == 1:
                with open("gaytri ex.txt") as s1:
                    print(s1.read())
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
            else:
                s2 = open("gaytri ex.txt", "a")
                data = input("Enter Exercise Name : ")
                s2.write(data)
                s2.write(" : ")
                s2.write(date)
                s2.write("\n")
                s2.close()
                print("Log Sucessfully Updated at {}".format(date))
                print("To Go back to Main menu press 1")
                print("To Exit enter 2")
                mm = int(input("Enter value : "))
                if mm == 1:
                    main()
                else:
                    exit()
def main():
    print("**********@ Welcome to Health Management System @**********")
    print("Press 1-For Shubham")
    print("Press 2-For Tpt")
    print("Press 3-For Gaytri")
    print("Press 4-For Exit")
    a=int(input("Enter Your Choice For Client : "))
    if a>4:
        print("Please Enter an Option From above listed Choices!!!")
        a = int(input("Enter Your Choice For Client : "))
        if a == 1:
            shubham()
        elif a == 2:
            tpt()
        elif a==3:
            gaytri()
        else:
            exit()
    elif a==4:
        exit()
    else:
        if a == 1:
            shubham()
        elif a == 2:
            tpt()
        else:
            gaytri()
if __name__=="__main__":
    main()


