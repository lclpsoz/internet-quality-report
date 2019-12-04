from datetime import datetime
from datetime import timedelta
from datetime import timezone
import sys
import visualGraph
from tqdm import tqdm

f = open (str (sys.argv[1]), 'r').read().strip()
ff = f.split ('\n')[1:]
all = []
for pos in tqdm(range (len (ff))):
    i = ff[pos]
    if (i == 'START'):
        break
    i = i.split ()
    tz = timezone(timedelta(hours=(int(i[1][1:]))) - timedelta(hours=3)) # TODO: Fix timezone problem in all project!!
    dt = datetime.fromtimestamp(int(i[0]))
    tp = (dt, i[-1] == 'ok')
    all.append (tp)

allPerSec = []
startDt = all[0][0]
dt = startDt
print (dt, all[-1][0])
pos = 0
state = True
acu = 0
while (dt <= all[-1][0]):
    if (all[pos][0] == dt):
        state = all[pos][1]
        acu = 0
        pos += 1
    elif (acu >= 6):
        state = False
    allPerSec.append ((dt, state))
    dt += timedelta (0, 1)
    acu += 1

valsThisHour = []
start = 0
for p in range (len(allPerSec)):
    if (int (allPerSec[p][0].timestamp())%3600 == 0):
        # print (len (valsThisHour))
        if (len (valsThisHour) < 3600):
            valsThisHour = []
        else:
            #visualGraph.generateRow (valsThisHour, 'files/internet_' + str(start))
            start = allPerSec[p][0]
            valsThisHour = []
    valsThisHour.append (not allPerSec[p][1])
    i = allPerSec[p]
    # print (p, i[0], i[0].timestamp())

#if (len (valsThisHour) == 3600):
#    visualGraph.generateRow (valsThisHour, 'files/internet_' + str(start))


ok = 0
fail = 0
startFail = -1
allFails = []
vals = []
for tp in allPerSec:
    if (tp[1]):
        if (startFail != -1):
            allFails.append ((startFail, tp[0] - timedelta(0, 1)))
            startFail = -1
        # print (".", end='')
        vals.append (0)
        ok+=1
    else:
        if (startFail == -1):
            startFail = tp[0]
        # print ("|", end='')
        vals.append (1)
        fail+=1

if (startFail != -1):
    allFails.append ((startFail, tp[0] - timedelta(0, 1)))
# print ("")
# print ("\Intervals without internet:")
timeWithout = timedelta(0)
for fls in allFails:
#    print (fls[0], fls[1], fls[1] - fls[0])
   timeWithout += fls[1] - fls[0]

thr = 15
print ("\Intervals without internet above", thr, "seconds:")
for fls in allFails:
    if (fls[1] - fls[0] + timedelta(0, 1) > timedelta (0, thr)):
        print (fls[0], fls[1], fls[1] - fls[0] + timedelta(0, 1))

print ("")
print ("From", startDt)
print ("To", all[-1][0])
print ("Duration of tests:", all[-1][0]-startDt)
print ("Duration without internet:", timeWithout)
print ("Percentage of time without internet: {0:.1f} %".format((fail/(ok+fail))*100, '%'))

for i in range (8):
    vals.pop()
valsCompressed = []
qnt = len(vals)//20000
for i in range (0, len (vals), qnt):
    if (i+qnt-1 >= len (vals)):
        break
    sum = 0
    for j in range (i, i+qnt):
        sum += vals[j]
    valsCompressed.append (sum >= qnt//2)
print ("Seconds per line of pixel in internet_all =", qnt)
visualGraph.generateRow (valsCompressed, "files/internet_all")

'''
for tp in all:
    if (tp[1]):
        print (".", end='')
    else:
        print ("|", end='')
print ("")
'''