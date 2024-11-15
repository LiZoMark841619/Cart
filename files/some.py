
def countApplesAndOranges(s, t, a, b, apples, oranges):
    validation_range = range(s, t)
    apple_tree_loc, orange_tree_loc = a, b
    
    apple_sum = 0
    for apple_loc in apples:
        apple_dist = apple_tree_loc + apple_loc
        if apple_dist in validation_range:
            apple_sum += 1

    
    orange_sum = 0
    for orange_loc in oranges:
        orange_dist = orange_tree_loc + orange_loc
        if orange_dist in validation_range:
            orange_sum += 1
            
    return apple_sum, orange_sum

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    print(countApplesAndOranges(s, t, a, b, apples, oranges)[0])
    print(countApplesAndOranges(s, t, a, b, apples, oranges)[-1])

