import tkinter

def runDrawGrid():
  root = tkinter.Tk()
  canvas = tkinter.Canvas(root, width=400,height=400)
  canvas.configure(bd=0,highlightthickness=0)
  canvas.pack()
  drawGrid(canvas, 4) # your call here!
  root.mainloop()


def drawGrid(canvas, size):
    for row in range(size):
        topSq = row * 50
        bottomSq = topSq + 50
        for col in range(size):
            leftSq = col * 50
            rightSq = leftSq + 50
            if (row+col)%2==0:
                color="red"
            else:
                color="blue"
            canvas.create_rectangle(leftSq, topSq, rightSq, bottomSq, fill=color)

runDrawGrid()