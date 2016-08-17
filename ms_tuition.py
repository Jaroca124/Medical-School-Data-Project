import urllib2
from bs4 import BeautifulSoup

f = open('med_data.txt', 'w')

timestamp = str(1997)

# Make School Dictionary
school_dictionary_loaded = False
school_dict = {}

for y in range(0,19):
	current_year = 1997 + y
	timestamp = str(current_year)
	print "Getting data for " + timestamp
	url = 'https://services.aamc.org/tsfreports/report.cfm?select_control=PUB&year_of_study=' + timestamp
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)

	line = soup.findAll('tr')

	# For Each School in the List
	for m in range(9,len(line) - 1):
		prep = str(line[m]).split('<td>')
		if len(prep) > 2:
			prep = str(prep[1]) + str(prep[2])
		else:
			prep = str(prep[1])
		school_info = prep.replace('\n', '').replace('\t', '').replace('</td>', '').replace('</tr>','').split('<td align="right">')
		school_name = school_info[0]
		load = school_info[len(school_info) - 2]
		if (load == '<span class="footnote">NA</span>'):
				load = 'NA'
		print "Loading: " + school_name + ' - ' + load
		
		if (school_name in school_dict):
			school_dict[school_name].append(load)
			
		else:
			school_dict[school_name] = [load]

for keys in school_dict:
	f.write(keys + '\t')
	for m in range(0, len(school_dict[keys])):
		f.write(school_dict[keys][m] + '\t')
	f.write('\n')
f.close()