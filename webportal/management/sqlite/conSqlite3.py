import sqlite3
import re
from json import loads

con = sqlite3.connect('db.sqlite3', check_same_thread=False)

modelsRegexs = [r'person', r'user', r'people', r'customer', r'pessoa', r'usuario', r'cliente']
sensitiveRegexs = [r'sindicato', r'religiao']
fieldsRegexs = [r'name', r'age', r'sex', r'birth', r'doc', r'email', r'phone', r'address', r'city', r'password', r'passwd', r'pwd', r'pass', r'sindicato', r'religiao',r'senha']

def getModels():
    cur = con.cursor()
    cur.execute('SELECT name FROM sqlite_master')
    rows = cur.fetchall()
    matchingModels = []
    for keyword in modelsRegexs:
        for row in rows:
            if re.findall(f"(?i){keyword}", row[0]):
                matchingModels.append(row[0])
    return matchingModels

def getFields(models_):
    matches = []
    for model in models_:
        try:    
            cur = con.cursor()
            cur.execute('SELECT * FROM {}'.format(model))
            fields =  [member[0] for member in cur.description]
            validFields = []
            problem = False
            for keyword in fieldsRegexs:
                for field in fields:
                    if re.findall("(?i){}".format(keyword), field):
                        validFields.append({'field': field, 'status': validateData(model, field)})
                        if validateData(model,field) != 'OK':
                            problem = True
            if len(validFields) > 0:
                matches.append({'model': model, 'fields': validFields, 'problem': problem})
        except Exception as e:
            pass
    return matches

def validateData(model, field):
    passwd = r'(?i)(password|passwd|pwd|pass|senha)'
    sensitive = r'(?i)(sindicato|religiao|deficiencia|opcaosexual|biometria)'
    status = 'OK'
    if re.findall(passwd, field):
        try:
            cur = con.cursor()
            cur.execute(f'SELECT {field} from {model}')
            value = cur.fetchone()[0]
            if len(value) < 32:
                status = 'Senha salva em plaintext'
            if not re.match(r'[a-f0-9]', value):
                status = 'Senha salva em plaintext'
            if re.match(r'^pbkdf2_sha256', value):
                status = 'OK'
        except Exception as e:
            print(e)
    if re.findall(sensitive, field):
        status = 'Dado sensível'
    else:
        print(field)

    return status