import time, random, os, datetime, sys, reddit, logging, itertools, ConfigParser, importlib, json
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

def write_progress(targetSubreddit, days_ago, count_left):
    file_name = "downloads/" + targetSubreddit + "/progress.json"
    data = {"days_ago" : days_ago, "count_left" : count_left}
    with open(file_name, 'w+') as fp:
        json.dump(data, fp)

def getImgurImages(targetSubreddit, limit=25, feed_type="hot"):
    logging.info("[ --- Searching %s most recent %s posts from %s for imgur files --- ]", limit, feed_type, targetSubreddit)
    daysAgo = 0
    count = limit
    
    file_name = "downloads/" + targetSubreddit + "/progress.json"
    if os.path.exists(file_name):
        with open(file_name) as json_file:
            json_data = json.load(json_file)
            daysAgo = json_data["days_ago"]

    while count > 0:
        submissions = reddit.getSubmissionsFromDaysAgo(targetSubreddit, daysAgo, count, feed_type)
        for submission in submissions:
            result = imgur.getImage(submission, targetSubreddit)
            if result:
                count -= 1
        daysAgo+=1
        write_progress(targetSubreddit, daysAgo, count)

def main():
    if len(sys.argv) >= 3:
        targetSubreddit = sys.argv[1]
        limit = int(sys.argv[2])
        feed_type = "hot"
        if(len(sys.argv) > 3):
            feed_type = sys.argv[3]
        getImgurImages(targetSubreddit, limit, feed_type)
    else:
        print "Usage: python redditd.py (targetSubreddit) (count) (new/hot/rising)"
        exit(0)

if __name__ == '__main__':
    start_time = time.time()
    freeze_support()
    main()
    logging.info("--- %s seconds ---", (time.time() - start_time))
