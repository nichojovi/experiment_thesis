def print_number_staircase(start, step, n):
    # TODO: Modify the code, use i to calculate the staircase value in each iteration
    for _ in range(n):
        staircase = start + step * n
        print(staircase)

