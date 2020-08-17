
    def _get_hourglasssum(matrix, row, col): # create a function to do calculation 
        sum = 0                             # sum is a function that returns the sum of each iterable
        sum += matrix[row-1][col-1]         # this grabs 
        sum += matrix[row-1][col]
        sum += matrix[row-1][col+1]         
        sum += matrix[row][col]
        sum += matrix[row+1][col-1]
        sum += matrix[row+1][col]
        sum += matrix[row+1][col+1]

        return sum                          # returns the sum 

    arr = []

    for arr_i in range(6):
        arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
        arr.append(arr_t)

    max_hourglass_sum = -63     # create a starting space for the variable. -63 is the lowest possible value that can be returned
    for i in range(1, 5):                                   # create 2 loosp for roows collums 1 2 3 4
        for j in range(1, 5):

            hourglasssum = _get_hourglasssum(arr, i, j)     # this function do calculate with the following argumetns
            if hourglasssum > max_hourglass_sum:            # if statement to compare the hourglass size
                max_hourglass_sum = hourglasssum

    print(max_hourglass_sum)                                # prints it out