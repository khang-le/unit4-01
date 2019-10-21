#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program does some calculation


def main():
    gia_tri_vong_lap = 1
    congdon = 0
    user_input = int(input("Enter a positive number: "))
    print("")

    # process & output
    while gia_tri_vong_lap < user_input + 1:
        print("The numbers is: {}".format(gia_tri_vong_lap))
        congdon = congdon + gia_tri_vong_lap
        gia_tri_vong_lap = gia_tri_vong_lap + 1
    print("The sum of the numbers is: {} ".format(congdon))


if __name__ == "__main__":
    main()
