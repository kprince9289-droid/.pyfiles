# task1

def read_file():
    try:
        with open("simple.txt", "r") as file:
            print("File content:\n")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'simple.txt' does not exist.")
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    read_file()

 # task 2


def write_and_append():
    try:
        user_data = input("Enter some data to write into the file: ")

        with open("simple.txt", "w") as file:
            file.write(user_data + "\n")
        extra_data = input("Enter additional data to append: ")
        with open("simple.txt", "a") as file:
            file.write(extra_data + "\n")
        print("\nFinal content of output.txt:\n")
        with open("simple.txt", "r") as file:
            print(file.read())

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    write_and_append()
