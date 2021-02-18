# remove duplicate from a list of strings

def remove_duplicate(li):
    return list(set(li))


def main():
    li = ['Sourav', 'Ganguly', 'Gourab', 'Ganguly', 'Ratul', 'Rakshit', 'Ratul', 'Mukherjee']

    new_list = remove_duplicate(li)
    print(f"New list : {new_list}")


if __name__ == '__main__':
    main()