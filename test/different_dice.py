# test
# die_visual
# AUTHOR: Maln
# TIME: 11/03/2017

from die import Die
import pygal

# Create a D6
die_1 = Die()
die_2 = Die(10)

# Make some rolls, store results
results = []

for roll_num in range(50000):
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
hist.title = "Results of rolling two D6 and D10 50,000 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist._x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')

print(frequencies)

