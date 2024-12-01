# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 1 dec 2024 
# ccc '03 j2

while True:
    # Read the number of photos (n)
    n = int(input())

    # If the input is 0, we stop the program
    if n == 0:
        break

    # Initialize variables to track the minimum perimeter and the corresponding dimensions
    min_perimeter = float('inf')  # Start with a large number for the minimum perimeter
    best_width = 0  # Variable to store the best width (dimension of the rectangle)
    best_height = 0  # Variable to store the best height (dimension of the rectangle)

    # Loop through possible widths from 1 to n (not just sqrt(n))
    for width in range(1, n + 1):
        # Calculate the minimum height that ensures the area (width * height) is at least n
        # This is the ceiling of n / width, i.e., the smallest integer height such that width * height >= n
        height = (n + width - 1) // width  # This is an efficient way to calculate ceiling(n / width)

        # Now calculate the perimeter for the current width and height
        perimeter = 2 * (width + height)

        # If this perimeter is smaller than the current minimum perimeter, update the best dimensions
        if perimeter < min_perimeter:
            min_perimeter = perimeter
            best_width = width
            best_height = height

    # Output the minimum perimeter and corresponding dimensions
    print(f"Minimum perimeter is {min_perimeter} with dimensions {best_width} x {best_height}")
