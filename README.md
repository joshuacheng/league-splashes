## League Splashart Scraper!

Creates a folder called LeagueSplashes in the directory this is placed in and dumps
all the full-size jpegs in there.

Additional methods for changing the images to jpeg or resizing, for example, are located at
the bottom of the script and can be uncommented to use.

Dependencies: 
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
* [requests_html](https://html.python-requests.org/)
* [PIL](https://pillow.readthedocs.io/en/5.3.x/)

Note: This implementation is very specific as to the way Riot stores the champ splashes right now (through [Data Dragon](https://developer.riotgames.com/static-data.html))
and is subject to change without notice in the future. Working as of 11/20/2018

Uses Python 3.7
