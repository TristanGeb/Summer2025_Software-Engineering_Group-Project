#look into inspect methods
#import inspect
line = "------------------------------------------\n"
def showinfo(obj):
    print(f"{line}type(obj)={type(obj)}\n{line}")
    print(f"{line}obj={obj}\n{line}")
    print(f"{line}dir(obj)={dir(obj)}\n{line}")
    print(f"{line}var(obj)={vars(obj)}\n{line}")
    #print(f"globals(obj)={globals(obj)}\n")
    #print(f"locals(obj)={locals(obj)}\n")
    #print(f"callable(obj)={callable(obj)}\n")
def get_help(obj):
    print(f"{line}help(obj)=")
    help(obj)
    print(f"\n{line}")
def log(str):
    print(str)
    print("\n")