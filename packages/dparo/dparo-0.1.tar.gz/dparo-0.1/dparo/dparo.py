import pyperclip
import pkg_resources
def main():
    file = input("Enter file name: ")
    filename = file+'.txt'    
    try:
        code = pkg_resources.resource_string(__name__, filename)
        pyperclip.copy(code.decode('utf-8'))
        print("Setting up ...")
    except FileNotFoundError:
        print("Code not found")