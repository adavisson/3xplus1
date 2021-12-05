def decision_time(number):
    return 3 * number + 1 if number % 2 else number / 2


def loop_it(value, count=0):
    if value == 1:
        return count

    next_value = decision_time(value)

    return loop_it(next_value, count + 1)


def main():
    for i in range(1, 15):
        print("Number: " + str(i) + str(loop_it(i)))


main()
