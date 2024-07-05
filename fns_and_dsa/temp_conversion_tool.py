fahrenheit_to_celsius_factor = (temperature - 32) * 5 / 9
celsius_to_fahrenheit_factor = (temperature * 9/5) + 32

question = input('Is this temperature in Celsius or Fahrenheit? (C/F):')


def convert_to_celsius():
    global fahrenheit_to_celsius_factor
    # fahrenheit_to_celsius_factor = (temperature - 32) * 5 / 9
    print (f'{temperature}°F is {fahrenheit_to_celsius_factor}°C')
# convert_to_celsius()

def convert_to_fahrenheit():
    global celsius_to_fahrenheit_factor
    # celsius_to_fahrenheit_factor = (temperature * 9/5) + 32
    print(f'{temperature}°C is {celsius_to_fahrenheit_factor}°F')
# convert_to_fahrenheit()

if question == 'C':
    convert_to_fahrenheit()
elif question == 'F':
    convert_to_celsius()
else:
    print('wrong answer')