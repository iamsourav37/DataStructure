def insertion_sort(elements):
    for i in range(1, len(elements)):
        j = i - 1
        key = elements[i]

        while j >= 0 and elements[j] > key:
            elements[j+1] = elements[j]
            j = j-1
        elements[j+1] = key


def display_elements(elements):
    for i in elements:
        print(i, end=" ")
    print("")


def main():
    elements = [3, 20, 6, 9, 99, 12, 21, 2,77]

    print("Before sorting : ")
    display_elements(elements)
    insertion_sort(elements)
    print("After sorting : ")
    display_elements(elements)


if __name__ == '__main__':
    main()
