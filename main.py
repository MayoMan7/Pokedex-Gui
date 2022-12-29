import data
import turtle

global type_colors
type_colors = {
  "Fire": "#e76f51",
  "Fairy": "#ffafcc",
  "Water": "#90e0ef",
  "Grass": "#80ed99",
  "Electric": "#ffbd00",
  "Dragon": "#3a0ca3",
  "Steel": "#979dac",
  "Ground": "#6c584c",
  "Rock": "#a98467",
  "Bug": "#606c38",
  "Dark": "#001233",
  "Psychic": "#e4c1f9",
  "Flying": "Light Blue",
  "Ice": "#b2f7ef",
  "Normal": "Light Gray",
  "Ghost": "#9c89b8"
}

running = True

somthing = turtle.Turtle()
somthing.hideturtle()

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)


def write_name(name):
  somthing.pencolor("white")
  somthing.penup()
  somthing.setpos(0, 30)
  somthing.write(name.title(), align="center", font=("Welland", 25, "italic"))


def write_stats(name):
  somthing.pencolor("white")
  somthing.penup()
  somthing.setpos(0, 0)
  counter = 0
  stats = data.get_stats(name)
  if data.get_stats(name) == None:
    somthing.write("Not valid pokemon",
                   align="center",
                   font=("Cooper Black", 10, "italic"))
    return ("empty lmao")
  for i in stats:
    somthing.penup()
    somthing.write(i + ": " + str(stats[i]),
                   align="center",
                   font=("Cooper Black", 10, "italic"))
    counter += -15
    somthing.setpos(0, counter)


def type_match(name):
  type = data.get_type(entry)
  if type == None:
    return ("Black")
  global type_colors
  for i in type_colors:
    if i == type[0]:
      return (type_colors[i])
  return ("Black")


while (running):
  entry = input("choose a pokemon: ")
  turtle.Screen().bgcolor(type_match(entry))
  write_name(entry)
  write_stats(entry)
  input("press enter to continue")
  somthing.clear()
