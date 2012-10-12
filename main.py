#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2012 Russell <russell@russell-Satellite-Pro-L630>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
exceptions = ['is', 'are', 'a', 'an', 'the']

def sort_keys(d):
	keys = sorted(insults, key=d.__getitem__, reverse=True)
	

def train_data():
	import csv
	csv_data = csv.reader(open('train.csv'), delimiter=",", quotechar='"')
	dict_data = [row for row in csv_data]
	return dict_data

def break_text(data):
	import re
	new_data = []
	for item in data:
		if item[0] == '1':
			text = item[2]
			new_data.append([word.lower().strip() for word in re.split('\W+', text) if not word ==''])
	return new_data
	
def hist(data, keys):
	hist_val = len(filter(lambda item: any(x in item for x in keys), data))
	return {keys:hist_val}
			

def train(data):
	hist_dict = {}
	for row in data:
		for item in row:
			if item not in hist_dict.keys():
				hist_dict.update(hist(data, item))
	return hist_dict

def main():
	data = train_data()
	new_data = break_text(data)
	insults = train(new_data)
	keys = sorted(insults, key=insults.__getitem__, reverse=True)
	for k in keys[:100]:
		print insults[k],'\t',k
	return 0

if __name__ == '__main__':
	main()

