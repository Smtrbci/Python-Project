import turtle
import random


def kare(a):
  for i in range(4):
   ok.forward(a)
   ok.left(90)


renkler = ['red', 'green', 'blue', 'yellow', 'purple', 'black', 'brown']

ok = turtle.Turtle()
ok.speed(0)

kenar = 10
for i in range(35):
  ok.color(random.choice(renkler))
  kare(kenar)
  kenar = kenar + 10
  ok.right(10)
