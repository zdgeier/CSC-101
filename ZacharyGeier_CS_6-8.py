def celsiusToFahrenheit(celsius):
    return (9/5) * celsius + 32

def fahrenheitToCelsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)

def main():
    print("Celsius", "Fahrenheit", "|", "Fahrenheit", "Celsius", sep="    ")
    print('-' * 51)
    
    c = 40.0
    f = 120.0

    for i in range(0,10):
        line = ''
        
        line += format(c, '<11.1f') + format(celsiusToFahrenheit(c), '<14.1f')
        line += '|' + (' ' * 4)
        line += format(f, '<14.1f') + format(fahrenheitToCelsius(f), '<14.2f')

        c -= 1
        f -= 10

        print(line)

main()
