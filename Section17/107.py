import ipywidgets as widgets
from IPython.display import display

widgets.IntSlider()

w = widgets.IntSlider()
display(w)

w.close()
display(w)

w = widgets.IntSlider()
display(w)

print(w.value)

print(w.keys)

widgets.Text(value='Hello World!', disabled=True)

a = widgets.FloatText()
b = widgets.FloatSlider()
display(a, b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))

mylink.unlink()
