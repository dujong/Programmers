import re

def solution(new_id):

    new_id = new_id.lower()
    new_id = re.sub('[^a-z\d\-\_\.]', '', new_id)
    new_id = re.sub('\.\.+', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)

    if new_id == '':
        new_id = 'a'
    
    new_id = re.sub('\.$', '', new_id[0:15])

    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id


a =  "123_.def"
a = solution(a)
print(a)