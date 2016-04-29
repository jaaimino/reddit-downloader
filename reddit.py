'''
Initial stages of new python api caller
'''
import praw, datetime
from util import unix_time

def getSubmissionsFromDaysAgo(targetSubreddit, daysAgo, limit=25, feed_type="hot"):
    try:
        now = datetime.datetime.utcnow()
        now -= datetime.timedelta(hours=4,days=daysAgo)
        #print now
        now2 = now - datetime.timedelta(hours=now.hour,minutes=now.minute,seconds=now.second)
        #print now2
        now3 = now + datetime.timedelta(hours=(23 - now.hour),minutes=(59-now.minute),seconds=(59-now.second))
        #print now3
        lower = unix_time(now2)
        upper = unix_time(now3)
        #query = '(and author:"%s" (and timestamp:%d..%d))' % (usermode, lower, upper)
        query = 'timestamp:%d..%d' % (lower, upper)
        r = praw.Reddit(user_agent='CHANGE THIS TO A UNIQUE VALUE') # Note: Be sure to change the user-agent to something unique.
        searchresults = list(r.search(query, subreddit=targetSubreddit, sort=feed_type, limit=limit, syntax='cloudsearch'))
        return searchresults
        #print len(searchresults)
    except Exception as exception:
        print exception
        return []
