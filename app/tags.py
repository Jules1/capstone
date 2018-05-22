import csv
import os 
"""get user tags some how"""



def compare(foodtags, usertags):
    result={}
    tcount = 0
    tags = foodtags[3].split(" ")
    tags2 = usertags.split(" ")
    """checking correlation with user tags"""
    if (tags[0] in tags2):
        tcount+= 1
    else:
        tcount +=0

    if (tags[1] in tags2):
        tcount+= 1
    else:
        tcount +=0

    if (tags[2] in tags2):
        tcount+= 1
    else:
        tcount +=0

    if (tcount == 3):
        result = {'name':foodtags[0], 'place':foodtags[1],'cost':foodtags[2],'image':foodtags[4], 'rating': 3}
        
    if (tcount == 2):
        result = {'name':foodtags[0], 'place':foodtags[1],'cost':foodtags[2],'image':foodtags[4] ,'rating': 2}
        
    if (tcount == 1):
        result = {'name':foodtags[0], 'place':foodtags[1],'cost':foodtags[2],'image':foodtags[4], 'rating': 1}

    if (tcount < 1):
        result = {'name':foodtags[0], 'place':foodtags[1],'cost':foodtags[2],'image':foodtags[4], 'rating': 0}

    
    return result

def generaterecs(tags):
    #usertags = ['rice','chicken','jerk','beef','spicy','salad']
    recs = []
    with open('app/Menu Items.csv','r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            '''results = compare(row[4:], tags)'''
            results = compare(row[1:], tags)
            recs.append(results)
        
    csvfile.close()
    sortedrec = sorted(recs, key=lambda k: k['rating'], reverse=True)
    return sortedrec 


"""if __name__ == '__main__':
    x = generaterecs()
    print(x[1]['name'])"""

