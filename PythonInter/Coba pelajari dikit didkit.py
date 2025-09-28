def pascal_triangle(rows):
    triangle = []
    for r in range(rows):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for i in range(1, len(last_row)):
                row.append(last_row[i - 1] + last_row[i])
            row.append(1)
        triangle.append(row)
    return triangle

def print_pascal_with_fibonacci(rows):
    triangle = pascal_triangle(rows)
    fib_positions = []

    # Tentukan posisi diagonal Fibonacci
    for d in range(rows):
        for r in range(d + 1):
            c = d - r
            if c < len(triangle[r]):
                fib_positions.append((r, c))

    # Cetak segitiga Pascal dengan highlight angka Fibonacci
    for r in range(rows):
        print(" " * (rows - r) * 2, end="")  # Spasi untuk bentuk segitiga
        for c in range(len(triangle[r])):
            val = triangle[r][c]
            if (r, c) in fib_positions:
                print(f" {val} ", end=" ")  # Highlight angka Fibonacci
            else:
                print(f" {val} ", end=" ")
        print()  # Baris baru

# Contoh penggunaan
print_pascal_with_fibonacci(9)


