stdm=int(input("enter the marks"))
stdm2=int(input("enter the marks"))
stdm3=int(input("enter the marks"))


stdavg=(stdm+stdm2+stdm3)/3

print(stdavg)

if (stdm>stdm2) and (stdm>stdm3):
    print("marks1  is highest",stdm)

elif(stdm2>stdm3):
    print("marks2 is highest",stdm2)
   

else:
    print(" marks3 is highest",stdm3)
