times=0
total=0
end=1
average=0
print("This program calculates the average. To stop the program, please enter 0")
while end==1:
    times=times+1
    num=int(input(str(times) + " Enter a number: "))
    if num==0:
        print("You have stopped the program")
        end=0
    else:
        total=total+num
        average=total/times
print("The average is", average)
