# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename

def find_extension(filename):

    return filename.split('.')[-1]


def main():

    filename = input("Enter filename : ")

    extension = find_extension(filename)

    print(f"Extension is : \'{extension}\'")


if __name__ == '__main__':
    main()


