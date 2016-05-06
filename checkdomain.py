#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
import urllib2
from tabulate import tabulate

def _check_domain(urls=['google.com']):
  data = []
  for url in urls:
    try:
      content = json.loads( urllib2.urlopen('https://domainr.com/api/json/info?&q='+url).read() )
      data.append( [content['domain'],content['tld']['domain'],content['availability']] )
    except urllib2.URLError as err:
      print 'Internet Connection Error'
      break
    print tabulate(data,headers=['Domain Name','TLD','Availability'])


if __name__ == "__main__":
  _check_domain(sys.argv[1:])
