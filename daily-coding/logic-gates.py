def and_gate(input1, input2):
    return input1 and input2

# Example usage:
input1 = 1
input2 = 0

result = and_gate(input1, input2)
print(f"The result of the AND gate with inputs {input1} and {input2} is: {result}")

def xor_gate(input1, input2):
    return input1 != input2

# Example usage:
input1 = 1
input2 = 0

result = xor_gate(input1, input2)
print(f"The result of the XOR gate with inputs {input1} and {input2} is: {result}")

def nand_gate(input1, input2):
    return not (input1 and input2)

# Example usage:
input1 = 1
input2 = 0

result = nand_gate(input1, input2)
print(f"The result of the NAND gate with inputs {input1} and {input2} is: {result}")