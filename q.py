import turtle

def draw_bharat_mart_logo():
  turtle.penup()
  turtle.goto(0, 0)
  turtle.pendown()

  # Draw the circle
  turtle.fillcolor("#FFC107")
  turtle.begin_fill()
  turtle.circle(40)
  turtle.end_fill()

  # Write the text
  turtle.fillcolor("#000000")
  turtle.penup()
  turtle.goto(30, 0)
  turtle.pendown()
  turtle.write("Bharat", font=("Arial", 20))
  turtle.penup()
  turtle.goto(70, 0)
  turtle.pendown()
  turtle.write("Mart", font=("Arial", 20))

if _name_ == "_main_":
  draw_bharat_mart_logo()
  turtle.done()