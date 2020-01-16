import math
import statistics
from functools import reduce

area = lambda radius: math.pi * (radius ** 2)

# from Celius to F
c_to_f = lambda data: (data[0], (9/5)*data[1]+32)

radii = [2, 5, 7.1, 0.5, 10]

output_areas = list(map(area, radii))
print(radii)
print(output_areas)

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 29, ("Tokyo", 27))]

output_temps = list(map(c_to_f, temps))
print(temps)
print(output_temps)

#filter the logic False values
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
print("====original data: {}".format(data))
avg = statistics.mean(data)
print("====the mean: {0}".format(avg))
filtered_list = list(filter(lambda x: x<avg, data))
print("====the filter output: {}".format(filtered_list))

# filter the None value
countries = ["", "China", "Japan", "Thailand", "Korea", "", "USA", "Canada"]
print("====Original list: {}".format(countries))

filtered_countries = list(filter(None, countries)) # Note 0 is considered None too
print("====Filtered countries: {}".format(filtered_countries))

# reduce function
# given data: [a1, a2, a3, ... an] and function: f(x,y)
# reduce(f, data):
#  step 1: val1 = f(a1, a2)
#  step 2: val2 = f(val1, a3)
#  step 3: val3 = f(val2, a4)
#  ...
#  step n-1: valn-1 = f(valn-2, an)
# return valn-1
# or: f(f(f(a1,a2),a3),a4),...an)

data=[2,3,7,11,13,17,19,23,29]
multiplier = lambda x,y: x*y
reduce_output = reduce(multiplier,data)
print("====output of reduce: {}".format(reduce_output))

try:
    with open("Gundam1.txt") as f:
        text = f.read()
        print(text)

except FileNotFoundError:
    text = None
    print("====File NOT Found")


countries = ["China", "Japan", "Thailand", "Korea", "USA", "Canada", "Mexico"]

try:
    with open("country.txt",'w') as f:
        for country in countries:
            f.write(country)
            f.write("\n")
except FileNotFoundError:
    pass

with open("country.txt",'w') as f:
    for country in countries:
        print(country, file=f)

with open("country.txt", 'a') as f:
    print(20*"=", file=f)
    print("There are {} countries.".format(len(countries)), file=f)
    