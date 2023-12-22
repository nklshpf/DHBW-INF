def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Fehler: Division durch Null"

def calculator():
    print("Einfacher Taschenrechner")
    print("Verfügbare Operationen:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")

    choice = input("Bitte wähle die gewünschte Operation (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Gib die erste Zahl ein: "))
        num2 = float(input("Gib die zweite Zahl ein: "))

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        else:
            result = divide(num1, num2)
            operation = '/'

        print(f"\nErgebnis: {num1} {operation} {num2} = {result}")

    else:
        print("Falsch! Bitte wähle 1, 2, 3 oder 4.")

if __name__ == "__main__":
    calculator()
