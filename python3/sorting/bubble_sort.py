
def bubble_sort(elements):
    for i in range(len(elements)):
        for j in range(len(elements)-1-i):
            if elements[j] > elements[j+1]:
                # swap in better way
                elements[j] , elements[j+1] = elements[j+1], elements[j]
                # temp = elements[j]
                # elements[j] = elements[j+1]
                # elements[j+1] = temp


def bubble_sort_improved_version(elements):
    for i in range(len(elements)):
        is_sorted = True
        print("pass : ", i+1)
        for j in range(len(elements)-1-i):
            if elements[j] > elements[j+1]:
                is_sorted = False
                # swap
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
        if is_sorted:
            return


def display_elements(elements):
    for i in elements:
        print(i, end=" ")
    print("")


def main():
    elements = [1,12,3,45,43,62,11]
    display_elements(elements)  # displaying elements before sorting
    bubble_sort(elements)
    display_elements(elements)  # displaying elements after sorting

    bubble_sort_improved_version([12,3,4,5,9])


if __name__ == "__main__":
    main()