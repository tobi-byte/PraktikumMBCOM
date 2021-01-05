height = int (input("What is the height: "))
print (height)
def print_pyramid (height):
    for index in range (height):
        print ("*", end = " ")
        for index2 in range (index):
            print ("*", end = " ")
        print ("\r")
print_pyramid (height)
        
