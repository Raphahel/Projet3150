import requests as r
from bs4 import BeautifulSoup
import ReliabilityCheck


def scrapAllT(users):

    datas = []

    for user in users:
        base_url = "https://nitter.net/" + user +"/with_replies"
        url = base_url
        header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        result = r.get(url, headers=header)

        page_soup = BeautifulSoup(result.content, "html.parser")
        

        data = {}
        data["Network"] = "twitter"
        data["Username"] = user.lower()
        data["Tweet"] = scrapNbTweet(page_soup)
        data["Followers"] = scrapNbFollowers(page_soup)
        data["Follows"] = scrapNbFollowing(page_soup)
        data["Likes"] = scrapNbLikes(page_soup)
        data["Creation Date"] = scrapCreationDate(page_soup)
        data.update(scrapCommentRetweet(page_soup, base_url, header))
        data["Reliability"] = ReliabilityCheck.reliabilityScoreTwitter(data)

        

        datas.append(data)

    return datas

        



def scrapNbTweet(page_soup):
    text = page_soup.select_one(".posts .profile-stat-num").text
    return int(text.replace(",", ""))

def scrapNbFollowers(page_soup):
    text = page_soup.select_one(".followers .profile-stat-num").text
    return int(text.replace(",", ""))

def scrapNbFollowing(page_soup):
    text = page_soup.select_one(".following .profile-stat-num").text
    return int(text.replace(",", ""))

def scrapNbLikes(page_soup):
    text = page_soup.select_one(".likes .profile-stat-num").text
    return int(text.replace(",", ""))

def scrapCreationDate(page_soup):
    text = page_soup.select_one(".profile-joindate .icon-container").text
    return text.replace(" Joined ", "")

def scrapCommentRetweet(page_soup, base_url, header):
    i = 0
    end = False
    comment = 0
    retweet = 0

    url = base_url
    while i < 5000 and end == False:
        print(url)
        result = r.get(url, headers=header)
        page_soup = BeautifulSoup(result.content, "html.parser")

        i += len(page_soup.select(".timeline-item"))

        retweetList = page_soup.select(".timeline-item .retweet-header")
    
        retweet += len(retweetList)
        commentList = page_soup.select(".timeline-item:not(:has(.retweet-header))  .replying-to")

        comment += len(commentList)

        if(page_soup.select_one(".timeline-footer .timeline-end") != None):
            end = True
        else:
            next_page_cursor = page_soup.select_one(".show-more:not(.timeline-item)  a")
            url = base_url + f"{next_page_cursor['href']}"
        
    
    return {"Comment" : comment , "Retweet" : retweet}

