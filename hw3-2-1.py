# Author: JD 09/29/2021

x = int(input("Please enter your grade: "))

if x > 100:
    print("This is not a valid grade.")
else:
    if x >= 93:
        print("A")
    else:
        if x >= 90:
            print("A-")
        else:
            if x >= 87:
                print("B+")
            else:
                if x >= 83:
                    print("B")
                else:
                    if x >= 80:
                        print("B-")
                    else:
                        if x >= 77:
                            print("C+")
                        else:
                            if x >= 73:
                                print("C")
                            else:
                                if x >= 70:
                                    print("C-")
                                else:
                                    if x >= 65:
                                        print("D+")
                                    else:
                                        if x >= 60:
                                            print("D")
                                        else:
                                            print("F")