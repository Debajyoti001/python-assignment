def binary_to_decimal(binary_str):
    result = 0
    for ch in binary_str:
        # Convert '0' or '1' to its numeric value
        bit = ord(ch) - ord('0')
        result = result * 2 + bit
    return result

# Example usage
binary_str = input("Enter a binary number: ")
decimal_value = binary_to_decimal(binary_str)
print("Decimal value:", decimal_value)
