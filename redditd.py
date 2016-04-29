import time, random, os, datetime, sys, reddit, logging, itertools, ConfigParser, importlib
from multiprocessing import Process, Queue, current_process, freeze_support, cpu_count, Pool
imgur = importlib.import_module('modules.imgur')

#Diable logging from requests
logging.getLogger("requests").setLevel(logging.ERROR)

#Set up own logging
logdir = "logs"

if not os.path.exists(logdir):
    os.makedirs(logdir)
logfilename = logdir + "/" + datetime.datetime.now().strftime('redditd_%H_%M_%S_%d_%m_%Y.log')
logging.basicConfig(
    filename=logfilename,
    format='%(levelname)s:%(message)s',
    level=logging.INFO
)

def getImgurImages(targetSubreddit, limit=25, feed_type="hot"):
    logging.info("[ --- Searching %s most recent %s posts from %s for imgur files --- ]", limit, feed_type, targetSubreddit)
    daysAgo = 0
    count = limit

    while count > 0:
        #submissions = reddit.get_submissions(targetSubreddit, count, feed_type)
        submissions = reddit.getSubmissionsFromDaysAgo(targetSubreddit, daysAgo, count, feed_type)
        for submission in submissions:
            result = imgur.getImage(submission, targetSubreddit)
            if result:
                count -= 1
        daysAgo+=1

def main():
    if len(sys.argv) >= 3:
        targetSubreddit = sys.argv[1]
        limit = int(sys.argv[2])
        feed_type = "hot"
        if(len(sys.argv) > 3):
            feed_type = sys.argv[3]
        getImgurImages(targetSubreddit, limit, feed_type)
    else:
        print "Usage: python redditd.py (targetSubreddit) (Limit) (new/hot/rising)"
        exit(0)

if __name__ == '__main__':
    start_time = time.time()
    freeze_support()
    main()
    logging.info("--- %s seconds ---", (time.time() - start_time))
