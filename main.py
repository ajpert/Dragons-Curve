"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
t.speed(0)

bonk = ['l','l']

num = 1;
show_draw = True
if show_draw == False:
  turtle.tracer(0, 0)
iteration = 5
turtle.screensize(canvwidth=30000, canvheight=30000,
                  bg="white")
for z in range(iteration):
  x = len(bonk)
  for y in range(x):
    bonk.append(bonk[y])
  x = len(bonk)
  if bonk[x-num] == 'l':
    bonk[x-num] = 'r'
  else:
    bonk[x-num] = 'l'
  num *= 2

print(len(bonk))


for n in bonk:
  if n == 'l':
    t.left(90)
  else:
    t.right(90)
  t.forward(5)

turtle.update()
