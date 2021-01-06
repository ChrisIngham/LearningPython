my_nums = [1,2,3,4,5,6]

# checks all even numbers
print(list(filter(lambda num:num%2 == 0, my_nums)))
# squares everything
print(list(map(lambda num:num**2, my_nums)))

