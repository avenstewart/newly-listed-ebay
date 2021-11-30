import webbrowser
from bs4 import BeautifulSoup
import requests
import time
import os
import getopt
import sys
import pushover

# set to keep track of seen listings
seen = set([])

# returns list of <a class='vip'></a>
def getLinks(url):
    r = requests.get(url).content
    soup = BeautifulSoup(r, "html.parser")
    return soup.find_all('a', {'class': 's-item__link'})


def activity_check(chk_int, sleep_time):
    # notifies you every 24 hours that the script is still running - temporary solution to uptime monitoring
    if chk_int < (86400 / sleep_time):
        return chk_int + 1
    else:
        pushover.send_message("Ebay listing notifier is active.")
        return 0

def newListing(url, message, sleep_time, open_links):
    check_int = 0
    while True:

        # let user know that the script hasn't failed
        check_int = activity_check(check_int, sleep_time)

        time.sleep(sleep_time)
        print('Checking....')
        for link in getLinks(url):
            itm_link = link.get('href')
            itm_title = str(link.contents[0]).split('>')[1].split("<")[0]

            if itm_link not in seen:
                print(itm_link)
                seen.add(itm_link)
                os.system("terminal-notifier -title 'New Item Found' -message 'Open " + itm_link + "' -open '" + itm_link + "'")
                if open_links:
                    webbrowser.open(itm_link)
                if message:
                    pushover.send_listing(itm_title, itm_link)
            else:
                print('No more found...')
                break

def usage():
    print('Usage:\n-m --message: flag to allow send message of new founding \n-u --url: ebay url of new listings (it is much easier to change default in py file (also make sure url is for new listings))\n-s --sleep: change default sleep time, default is 60sec (or change in py file)\n-o --open: set open_links to true to automatically open links')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hmp:u:s:o', ['help', 'message', 'url=', 'sleep=', 'open'])
        pushover.send_message("Ebay listing notifier is active.")
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(2)

    # ***************************
    # defaults, change them to your liking or use the command line
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_ipg=50%27&_nkw=yeezy+boost+350+v2&_sop=10'
    sleep_time = 300
    message = True
    open_links = False

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
            exit()
        elif o in ('-m', '-message'):
            message = True
        # url is better to change default in this file rather than have an INPUT
        # else you have to escape the characters that interfere like '\' or '&'
        elif o in ('-u', '-url'):
            url = a
        elif o in ('-s', '-sleep'):
            sleep_time = a
        elif o in ('-o', '--open'):
            open_links = True
        else:
            print('unhandled option')

    # first run should be ignored (i mean unless you want to be notified of a bunch of stuff)
    for link in getLinks(url):
        itm_link = link.get('href')
        # itm_title = str(link.contents[0]).split('>')[1].split("<")[0]
        # pushover.send_listing(itm_title, itm_link)

        if itm_link not in seen:
            seen.add(itm_link)

    # while
    newListing(url, message, sleep_time, open_links)


if __name__ == "__main__":
    main()
