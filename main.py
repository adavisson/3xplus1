import time


def decision_time(number):
    return 3 * number + 1 if number % 2 else number / 2


def loop_it(value, count=0):
    if value == 1:
        return count

    next_value = decision_time(value)

    return loop_it(next_value, count + 1)


def three_x_plus_one(number):
    highest_count = 0
    highest_number = 0

    # print("Number | Count")
    # print("--------------")
    for i in range(1, int(number) + 1):
        count = loop_it(i)

        if count > highest_count:
            highest_count = count
            highest_number = i

        # print(i, " | ", highest_count)

    print("Highest Count is ", highest_count, " for number ", highest_number)


def main():
    val = input("Enter a number: ")

    start_time = time.time()
    three_x_plus_one(val)
    end_time = time.time()

    print("Time to Complete: ", str(end_time - start_time), "seconds")


main()
