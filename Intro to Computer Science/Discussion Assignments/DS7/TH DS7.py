import math
import pylab
 
# try plotSquares(7), ... 100, 1000
#
def plotSquares(maxNum=20):
    pylab.clf()
    xlist, ylist = [], []
    for x in range(1,maxNum+1):
        xlist.append(x)
        ylist.append(x*x)
    pylab.plot(xlist, ylist)
    pylab.show()

# plot linear, n log n, and quadratic functions on the same chart
# try plotThree()
# 
def plotThree(maxNum=200):
    pylab.clf()
    xlist, linlist, nlognlist, sqlist = [], [], [], []
    for x in range(1,maxNum+1):
        xlist.append(x)
        linlist.append(50*x)
        nlognlist.append(25 * x * math.log(x,2))
        sqlist.append(x*x)
    pylab.plot(xlist, linlist, linestyle = '-', color = 'b')
    pylab.plot(xlist, nlognlist, linestyle = '--', color = 'r')
    pylab.plot(xlist, sqlist, linestyle = ':', color = 'g')
    pylab.savefig('plotTwoImage')
    pylab.show() 

# a simple bar chart
def barChartTest():
    pylab.clf() # clears the current chart
    pylab.bar([0,1,2,3], [5,10,12,2])
    # use xticks to specify bar labels
    pylab.xticks([v + 0.45 for v in range(4)], ('A', 'B', 'C', 'D') )
    pylab.show()

def coneChart(maxNum=1000):
    pylab.clf()
    xlist, ylist = [], []
    for x in range(1, maxNum+1):
        xlist.append(x)
        ylist.append(x * math.sin(x))
    pylab.plot(xlist, ylist)
    pylab.savefig('coneChart')
    pylab.show()