import os
import sys

def main():

    command = sys.argv[1] 

    if command == "init":
        if os.path.exists(".git"):
            print("A git repository is already initialized here.")
        else:
            os.makedirs(".git",exist_ok=True)
            os.makedirs(".git/refs",exist_ok=True)
            os.makedirs(".git/objects",exist_ok=True)
            with open(".git/HEAD", "w") as file:
                file.write("ref: refs/heads/main\n")
            print("Initialized git repository.")
    


if __name__ == '__main__':
    main()