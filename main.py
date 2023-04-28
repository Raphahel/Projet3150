import TwitterScrapper
import DataLink
import sys

def chooseScrapper(network, users):
    if(network == "twitter"):
        return twitterScrap(users)
    
    return None

def twitterScrap(users):
    datas = TwitterScrapper.scrapAllT(users)
    for data in datas:
        DataLink.addData(data)


def databaseGet(network, users):
    datas = [] 
    for user in users:
        datas.append(DataLink.getData(user, network))
    
    return datas

action = sys.argv[1].lower()
network = sys.argv[2].lower()
users = sys.argv[3].lower().split(',')


if(action == "scrap"):
    chooseScrapper(network, users)
elif(action == "getusers"):
    datas = databaseGet(network, users)
    for data in datas:
        print(data)
elif(action == "getreliability"):
    datas = databaseGet(network, users)
    for data in datas:
        print(data["Username"] + " : " + '%.2f' % data["Reliability"])
else:
    print("action not recognised")
