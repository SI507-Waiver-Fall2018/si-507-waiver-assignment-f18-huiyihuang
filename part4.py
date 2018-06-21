# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

f=open("noun_data.csv","r")
fread=f.readlines()
f.close()
x_noun = []
y_number = []
for n in range(len(fread)):
	if n > 0:
		parts = fread[n].split(",")
		x_noun.append(str(parts[0]))
		y_number.append(int(parts[1].strip())) 

data = [go.Bar(
    x=x_noun,
    y=y_number,
    name='Most Used Nouns',
    )]
layout = go.Layout(title="Most Used Nouns")
nouns_fig = go.Figure(data=data, layout=layout)

py.plot(data, filename='part4_viz_image')
py.image.save_as(nouns_fig, filename='part4_viz_image.png')

