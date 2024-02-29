from user_interface import *

def main():
    try:
        num1, num2, operator = get_user_input()
        result = perform_operation(num1, num2, operator)
        display_result(result)
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
