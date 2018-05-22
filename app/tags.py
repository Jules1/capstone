import csv
import os 
"""get user tags some how"""



def compare(foodtags, usertags):
    result={}
    tcount = 0
    tags = foodtags[0].split(" ")
    """checking correlation with user tags"""
    if (tags[0] in usertags):
        tcount+= 1
    else:
        tcount +=0

    if (tags[1] in usertags):
        tcount+= 1
    else:
        tcount +=0

    if (tags[2] in usertags):
        tcount+= 1
    else:
        tcount +=0

    if (tcount == 3):
        result = {'name':foodtags[1], 'rating': 3}
        
    if (tcount == 2):
        result = {'name':foodtags[1], 'rating': 2}
        
    if (tcount == 1):
        result = {'name':foodtags[1], 'rating': 1}

    if (tcount < 1):
        result = {'name':foodtags[1], 'rating': 0}
    
    return result

"""def generaterecs():
    usertags = ['rice','chicken','jerk','beef','spicy','salad']
    recs = []
    with open('usertags.csv','rd') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            results = compare(row[2:], usertags)
            recs.append(results)
    csvfile.close()
    return (recs)"""

def generaterecs():
    usertags = ['rice','chicken','jerk','beef','spicy','salad']
    recs = []
    with open(os.path.join(os.path.dirname(__file__),'usertags.csv'),'rd') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            """print(row)"""
            results = compare(row[2:], usertags)
            """print(res)"""
            recs.append(results)
    csvfile.close()
    return (recs)


"""if __name__ == '__main__':
    x = generaterecs()
    print(x)"""

