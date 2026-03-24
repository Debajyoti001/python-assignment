sales = [
    [5, 3, 0, 2],
    [7, 0, 2, 1],
    [0, 1, 4, 0]
]
t=[0,0,0,0]
for days in sales:
    for i in range(0, len(days)):
        t[i]=t[i]+days[1]
print("Total:",t)
max_sales=max(t)
min_sales=min(t)
for j in range(0, len(t)):
    print("Total sales of", j+1, "th product is",t[j])
    if t[j]==max_sales:
        print("Max products:", j+1, "th product")
    elif t[j]==min_sales:
        print("Min products:", j+1, j+1, "th product")
    else:
        continue