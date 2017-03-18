# test
# die_visual
# AUTHOR: Maln
# TIME: 11/03/2017

from die import Die
import pygal

# Create a D6
die = Die()

# Make some rolls, store results
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze Results
frequencies = [results.count(value) for value in range(1,die.num_sides+1)]

# Visualize Results

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(i) for i in range(die.min_side,die.num_sides+1)]
hist._x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

print(frequencies)

