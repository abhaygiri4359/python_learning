#wap python prg which accept string a display other than vowel
s=input("enter the word ")
for ch in s:
    if ch in "aAeEiIoOuU":
        continue
    print(ch)