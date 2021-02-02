
def bubble_sort(elements):
    for i in range(len(elements)):
        for j in range(len(elements)-1-i):
            if elements[j] > elements[j+1]:
                # swap
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp


def display_elements(elements):
    for i in elements:
        print(i, end=",")
    print("")


def main():
    elements = [1,12,3,45,43,62,11]
    display_elements(elements)  # displaying elements before sorting
    bubble_sort(elements)
    display_elements(elements)  # displaying elements after sorting


if __name__ == "__main__":
    main()