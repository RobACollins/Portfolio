# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:17:48 2017

@author: gy17rac
"""

#The following code is the model created within the practicals.
#This can be ran within a python simulator or within command line with "python ./model.py"

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import tkinter
import matplotlib.backends.backend_tkagg
import requests
import bs4

#This code grabs the x and y coordinates from the practical website. 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})


"""This creates the variables that the model will be built upon
Number of agents relates to the number of sheep.
Number of iterations details how many moves the agents will make.
Total is the total store, which relates to the amount of the environment the sheep can fit within them.
Neighbourhood limits the size of the environment.
"""
num_of_agents = 10
num_of_iterations = 100
total = 5000
neighbourhood = 20

agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)


"""This bit of code will make the environment before below this reads the file containing the environment and then appends each row to the environment variable."""
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
environment = []                #Makes the environment
for row in reader:				# A list of rows
    rowlist = []                #Makes
    for value in row:       		# A list of value
        rowlist.append(float(value))
    environment.append(rowlist)
    print(value) 				# Floats
f.close() 

#Make the agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

#Introduction of the carry on until function
carry_on = True	

#The def update he begins the process of the programme becoming an animation, so that it runs for multiple frames.
def update(frame_number):
    
    fig.clear()
    global carry_on
    
# Move the agents.
    for j in range(num_of_iterations):
        from random import shuffle
        shuffle(agents)
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
        
        """this has been put within the for loop to show that the agents are moving by 100 steps
        not needed to run the model but worthwhile looking at for testing purposes
        print(agents[i].x)"""
    
    """This is the query implemented as to whether or not the program will continue to run, 
    it will only stop when the total amount is less than that stored by the agents"""
    if total < agents[i].store:
        carry_on = False
        print("stopping condition")
    
    #This next bit of code acts to open the environment that the agents will be acting on 
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    #This is plotting the scatter for each frame
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print(agents[i].x,agents[i].y)

#This generator function acts to stop the programme once the carry on function requies the programme to stop. 
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


"""This next bit is the plotting of the animation of the scatter"""
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=num_of_iterations)
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.show()
    
""" This code below creates the main window for the model, this relates to the canvas and the menu to start the model."""
root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


"""The following code writes the outputs from the model to two files. 
The first file writes the environment. In terms of where the agents have collected the environment.
The second file writes the total amount that the agents gather to one file."""
f2 = open('dataout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		# List of values.
f2.close()

f3 = open('datatotal.csv', 'a', newline='')
writer = csv.writer(f3, delimiter=',')
a = []
for i in range(num_of_agents):
    a.append(float(agents[i].store))    #float allows it to be a decimal number
s = sum(a)
f3.write(str(s) + "\n")				# Floats
f3.close()


#This is the end loop to the window created above.
tkinter.mainloop()



#Future Developments - the following code could be used alongside a sweeper file to make the model more user friendly. This code is not used here but is an example of future work.
"""import sys

print ('Argument Lists', str(sys.argv))

num_of_agents = int(sys.argv[1])
num_of_iterations = int(sys.argv[2])
neighbourhood = int(sys.argv[3])"""


