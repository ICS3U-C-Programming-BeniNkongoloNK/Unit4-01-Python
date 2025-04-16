#!/usr/bin/env python3
# Created By: Beni
# Date: April 16, 2025
# Calculates the sum of a number


def main():

    valid_input = False

    while not valid_input:

        user_num_str = input("Can you please give a number: \n")

        try:
            user_num_int = int(user_num_str)
            valid_input = True
            if user_num_int <= 0:
                print("Sorry that is not a positive integer!")
                valid_input = False
            else:
                sum = 0
                counter = 0
                while counter < user_num_int:
                    counter = counter + 1
                    sum = sum + counter
                print("The sum is {}".format(sum))
        except:
            print("Sorry that's not a integer. Please try again")


if __name__ == "__main__":
    main()
