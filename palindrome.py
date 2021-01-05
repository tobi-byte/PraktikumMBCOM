def isPalindrome (wort): 
    wort = wort.lower()
    for index in range (len(wort)//2):
        if wort [index] != wort[len(wort)-index-1]:
            return False
    return True

wort = input ("wort ") 
palindromeBool = isPalindrome (wort)
if palindromeBool:
    print ("Ist ein Palindrom")
else:
    print ("Ist kein Palindrom")
