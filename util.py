import urllib, logging, datetime, os
from os import listdir
from os.path import isfile, join

def downloadImage(targetSubreddit, submission, imageUrl, localFileName):
    filedir = "downloads" + "/" + targetSubreddit + "/"
    #filedir += str(submission.author) + "/"
    filepath = filedir + localFileName
    try:
        if os.path.isfile(filepath):
            #logging.info("Found duplicate at %s", filepath)
            return True
        else:
            if not os.path.exists(filedir):
                os.makedirs(filedir)
            response = urllib.urlopen(imageUrl)
            if(response.getcode() == 200):
                urllib.urlretrieve(imageUrl, filepath)
                return True
            else:
                return False
    except Exception as exception:
        logging.error(exception)
        return False

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def find_files(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]