# new-ebay-items
A script that constantly checks for new items (provided by a url for now)

### Python needs
- python > 3
- beautifulsoup4
- requests
- configparser

## Pushover Config
Change the properties settings within config.properties.example to define your pushover user_key and application token

### Usage:
```bash

###########
# DEFAULTS
# url = 'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&_ipg=50%27&_nkw=yeezy+boost+350+v2&_sop=10'
# sleep_time = 60
# message = False
# open_links = False

###########
# -m --message: flag to allow send message of new founding
# -u --url: ebay url of new listings (it is much easier to change default in py file (also make sure url is for new listings))
# -s --sleep: change default sleep time, default is 60sec (or change in py file)


# run script with defaults (changed defaults in py file)
python script.py

# run script w/ defaults and open links automatically
python script.py -o

# run script with different url (no messages)
python -u  https:\/\/www.ebay.com\/sch\/i.html?_from=R40\&_sacat=0\&_ipg=50%27\&_nkw=yeezy+boost+350+v2\&_sop=10

# run python with different sleep_time (everything else is default)
python -s 30
```

#### Things used (credit & cool things)
- Pushover (https://pushover.net/)
- Credit to Josue-rojas for original script (https://github.com/josue-rojas/newly-listed-ebay)

#### TODO
- http://www.helios825.org/url-parameters.php ADD SUPPORT FOR CUSTOM URL IN INPUT
- maybe change to use the ebay api instead!?!?! [here](https://developer.ebay.com/Devzone/finding/CallRef/findItemsAdvanced.html)(but then it would need keys)
