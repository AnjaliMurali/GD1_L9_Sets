input_string = input("Enter a string: ")

input_set = set(input_string.lower())

alphabet_set = set('abcdefghijklmnopqrstuvwxyz')

difference_set = alphabet_set - input_set

if len(difference_set) == 0:
    print("The input string is a pangram.")
else:
    print("The input string is not a pangram.")

