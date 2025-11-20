def string_to_integer(s):
    result = 0
    for ch in s:
        # Convert character to its numeric value
        digit = ord(ch) - ord('0')
        result = result * 10 + digit
    return result
s = input("Enter a string of digits: ")
number = string_to_integer(s)
print("Converted integer:", number)
