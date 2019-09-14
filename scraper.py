import bs4
import os
from requests_html import HTMLSession

from PIL import Image
from os import listdir
from os.path import splitext



'''
    Scrapes the champion names off of the HTML provided.
    write: Whether or not the text file will be overwritten. Sometimes
           the page gives a bad response and will instead give no names back,
           which will essentially erase the text file.
           
    DEPRECATED OR SOMETHING (it's really just bugged)
'''


def get_champ_names_with_bs4(html, write=False, print_contents=False):
    soup = bs4.BeautifulSoup(html, features="html.parser")

    # print(innerHTML)

    champ_links = soup.find_all(class_="champ-name")
    champ_names = []
    file_string = ''
    for champ_info in champ_links:
        info = champ_info.contents
        champ_names.append(info[0]['href'])
        # champ_name_array.append(info[0]['href'])
        file_string += info[0]['href'] + ' '

    if len(champ_names) or write:
        name_file = open('ChampionNames.txt', 'w')
        name_file.write(file_string)
        name_file.close()

    if print_contents:
        name_file = open('ChampionNames.txt')
        file_contents = name_file.read()
        name_file.close()
        print(file_contents)


'''
    Gets all the champ names from ChampionNames.txt in the current directory
    to use as extensions on the base_url
    Returns them in a list
    :used for debugging purposes
'''


def retrieve_names():
    file = open('ChampionNames.txt')
    file_contents = file.read()
    file.close()

    arr = file_contents.split(' ')
    return arr


'''
    Gets all champion names and returns an array of them
    write: Write champion names to ./ChampionNames.txt
    print_names: Print out names as they are found
'''


def get_champ_names_with_requests(write=False, print_names=False):
    r = session.get(base_url)
    r.html.render()
    names = r.html.find('.champ-name')
    champ_name_array = []

    # Sometimes it fails for some reason keep trying
    while len(names) == 0:
        r = session.get(base_url)
        r.html.render()
        names = r.html.find('.champ-name')

    file_string = ''

    for i in range(0, len(names)):
        names[i] = names[i].find('a', first=True)
        names[i] = names[i].attrs['href']
        file_string += names[i][:-1] + ' '
        champ_name_array.append(names[i][:-1])

    if print_names:
        print(names)

    # Write to champion names file
    if write:
        name_file = open('ChampionNames.txt', 'w')
        name_file.write(file_string)
        name_file.close()

    return champ_name_array


'''
    Download all the champ splash arts given the names of all champions.
'''


def do_the_do(name_arr):
    images_base_url = 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/'

    # Start getting to all those links
    for name in name_arr:
        i = 0
        while True:
            extended_url = images_base_url + name + '_' + str(i) + '.jpg'
            print(extended_url)
            response = session.get(extended_url, stream=True)
            if response.status_code == 403:
                break

            image_url = './LeagueSplashes/' + extended_url[60:] + '.jpg'
            with open(image_url, 'wb') as image_file:
                image_file.write(response.content)

            i += 1



'''
    Converts all jpg files in a directory to pngs
    Directory is a relative path
'''


def convert_directory_to_pngs(directory):
    target = '.png'

    for file in listdir(directory):
        filename, extension = splitext(file)
        try:
            if extension not in ['.py', target]:
                im = Image.open(directory + filename + extension)
                im.save(directory + filename + target)
                os.remove(directory + filename + extension)
                print('Converted %s' % filename)
        except OSError:
            print('Cannot convert %s' % file)


def remove_jpg_from_names(directory):
    for file in listdir(directory):
        filename, extension = splitext(file)
        try:
            if filename[-4:] == '.jpg':
                os.rename(directory + file, directory + file[:-4])
        except OSError:
            print('Cannot convert %s' % file)

        print('just did %s' % filename)


'''
    Changes all images in a directory to 80x80
'''


def convert_size_to_80x80(directory):
    for file in listdir(directory):
        try:
            im = Image.open(directory + file)
            im = im.resize((80, 80), Image.ANTIALIAS)
            im.save(directory + file)
            print('converted %s' % file)
        except OSError:
            print('Cannot convert %s' % file)


os.makedirs('./LeagueSplashes', exist_ok=True)
base_url = 'https://na.leagueoflegends.com/en/game-info/champions/'
session = HTMLSession()

all_names = get_champ_names_with_requests(False, True)
do_the_do(all_names)

# remove_jpg_from_names('./LeagueSplashes')
# convert_directory_to_pngs('./LeagueSplashes/')
# convert_size_to_80x80('./LeagueSplashes/')