b = int(input("Type in a positive integer: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for i in a:
    if int(i) < b:
        new_list.append(i)
print (new_list)
