import re

# Load the hex dump
with open("bl2_hex.txt", "r", encoding="utf-8", errors="ignore") as file:
    data = file.read()

# Extract readable strings (ASCII characters, 4+ length)
strings = re.findall(r"[ -~]{4,}", data)

# Save to file or print
with open("readable_strings.txt", "w") as out:
    for s in strings:
        out.write(s + "\n")

print(f"Extracted {len(strings)} strings.")
