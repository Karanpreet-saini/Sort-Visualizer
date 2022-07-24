from tkinter import *
from tkinter import ttk
import random
from quick import quick_sort
from bubble import bubble
from merge import mergesort
from insertion import insertion


root = Tk()
root.title("Sort Visualizer")

root.maxsize(900, 600)
root.config(bg="white")

select_alg = StringVar()
data = []


def generate():
	global data

	# minval : minimum value of the range
	minval = int(minEntry.get())

	# maxval : maximum value of the range
	maxval = int(maxEntry.get())

	# sizeval : number of data
	# values/bars to be generated
	sizeval = int(sizeEntry.get())


	data = []
	for _ in range(sizeval):
		data.append(random.randrange(minval, maxval+1))

	drawData(data, ['Red' for x in range(len(data))])


def drawData(data, colorlist):
	canvas.delete("all")
	can_height = 380
	can_width = 550
	x_width = can_width/(len(data) + 1)
	offset = 30
	spacing = 10
	normalized_data = [i / max(data) for i in data]

	for i, height in enumerate(normalized_data):
		# top left corner
		x0 = i*x_width + offset + spacing
		y0 = can_height - height*340

		# bottom right corner
		x1 = ((i+1)*x_width) + offset
		y1 = can_height

		# data bars are generated as Red
		# colored vertical rectangles
		canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
		canvas.create_text(x0 + 2, y0, anchor=SE, text=str(data[i]))
	root.update_idletasks()


# function to initiate the sorting
def start_algorithm():
	global data

	if not data:
		return

	if (algmenu.get() == 'Quick Sort'):
		quick_sort(data, 0, len(data) - 1, drawData, speed.get())
		drawData(data, ['Green' for x in range(len(data))])

	elif (algmenu.get() == 'Bubble Sort'):
		bubble(data, drawData, speed.get())
		drawData(data, ['Green' for x in range(len(data))])

	elif (algmenu.get() == 'Merge Sort'):
		mergesort(len(data), data, 0, len(data) - 1, drawData, speed.get())
		drawData(data, ['Green' for x in range(len(data))])

	elif (algmenu.get() == 'Insertion Sort'):
		insertion(len(data), data, drawData, speed.get())
		drawData(data, ['Green' for x in range(len(data))])


Mainframe = Frame(root, width=600, height=200, bg="Black")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=600, height=380, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)

# creating user interface area in grid manner
# first row components
Label(Mainframe, text="SORTING ALGORITHMS", bg='Grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)

# algorithm menu for showing the
# name of the sorting algorithm
algmenu = ttk.Combobox(Mainframe, textvariable=select_alg, values=["Quick Sort", "Bubble Sort", "Merge Sort", "Insertion Sort"])
algmenu.grid(row=0, column=1, padx=5, pady=5)
algmenu.current(2)

# creating Start Button to start
# the sorting visualization process
Button(Mainframe, text="START", bg="Blue", command=start_algorithm).grid(row=1, column=3, padx=5, pady=5)

# creating Speed Bar using scale in Tkinter
speed = Scale(Mainframe, from_=0.10, to=2.0, length=100, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speed.grid(row=0, column=2, padx=5, pady=5)

sizeEntry = Scale(Mainframe, from_=6, to=60, resolution=1, orient=HORIZONTAL, label="Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

# minEntry : scale to select the
# minimum value of data bars
minEntry = Scale(Mainframe, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Minimum Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

# maxEntry : scale to select the
# maximum value of data bars
maxEntry = Scale(Mainframe, from_=20, to=100, resolution=1, orient=HORIZONTAL, label="Maximum Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

# creating generate button
Button(Mainframe, text="Generate", bg="Red", command=generate).grid(row=0, column=3, padx=5, pady=5)

root.mainloop()
