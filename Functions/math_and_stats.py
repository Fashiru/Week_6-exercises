import random
import math
import statistics


vals_1_100 = range(1, 101)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3, 10)
pi = math.pi


# Experimenting with a subset of integers 1-100
sum_sample = sum(vals_sample)
avg_sample = statistics.mean(vals_sample)
median_sample = statistics.median(vals_sample)


print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from  1 to 100: {sum_sample}")
print(f"Average of 75 sample values: {avg_sample}")
print(f"Median of 75 sample values: {median_sample}\n")


#Experimenting with a suspect of 200 values
avg_choices = statistics.mean(vals_choices)
median_choices = statistics.median(vals_choices)
mode_choices = statistics.mode(vals_choices)
std_dev_choices = statistics.stdev(vals_choices)
variance_choices = statistics.variance(vals_choices)

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {avg_choices}")
print(f"Median of 200 values: {median_choices}")
print(f"Mode of 200 values: {mode_choices}")
print(f"Standard deviation of 200 values: {std_dev_choices}")
print(f"Variance of 200 values: {variance_choices}\n")


#Modeling a random circle 
area_rounded_up = math.ceil(pi * (radius ** 2))
area_rounded_down = math.floor(pi * (radius ** 2))


print(f"_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_rounded_down}")
print(f"Radius = {radius}, area = {area_rounded_down}")

