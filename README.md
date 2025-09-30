Steps to Push to Git Hub from Local PC

Microsoft Windows [Version 10.0.22621.4317]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Libin Daniel\Desktop\HEX_BIN_Converter>git init
Initialized empty Git repository in C:/Users/Libin Daniel/Desktop/HEX_BIN_Converter/.git/

C:\Users\Libin Daniel\Desktop\HEX_BIN_Converter>git remote add origin https://github.com/Libi486/Binary-Hex-ASCII-Converter.git

C:\Users\Libin Daniel\Desktop\HEX_BIN_Converter>git branch -M main

C:\Users\Libin Daniel\Desktop\HEX_BIN_Converter>git add .

C:\Users\Libin Daniel\Desktop\HEX_BIN_Converter>git commit -m "first commit"
[main (root-commit) 1fef86f] first commit
 7 files changed, 37 insertions(+)
 create mode 100644 Binary2Hex.py
 create mode 100644 Hex to readable.py
 create mode 100644 binary_output.txt
 create mode 100644 bl2_hex.txt
 create mode 100644 convert_to_binary.py
 create mode 100644 readable_strings.txt
 create mode 100644 your_file.bin

C:\Users\Libin Daniel\HEX_BIN_Converter>git push -u origin main
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 12 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (9/9), 271.77 KiB | 2.64 MiB/s, done.
Total 9 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/Libi486/Binary-Hex-ASCII-Converter.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
