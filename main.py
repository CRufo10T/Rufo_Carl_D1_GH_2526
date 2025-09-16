# Working with Numbers
from pyscript import display, document

def formula(e):
    document.getElementById('output').innerHTML = ""
    b1 = float(document.getElementById('base1').value)
    b2 = float(document.getElementById('base2').value)
    h = float(document.getElementById('height').value)

    t = ((b1 + b2) / 2) * h

    display( f'The half of the sum of {b1} and {b2} times {h} equals the area of the trapezoid: {t}', target="output")