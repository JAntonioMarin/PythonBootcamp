import ipywidgets as widgets
from IPython.display import display

w = widgets.IntSlider()
display(w)

w.layout.margin = 'auto'
w.layout.height = '75px'

x = widgets.IntSlider(value=15, description='New slider')
display(x)

x.layout = w.layout

import ipywidgets as widgets

widgets.Button(description='Ordinary Button', button_style='')
widgets.Button(description='Danger Button', button_style='danger')

b1 = widgets.Button(description='Custom color')
b1.style.button_color = 'lightgreen'
print(b1)

b1.style.keys

b2 = widgets.Button()
b2.style = b1.style
print(b2)

s1 = widgets.IntSlider(description='Blue handle')
s1.style.handle_color = 'lightblue'
print(s1)
