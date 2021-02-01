

def selection_sort(elements):

    for i in range(len(elements)):
        index_of_min = i

        for j in range(i+1, len(elements)):
            if elements[index_of_min] > elements[j]:
                index_of_min = j
        # swap
        temp = elements[i]
        elements[i] = elements[index_of_min]
        elements[index_of_min] = temp


def display_elements(elements):
    for i in elements:
        print(i , end=",")
    print("")


def main():
    elements = [12,3,45,32,20,76,9]
    display_elements(elements)
    selection_sort(elements)
    display_elements(elements)


if __name__ == '__main__':
    main()