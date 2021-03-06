"""
    returns the rotated list by n 

    >>> right_rotate([1,2,3,4,5,6], 3)
    [4, 5, 6, 1, 2, 3]

    >>> right_rotate([3,0,1,4,2,3], 3)
    [4, 2, 3, 3, 0, 1]

"""
    

def right_rotate(input_list, num):
    output_list = input_list[num:] + input_list[:num]
    return output_list












if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")