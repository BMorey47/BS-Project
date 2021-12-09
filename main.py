import random


def gen_random_nums_sorted():
    r_list = []
    for i in range(1, 10):
        r = random.randint(1, 100)
        r_list.append(r)
    r_list.sort()
    return r_list


def b_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = int((left + right) / 2)
        # FOUND IT!
        if arr[mid] == target:
            return True
        # Is target Less than this?
        elif target < arr[mid]:
            right = mid - 1
        # else target is greater than current point
        elif target > arr[mid]:
            left = mid + 1
        else:
            raise Exception("WTF??!!")
    return False


    while True:
        s_list = gen_random_nums_sorted()

        print("Sorted List:", s_list)

        print(b_search(s_list, int(input())))


if __name__ == '__main__':

    while True:
        s_list = gen_random_nums_sorted()

        print("Sorted List:", s_list)

        print(b_search(s_list, int(input())))
