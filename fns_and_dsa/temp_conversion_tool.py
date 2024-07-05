



#! C TO F = (14°C × 9/5) + 32 = 57.2°F

#! F To C = (14°F − 32) × 5/9 = -10°C

FAHRENHEIT_TO_CELSIUS_FACTOR = ''
CELSIUS_TO_FAHRENHEIT_FACTOR = ''

temperature = int(input('Enter the temperature to convert:'))
question = input('Is this temperature in Celsius or Fahrenheit? (C/F):')


def convert_to_celsius():
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = (temperature - 32) * 5 / 9
    print (f'{temperature}°F is {FAHRENHEIT_TO_CELSIUS_FACTOR}°C')
# convert_to_celsius()

def convert_to_fahrenheit():
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    CELSIUS_TO_FAHRENHEIT_FACTOR = (temperature * 9/5) + 32
    print(f'{temperature}°C is {CELSIUS_TO_FAHRENHEIT_FACTOR}°F')
# convert_to_fahrenheit()

if question == 'C':
    convert_to_fahrenheit()
elif question == 'F':
    convert_to_celsius()
else:
    print('wrong answer')