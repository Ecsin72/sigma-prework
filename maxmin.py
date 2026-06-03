def maxmin():
    numbers_input = input(
        "Please enter your desired numbers separated by spaces only: ")
    given_list = [int(num) for num in numbers_input.split()]
    if type(given_list) == list:
        sorted_list = sorted(given_list)
        maximum = int(sorted_list[-1])
        minimum = int(sorted_list[0])
        print([minimum, maximum])
    else:
        print("Please provide a valid list to use this function!")


maxmin()
