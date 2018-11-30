#!/usr/bin/env python
# majestic.py (v.0.1) - Parsing the top n websites (rank and domain) from the majestic.com project
# written by SI9INT (twitter.com/si9int) | si9int.sh

import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()

parser.add_argument('max', help = 'upper-limit (in hundreds) < 1000000 ', type = int)
parser.add_argument('-t', '--tld', help = 'limits results to a specifc TLD (e.g. de)', type = str)

args = parser.parse_args()

if args.tld:
	print('[!] TLD set to: ' + args.tld)
else:
	print('[!] No TLD set, fetching global entries')
	args.tld = ''

def getThem(tld, page):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
	html = requests.get('https://majestic.com/reports/majestic-million?majesticMillionType=2&tld=' + tld + '&oq=&s=' + str(page),headers=headers).text

	try:
		soup = BeautifulSoup(html, 'lxml')
		table = soup.findAll('table', attrs={'class':'clean-table mob-margin'})[0]
		trs = table.findAll('tr', attrs={'class':['odd', 'even']})

		for tldrank, tr in enumerate(trs):
			tds = tr.findAll('td')
			domain = tds[2].select('a.domainname')[0].text
			rank = tds[0].select('span')[0].text
			tldrank = str(tldrank + 1 + page).zfill(3)
			
			print('[' + tldrank + '] #' + rank + ' ' + domain)
	except:
		pass

for i in range(0, args.max, 100):
	getThem(args.tld, i)