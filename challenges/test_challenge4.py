def test_challenge4():
    num_to_words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                    6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                    11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                    15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                    19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                    50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
                    90: 'Ninety', 0: 'Zero', 1000: 'Thousand ', 100: 'Hundred '}

    def fibonacci(n):
        if n == 1 or n == 0:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    number_sequence = 13

    def convert_to_words(number):
        try:
            if number // 1000 > 0:
                return convert_to_words(number // 1000) + num_to_words[1000]
            if 0 < number//100 < 10:
                if number % 100:
                    return convert_to_words(number // 100) + num_to_words[100] + convert_to_words(number % 100)
                else:
                    return convert_to_words(number // 100) + num_to_words[100]
            elif 2 <= number//10 < 10:
                return num_to_words[number - (number % 10)] + convert_to_words(number % 10)
            elif 0 <= number < 20:
                return ' ' + num_to_words[number] + ' '
        except KeyError:
            print('Out Of Bound')
    print(f'\n {fibonacci(number_sequence)}')
    print(f'\nAt the sequence term {number_sequence}, the fibonacci number is {convert_to_words(fibonacci(number_sequence))}')