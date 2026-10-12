from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        user_input = float(input("Enter a number: "))
        
        print(f"Square: {square(user_input)}")
        print(f"Is Even: {is_even(user_input)}")
        print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(user_input)}")
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    main()
