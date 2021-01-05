lower_number = input ("Was ist die kleine Zahl?: ")
if not lower_number .isdigit():
    print ("Gib eine Zahl ein!")
    quit()
lower_number = int (lower_number)
upper_number = input ("Was ist die große Zahl?: ")
if not upper_number .isdigit():
    print ("Gib eine Zahl ein!")
    quit()
upper_number = int (upper_number)
gerade = input ("Gerade oder ungerade?(g, u): ")
print (gerade)
if gerade == "g":
    for index in range (lower_number, upper_number +1):
        if index % 2 == 0:
            print (index)
elif gerade == "u":
    for index in range (lower_number, upper_number +1):
        if index % 2 == 1:
            print (index)
else:
    print ("Gibts ned")
