import instaloader
import os
import sys

location = os.getcwd()
#Getting the configuration details from the config file
configuration = {  config.split("=")[0]:config.split("=")[1] for config in open(f"{location}/config.txt").read().split('\n')}

USERNAME = configuration['username']
PASSWORD = configuration['password']
HASHTAG = configuration['hashtag']
n=int(configuration['n'])



def web_scraping_insta(n):
    """ This function is to download the data from the instagram 
    based the parameter passed.
    :param n: n, n number of latest post to be downloaded.
    ex - web_scraping_insta(10)  it downloads the latest 10 post containing hastag HASHTAG
    """
    
    try:
        loader = instaloader.Instaloader(download_pictures=False,download_videos=False,compress_json=False)
        loader.login(USERNAME, PASSWORD)
        loader.download_hashtag(HASHTAG,max_count=n,profile_pic=False)
    except Exception as e:
        print(f"Error while downloading coentent of hashtag - {HASHTAG} - {e}")
            
if __name__ == "__main__":
    web_scraping_insta(n)


