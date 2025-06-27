import numbers

def convert_numbers_to_words(numbers):
    numbers_to_words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten'
}
    return numbers_to_words.get(numbers, "Invalid number")

if __name__ == '__main__':
    number = int(input("Enter a number: "))
    numbers_to_words = convert_numbers_to_words(number)
    print(f" The number {number} is: {numbers_to_words}")