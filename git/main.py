import os
import sys
import zlib

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
    if command == "cat-file" and sys.argv[2] == "-p":
        object_name = sys.argv[3]
        with open(f".git/objects/{object_name[:2]}/{object_name[2:]}","rb") as file:
            content = file.read()
            decompressed_content = zlib.decompress(content)
            header,content = decompressed_content.split(b"\0")
            print(content)


if __name__ == '__main__':
    main()