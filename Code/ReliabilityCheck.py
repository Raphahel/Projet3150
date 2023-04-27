from datetime import date


#Get A dicctionnary representing a Twitter user and return the reliability score
#user is a dictionnary containing user information
#return a float corresponding to the reliability score
def reliabilityScoreTwitter(user):

    today = date.today()
    creationDateTab = user["Creation Date"].split(" ")
    creationDate = date(int(creationDateTab[1]), MonthToInt(creationDateTab[0]), 1)
    nbMonthSiceCreation = (today.year - creationDate.year) * 12 + today.month - creationDate.month

    ratioFollowerFollowed = float(user["Followers"]) / float(user["Follows"])
    ratioLikedTweet = float(user["Likes"]) / float(user["Tweet"])
    ratioCommentTweet = float(user["Comment"]) / float(user["Tweet"])
    ratioRetweetTweet = float(user["Retweet"]) / float(user["Tweet"])

    return (nbMonthSiceCreation**2 + ratioFollowerFollowed**2 + ratioLikedTweet**2 + ratioCommentTweet**2 + ratioRetweetTweet**2)**0.5




def MonthToInt(month):
    if(month == "January"):
        return 1
    if(month == "February"):
        return 2
    if(month == "March"):
        return 3
    if(month == "April"):
        return 4
    if(month == "May"):
        return 5
    if(month == "June"):
        return 6
    if(month == "July"):
        return 7
    if(month == "August"):
        return 8
    if(month == "September"):
        return 9
    if(month == "October"):
        return 10
    if(month == "November"):
        return 11
    if(month == "December"):
        return 12

    return 0