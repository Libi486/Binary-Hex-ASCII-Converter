# Convert binary file to hex
with open("bl2 - Copy.bin", "rb") as f:
    data = f.read()

# Save as hex
with open("bl2_hex.txt", "w") as out:
    out.write(data.hex())
