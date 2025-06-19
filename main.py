from sympy import symbols, Eq, solve, sqrt, simplify
from fractions import Fraction

x = symbols('x')

def solve_proportion():
    print("Enter proportion (a:b = c:x). Use 'x' for unknown.")
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    d = input("d: ")

    try:
        a = float(a) if a != 'x' else 'x'
        b = float(b) if b != 'x' else 'x'
        c = float(c) if c != 'x' else 'x'
        d = float(d) if d != 'x' else 'x'
    except:
        print("Invalid input.")
        return

    if a == 'x':
        result = c * b / d
    elif b == 'x':
        result = a * d / c
    elif c == 'x':
        result = a * d / b
    elif d == 'x':
        result = b * c / a
    else:
        print("No unknown variable ('x') found.")
        return

    print("Solved value of x:", result)

def solve_for_x():
    eq = input("Enter equation (example: 3*x + 2 = 11): ")
    try:
        lhs, rhs = eq.split('=')
        equation = Eq(eval(lhs), eval(rhs))
        result = solve(equation, x)
        print("Solution for x:", result)
    except Exception as e:
        print("Error:", e)

def factor_square_root():
    try:
        n = float(input("Enter number to factor its square root: "))
        result = simplify(sqrt(n))
        print(f"√{n} =", result)
    except:
        print("Invalid input.")

def decimal_to_fraction_percent():
    try:
        d = float(input("Enter decimal: "))
        frac = Fraction(d).limit_denominator()
        percent = round(d * 100, 2)
        print("Fraction:", frac)
        print("Percent:", f"{percent}%")
    except:
        print("Invalid input.")

def fraction_to_decimal_percent():
    try:
        num = int(input("Numerator: "))
        denom = int(input("Denominator: "))
        decimal = num / denom
        percent = round(decimal * 100, 2)
        print("Decimal:", decimal)
        print("Percent:", f"{percent}%")
    except:
        print("Invalid input.")

def percent_to_decimal_fraction():
    try:
        p = input("Enter percent (e.g., 45%): ").replace('%', '')
        p = float(p)
        decimal = p / 100
        frac = Fraction(decimal).limit_denominator()
        print("Decimal:", decimal)
        print("Fraction:", frac)
    except:
        print("Invalid input.")

def menu():
    while True:
        print("\n=== Multi-Function Calculator ===")
        print("1. Solve a proportion (a:b = c:x)")
        print("2. Solve for x in an equation")
        print("3. Factor square root")
        print("4. Convert decimal to fraction and percent")
        print("5. Convert fraction to decimal and percent")
        print("6. Convert percent to decimal and fraction")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            solve_proportion()
        elif choice == '2':
            solve_for_x()
        elif choice == '3':
            factor_square_root()
        elif choice == '4':
            decimal_to_fraction_percent()
        elif choice == '5':
            fraction_to_decimal_percent()
        elif choice == '6':
            percent_to_decimal_fraction()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the calculator
menu()
