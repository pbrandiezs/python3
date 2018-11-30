#!/user/bin/env python3

filename = input("File Name? ")

try:
    f = open(filename, 'w')
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:
    with f:
        line = input("line? ")
        lines = line + "\n"
        while line:
            line = input("line? ")
            if line:
                lines = lines + line +"\n"
            else: 
                break
        print(f"lines:\n{lines}")
        f.write(lines)
f.close()

        