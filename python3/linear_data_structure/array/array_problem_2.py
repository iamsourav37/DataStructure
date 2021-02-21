# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max_number = int(input("Enter max number : "))

odd_list = [x for x in range(1, max_number+1) if x % 2 == 1]
print(odd_list)