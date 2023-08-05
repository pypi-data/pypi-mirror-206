import builtins
import os
import re
import sys
import threading
import time
from typing import *
from urllib.parse import urlparse, urljoin
from rich import print as rprint
import requests

USE_RICH = True

fileLock = threading.Lock()
printLock = threading.Lock()


def check_int(s: str = ''):
    """ Check if a string is an integer
    :return: None if not an integer, otherwise the raw string
    """
    try:
        int(s)
        return s
    except:
        return None

def print_with_lock(*args, **kwargs):
    printLock.acquire()
    if USE_RICH:
        # replace [[ and ]] with "
        try:
            rich_args = args
            rich_args = [re.sub(r'\[\[', '\"', str(arg)) for arg in rich_args]
            rich_args = [re.sub(r'\]\]', '\"', str(arg)) for arg in rich_args]
            rprint(*rich_args, **kwargs)
        except: # fallback to builtins.print
            builtins.print(*args, **kwargs)
    else:
        builtins.print(*args, **kwargs)
    printLock.release()


def avoidSites(url: str, session: requests.Session):
    #check robots.txt
    r = session.get(urlparse(url).scheme + '://' + urlparse(url).netloc + '/robots.txt')
    if r.status_code == 200:
        if 'User-agent: ia_archiver\nDisallow: /' in r.text or f'User-agent: dokuWikiDumper\nDisallow: /' in r.text:
            print('This wiki not allow dokuWikiDumper or IA to crawl.')
            sys.exit(1)

    site = urlparse(url).netloc
    avoidList = ['www.dokuwiki.org']  # TODO: Add more sites
    if site in avoidList:
        if input('\nWarning:\nYou are trying to dump '+site+', which is in the avoid list. \n' +
                 'If you just want to test ' +
                 'if this program can dump dokuwiki successfully, please DO NOT do this, ' +
                 '\nthis will bring a lot of pressure to the server of ' + site +
                 '\n\nContinue anyway? (y/n): ') != 'y':
            sys.exit(1)

        print('You have been warned. :-)')
        time.sleep(3)


def smkdirs(parent: str = None, *child: str)-> Optional[str]:
    """ safe mkdir, return: True->created, False->existed """
    if parent is None:
        raise ValueError('parent must be specified')
    
    # lstrip / in child
    child = [c.lstrip('/') for c in child]

    dir = os.path.join(parent, *child)
    # print(dir)
    fileLock.acquire()
    if not os.path.exists(dir):
        os.makedirs(dir)
        fileLock.release()
        return dir

    fileLock.release()
    return None


def standardizeUrl(url: str = ''):
    """ Add http:// if not present """
    if not url.startswith('http'):
        url = 'http://' + url
    return url


def getDokuUrl(url: str = '', session=requests.Session):
    r = session.get(url)
    parsedUrl = urlparse(r.url)
    dokuUrl = urljoin(
        parsedUrl.scheme + '://' + parsedUrl.netloc + '/',
        parsedUrl.path
    ) # remove query string


    return dokuUrl


def buildBaseUrl(url: str = '') -> str:
    r = urlparse(url)
    path = r.path
    if path and path != '/' and not path.endswith('/'):
        path = path[:path.rfind('/')]
    baseUrl = r.scheme + '://' + r.netloc + path
    if not baseUrl.endswith('/'):
        baseUrl += '/'

    return baseUrl


def url2prefix(url):
    """Convert URL to a valid prefix filename."""

    # use request to transform prefix into a valid filename

    r = urlparse(url)
    # prefix = r.netloc + r.path
    if r.path and r.path != '/' and not r.path.endswith('/'):
        # truncate to last slash
        prefix = r.netloc + r.path[:r.path.rfind('/')]
    else:
        prefix = r.netloc + r.path
    prefix = prefix.lower()
    prefix = re.sub(r"(/[a-z0-9]+\.php)", "", prefix)
    prefix = prefix.strip('/')
    prefix = re.sub(r"/", "_", prefix)

    prefix = prefix.replace(':', '_') # port

    # domain = re.sub(r"\.", "", domain)
    # domain = re.sub(r"[^A-Za-z0-9]", "_", domain)

    return prefix


def loadTitles(titlesFilePath) -> Optional[List[str]]:
    """ Load titles from dump directory

    Return:
        `list[str]`: titles
        `None`: titles file does not exist or incomplete
     """
    if os.path.exists(titlesFilePath):
        with uopen(titlesFilePath, 'r') as f:
            titles = f.read().splitlines()
        if len(titles) and titles[-1] == '--END--':
            print('Loaded %d titles from %s' %
                  (len(titles) - 1, titlesFilePath))
            return titles[:-1]  # remove '--END--'

    return None


def uopen(*args, **kwargs):
    """ I dont wanna type `encoding=utf8` anymore.
    Made for Windows compatibility :-( """
    return open(*args, encoding='UTF-8', **kwargs)
