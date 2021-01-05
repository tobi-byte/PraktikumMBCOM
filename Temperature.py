def CelsiusToFahrenheit (celsius):
    return celsius * 1.8 + 32
def CelsiusToKelvin (celsius):
    return celsius + 273.15
def FahrenheitToCelsius (fahrenheit):
    return (fahrenheit - 32) / 1.8
def KelvinToCelsius (kelvin): 
    return kelvin - 273.15 
def readFloat (text): 
    value = input ("Temperatur in " + text.upper() +  " : ")
    return float (value)
def printTemperature (celsius, fahrenheit, kelvin): 
    print (celsius, "°C")
    print (fahrenheit, "°F")
    print (kelvin, "K")
    return 
unit = input("Wähle Einheit(C, F, K)")
print (unit)
if (unit == "C" or unit == "c"):
    celsius = readFloat (unit)
    fahrenheit = CelsiusToFahrenheit (celsius)
    kelvin = CelsiusToKelvin (celsius)
    printTemperature (celsius, fahrenheit, kelvin)
elif (unit.lower() == "f"):
    fahrenheit = readFloat(unit)
    celsius = FahrenheitToCelsius (fahrenheit)
    kelvin = CelsiusToKelvin (celsius)
    printTemperature (celsius, fahrenheit, kelvin)
elif (unit.upper() == "K"):
    kelvin = readFloat(unit)
    celsius = KelvinToCelsius (kelvin)
    fahrenheit = CelsiusToFahrenheit (celsius)
    printTemperature (celsius, fahrenheit, kelvin)
else: 
    print ("Falscher Input")
