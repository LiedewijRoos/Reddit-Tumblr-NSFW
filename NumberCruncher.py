'''
Calculates the number of nsfw and SFW Subs created per day,
'''
import csv, time, datetime

nsfw = 0
sfw = 0
dates = {}
months = []

with open("NSFWData.csv","a+") as d2:
    d2.seek(0)
    r = csv.reader(d2,delimiter=',')
    for line in r:
        d_str = line[1]
        if line[2] == "NSFW":
            nsfw += 1
        else:
            sfw+=1
        if d_str not in dates:
            nsfw = 0 #Comment these out for total rather than per day
            sfw = 0 #Comment these out for total rather than per day
            dates[d_str]=[d_str,str(nsfw),str(sfw),str(nsfw+sfw)]
        if d_str in dates:
            dates[d_str]=[d_str,str(nsfw),str(sfw),str(nsfw+sfw)]


with open("NSFWPerDay.csv","a+",newline='') as d2:
    w = csv.writer(d2,delimiter=',')
    w.writerow(["day","nsfw#","sfw#","total#"])
    w.writerows(list(dates.values()))