# Input number of days late
days = int(input("Enter the number of days late: "))

# Check fine conditions
if days <= 5:
    f=(days*0.50)
    print("Fine is ",f)
elif days <= 10:
    f=(days*0.50)+(days-5)*1
    print("Fine is ",f)
elif days <= 30:
    f=(days*0.50)+(days*1)+(days*10)*6
    print("Fine is ",f)

else:
    print("Your membership is cancelled.")
