# test
# die_visual
# AUTHOR: Maln
# TIME: 11/03/2017

from die import Die
import pygal

# Create a D6
die_1 = Die(num_sides=8)
die_2 = Die(num_sides=8)

# Make some rolls, store results
results = []

for roll_num in range(1000*10):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# Analyze Results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize Results

hist = pygal.Bar()
hist.title = "Results of rolling two D8 1000 times"
hist.x_labels = [str(i) for i in range(die_1.min_side+die_2.min_side,max_result+1)]
hist._x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)

