import turtle

t = turtle.Turtle()
t.speed(0)
t.turtlesize(.5)

bonk = ['l','l']

num = 1;
show_draw = False #change to false to speed up process, but does not draw
if show_draw == False:
  turtle.tracer(0, 0)
iteration = 15
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
t.hideturtle()
turtle.update()
turtle.exitonclick()
