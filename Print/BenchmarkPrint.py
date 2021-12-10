import os
import time
from numpy import mean

tests = [('Python (py)', 'python Print\Print.py'),
        ('jython (-jar)', 'Print\PrintJy.bat')]

data = [] 
plotting = True
for label, cmd in tests:
    ret = []
    print("%s..." % label)
    for i in range(3):
        t1 = time.time()
        result = os.popen(cmd).read()
        taken = time.time() - t1
        ret.append(taken)
    taken = mean(taken)
    data.append((taken, label))

data.sort()
data.reverse()
for d,l in data:
	print(l.ljust(30), ("%.3f" % d).ljust(10), 'sec')
	
if plotting:
	data, labels = zip(*data)
	from pylab import array, bar, yticks, xticks, show, grid, arange, xlabel, ylabel, title
	xlocations = array(range(len(data)))+0.5
	width = 0.5
	bar(xlocations, data, width=width)
	yticks(arange(0, max(data)+1, .5))
	grid()
	xticks(xlocations, labels)
	xlabel("Python Interpeter / Platform")
	ylabel("Time (sec)")
	title("Print répété 100000 fois")
	show()