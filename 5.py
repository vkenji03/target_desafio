def invert_string(string):
    out = ''
    for char in string[::-1]:
        out += char
    return out

def main():
    string = input()
    print(invert_string(string))

main()