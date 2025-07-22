line = "------------------------------------------\n"
def showinfo(obj):
    print(f"{line}type(obj)={type(obj)}\n{line}")
    print(f"{line}obj={obj}\n{line}")
    print(f"{line}dir(obj)={dir(obj)}\n{line}")
    #print(f"globals(obj)={globals(obj)}\n")
    #print(f"locals(obj)={locals(obj)}\n")
    #print(f"callable(obj)={callable(obj)}\n")
def log(str):
    print(str)
    print("\n")