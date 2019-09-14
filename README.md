## League Splashart Scraper!


### Usage

To run: `python3 scraper.py`

Creates a folder called LeagueSplashes in the directory this is placed in and dumps
all the full-size jpegs in there.

Additional methods for changing the images to jpeg or resizing, for example, are located at
the bottom of the script and can be uncommented to use.

Dependencies: 
* [Python 3.7](https://www.python.org/downloads/release/python-374/)
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
* [requests_html](https://html.python-requests.org/)
* [PIL/Pillow](https://pillow.readthedocs.io/en/5.3.x/)

Note: This implementation is very specific as to the way Riot stores the champ splashes right now (through [Data Dragon](https://developer.riotgames.com/static-data.html))
and is subject to change without notice in the future.  

Working as of 9/14/2019

### Improvements
* Make it run with command line args instead of changing source code
* Performance probably
* Get champ names from API/Data Dragon somewhere rather than scraping from info site (http://ddragon.leagueoflegends.com/cdn/9.18.1/data/en_US/champion.json)