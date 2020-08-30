import clc

arry=[" ","0","1","2","3","4","5"]
arry0=["0","*","*","*","*","*","*"]
arry1=["1","*","0","*","*","*","*"]
arry2=["2","*","0","*","*","*","*"]
#arry5=[]
print(arry)
print(arry0)
print(arry1)
print(arry2)
while 1:
    print("event id for car in is 1 & event id for car out is 2 ")
    print("Enter the event id ")
    event=int(input())

    if event==1:
        print("in car in evernt")
        for i in range(0,5):

            if arry0[i]=="0" and i >0:
                print("Park the car at spot number 0{}".format(i-1))
        for i in range(0,5):
            if arry1[i]=="0":

                print("Park the car at spot number 1{}".format(i-1))
        for i in range(0,5):
            if arry2[i]=="0":

                print("Park the car at spot number 2{}".format(i-1))
    elif event==2:
        print("in car out evernt")
        print("enter your spot number")
        spot=int(input())
        if spot <100:
            k=spot
            c=int(k/10)
            m=spot%10
            print(c,m)
            if c==0:
                print("arry0")
                if m < 6:
                    arry0[m+1]=0
                    clc
            elif c==1:
                print("arry1")
                if m < 6:
                    arry1[m+1]="0"
                    clc
            elif c == 2:
                print("arry2")
                if m < 6:
                    arry2[m+1] = "0"
                    clc
        print("Enter the vaild spot only")
        print(arry)
        print(arry0)
        print(arry1)
        print(arry2)

    else:
        print("Enter the event id only")
        clc