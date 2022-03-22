import re

def file_to_test():
    user_input = input("Press 1 for sample or 2 for actual data to test:")
    if user_input == '1':
        return 'regex_sum_42.txt'
    elif user_input == '2':
        return 'regex_sum_1510266.txt'
    else:
        print('ERROR: Unsupported input.')
        file_to_test()

fhandle = open(file_to_test())

print( sum( [ int(num) for num in re.findall('[0-9]+',fhandle.read()) ] ) )

# sum = 0
# for line in fhandle:
#     numbers = re.findall(('[0-9]+'), line.rstrip())
#     if len(numbers) < 1 : continue
#     for number in numbers:
#         sum += int(number)
# print(sum)