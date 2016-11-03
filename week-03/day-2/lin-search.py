def linear_search(list, number):
    indicator = 0;
    for i, val in enumerate(list):
        if val == number:
            print(i)
            indicator = 1
    if indicator == 0:
        print(-1)

# linear_search([2, 54, 6, 2, 2, 2], 2)
#
# linear_search([4,5,6], 6)
#
# linear_search([4,5,6], 3)

linear_search([3, 4, 5, 56, 67, 45, 45, 45, 3, 5, 3, 4, 5, 56, 67, 45, 45, 45, 3, 5, 3, 4, 5, 56, 67, 45, 45, 45, 3, 5], 41)
