# Open and read the binary file
with open("your_file.bin", "rb") as f:
    data = f.read()

# Convert each byte to 8-bit binary
binary_data = ' '.join(format(byte, '08b') for byte in data)

# Save to a new file
with open("binary_output.txt", "w") as out:
    out.write(binary_data)

print("Conversion complete. Check 'binary_output.txt' for results.")
