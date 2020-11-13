# 1. Check validity of inputed credit card number using Luhn's Algorithm
# 2. Identify whether it is AMEX, VISA, MASTERCARD, OTHER
# 3. Print out result "Card Number" "AMEX, VISA, MASTERCARD, OTHER or INVALID"


def luhn_even(string_number):
    even_chars = string_number[-2::-2]
    luhn_even = 0
    for n in even_chars:
        multiplied_number = int(n) * 2
        first_digit = multiplied_number % 10
        second_digit = multiplied_number // 10
        luhn_even += first_digit + second_digit
    return luhn_even


def luhn_odd(string_number):
    odd_chars = string_number[-1::-2]
    luhn_odd = 0
    for n in odd_chars:
        number = int(n)
        luhn_odd += number
    return luhn_odd


cc= input("Enter your credit card number: ")
number = str(cc)

luhn = luhn_even(number) + luhn_odd(number)
luhn = str(luhn)
if luhn.endswith("0"):
    if number.startswith(('34', '37')) and len(number) == 15:
        cardtype = "AMEX"
    elif number.startswith(('51', '52', '53', '54', '55')) and len(number) == 16:
        cardtype = "MASTERCARD"
    elif number.startswith('4') and (len(number) == 13 or len(number) == 16):
        cardtype = "VISA"
    else:
        cardtype = "OTHER"
else:
    cardtype = "INVALID"

print(number + " " + cardtype)
