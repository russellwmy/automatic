'''
Created on 27 Sep, 2012

@author: russell wong (russellwmy@gmail.com)
'''

import csv
import os.path
import sys
from checkbox.properties import Path

def main(primay_lang, fp,output='locale'):
    if os.path.exists(fp):
        generate(primay_lang,fp,output)
    else:
        print 'File does not exists'
def gen_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        
def generate(primay_lang, fp, output):
    with open(fp, 'rb') as csvfile:
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')
        data = []
        for row in rows:
            data.append(row)
        langs = []
        lang_data = data[0]
        msg_data = data[1:]
        for item in lang_data:
            langs.append(item)
        key_idx = langs.index(primay_lang)
        langs_po = {}
            
        for i , lang in enumerate(langs):
            if i != key_idx:
                langs_po[lang] = []
                for msg in msg_data:
                    msgid = msg[key_idx]
                    msgstr = msg[i]
                    langs_po[lang].append((msgid, msgstr))
        for lang, msgs in langs_po.items():
            path = os.path.join(output, lang,'LC_MESSAGES')
            gen_dir(path)
            path = os.path.join(path,'default.po')
            lang_fp = open(path, 'w+')
            for msg in msgs:
                if len(msg) == 2:
                    msgid_fmt = 'msgid "%s"\n'
                    msgstr_fmt = 'msgstr "%s"\n'
                    lang_fp.write(msgid_fmt % (msg[0]))
                    lang_fp.write(msgstr_fmt % (msg[1]))
                    lang_fp.write('\n')
            lang_fp.close()
            
if __name__ == '__main__':
    
    args = sys.argv
    if len(args) > 2:
        main(args[1], args[2])
    else:
        help_str = """csv2po - created by Russell Wong (russellwmy@gmail.com) 27 Sep 2012
        
usage:
    csv2po.py [primary] [file]    convert the csv into po files
    
examples:
    csv2po.py en_US locales.csv"""
    
        print help_str
        
