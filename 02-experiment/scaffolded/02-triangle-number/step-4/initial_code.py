def print_number_triangle(n):
    # TODO: Modify the outer and inner loop range
    for i in range(n):
        row = ''
        for j in range(1, n + 1):
            row += str(j) + ' '
        print(row)