def print_number_staircase(start, step, n):
    staircase = start + step * n
    for _ in range(n):
        print(staircase)
