import pyperclip

def main():
    file = input("Enter file name: ")
    filename = file+'.txt'
    try:
        with open(filename, "r") as f:
            code = f.read()
            pyperclip.copy(code)
            print("Setting up ...")
    except FileNotFoundError:
        print("code not found")