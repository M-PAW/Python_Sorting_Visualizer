from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubble_sort
from quickSort import quick_sort

root = Tk()
root.title('Sorting Algorithm Visualization')
root.maxsize(900, 900)
root.config(bg='black')

#variables
selected_alg = StringVar()
data = []

#Functions

def drawData(data, colorArray):
    canvas.delete("all")
    c_height = 380
    c_width = 720
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizeData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizeData):
        # Top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        # bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW,  ) # text=str(data[i])

    root.update_idletasks()

def Generate():
    global data
    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data=[]
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal + 1))

    drawData(data, ['red' for x in range(len(data))])

def StartAlgorithm():
    global data

    if not data: return

    if algMenu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])

    elif algMenu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, speedScale.get())

    elif algMenu.get() ==  'Merge Sort':
        print("Merge Sort Selected")


# frame / base layout
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=780, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)
## Michael Walter - M-PAW on GitHub

#User Interface Area
#Row[0]
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(UI_frame, textvariable = selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=1, column=1, padx=5, pady=5, sticky=W)

sizeEntry = Scale(UI_frame, from_=1, to=100, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min")
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

maxEntry = Scale(UI_frame, from_=11, to=100, resolution=1, orient=HORIZONTAL, label="Max")
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=0, column=2, padx=5, pady=5)

## Michael Walter - M-PAW on GitHub

root.mainloop()