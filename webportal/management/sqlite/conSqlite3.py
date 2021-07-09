import sqlite3
import re

con = sqlite3.connect('db.sqlite3')

modelsRegexs = ['person', 'user', 'people', 'customer', 'pessoa', 'usuario', 'cliente']
fieldsRegexs = ['name', 'age', 'sex', 'birth', 'doc', 'email', 'phone', 'address', 'city']

def cleanStr(raw):
    rClean = str(raw).replace('(', '')
    rClean = str(rClean).replace(')', '')
    rClean = str(rClean).replace(',', '')
    rClean = str(rClean).replace('\'', '')
    return rClean

def getModels():
    cur = con.cursor()
    cur.execute('SELECT name FROM sqlite_master')
    rows = cur.fetchall()
    matchingModels = []
    for mrgx in modelsRegexs:    
        for r in rows:
            if re.findall("{}*".format(mrgx), cleanStr(r)):
                matchingModels.append(cleanStr(r))
    return matchingModels

def getFields(models):
    matchingFields = []
    try:
        for m in models:
            cur = con.cursor()
            cur.execute('SELECT * FROM {}'.format(m))
            rows = cur.fetchall()
            for frgx in fieldsRegexs:
                for r in rows:
                    if re.findall("{}*".format(frgx), cleanStr(r)):
                        matchingFields.append(cleanStr(r))
    except Exception as e:
        print('[!] Error: {}\n'.format(e))
    return matchingFields