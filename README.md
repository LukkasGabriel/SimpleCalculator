# Simple Calculator

This is a simple Python program that allows you to perform basic mathematical operations on two numbers. The program provides a menu for the user to choose between several operations and includes a loop for continued use until the user decides to exit.


https://github.com/user-attachments/assets/46702680-eeb1-4aff-9ec4-d7a13234e846


## Features

- **Add two numbers**: Sum of the two numbers entered.
- **Multiply two numbers**: Product of the two numbers entered.
- **Find the largest number**: Determines the larger of the two numbers.
- **Enter new numbers**: Allows the user to input new numbers for the operations.
- **Exit the program**: Exits the program when the user selects the option.

## Requirements

- Python 3.x

## Usage

1. The program will first ask you to input two numbers.
2. You will then be presented with a menu of operations:
   - [ 1 ] Add the numbers
   - [ 2 ] Multiply the numbers
   - [ 3 ] Find the largest of the two numbers
   - [ 4 ] Enter new numbers
   - [ 5 ] Exit the program
3. Select an option by entering the corresponding number.
4. You can choose to continue using the program after each operation, or exit when you're done.

### Example

```python
first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))

menu = 0

while menu != 5:
    print('==-==-==-==-==-==-==-')
    print('[ 1 ] ADD')
    print('[ 2 ] MULTIPLY')
    print('[ 3 ] FIND LARGEST')
    print('[ 4 ] ENTER NEW NUMBERS')
    print('[ 5 ] EXIT THE PROGRAM')
    menu = int(input('Which option do you choose? '))

    if menu == 1:
        total = first_number + second_number
        print(total)

    elif menu == 2:
        product = first_number * second_number
        print(product)

    elif menu == 3:
        largest = max(first_number, second_number)
        print(largest)

    elif menu == 4:
        first_number = int(input('Enter first number: '))
        second_number = int(input('Enter second number: '))

    elif menu == 5:
        print('Exiting the program...')
        break

    else:
        print('Invalid option! Please try again.')

    continue_prompt = str(input('Do you want to continue? [Y/N] ')).upper()

    if continue_prompt == 'N':
        print('Exiting the program...')
        break

````

# How It Works

- The program continuously displays the menu of options until the user selects the "Exit" option.
- The user can perform basic arithmetic operations, find the largest number, or enter new numbers for subsequent calculations.
- The program also provides an option to exit after each operation, ensuring a smooth user experience.

# License
This project is open-source and licensed under the MIT License. See the LICENSE file for more details.
