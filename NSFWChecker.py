import csv
import praw,time


reddit = praw.Reddit()#private

i=0
real_data = []
with open("cutdown.csv","a+",encoding='UTF-8') as d:
    d.seek(0)
    r = csv.reader(d, delimiter=',')
    w = csv.writer(d,delimiter=',')
    start = time.time()
    for lines in r:
        i+=1
        try:
            if reddit.subreddit(lines[0]).over18:
                n = "NSFW"
            else:
                n = "SFW"
            real_data.append([str(lines[0]), str(lines[1]), n])
            end = time.time()
            print("%.2f" % (end - start))
            print(i)
        except Exception as E:
            print(E)
with open("NSFWData.csv","a+",encoding='UTF-8') as d2:
    w = csv.writer(d2,delimiter=',')
    w.writerows(real_data)