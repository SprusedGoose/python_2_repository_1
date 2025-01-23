
number = []
append_numbers = []
summed_same = []

def is_sum(n):
   for i in range(1, n):
        n = str(n)
        number.append(n)
        append_numbers.append([int(x) for x in n])

is_sum(5)
print(append_numbers)