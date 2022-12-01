import sys
import os
import hashlib
import json
import webbrowser

NUM_BUCKETS1 = 20
NUM_BUCKETS2 = 20
root = "."

def main():
    global root
    url = sys.argv[1]
    root = sys.argv[2]
    if url.startswith("gr://"):
        expand_url(url)
    else:
        shorten_url(url)

def expand_url(url):
    id = "gr://".join(url.split("gr://")[1:])
    jsonpath = get_json_path(id)
    with open(jsonpath,"r") as f:
        file_content = f.read()
        if file_content and file_content != '{}':
            url_bucket = json.loads(file_content)
            if id in url_bucket.keys():
                webbrowser.open(url_bucket[id], new=0, autoraise=True)
                return
    print(f'Invalid Url: {url}') 
    
def shorten_url(url):
    id = generate_id_for_long_url(url)
    jsonpath = get_json_path(id)
    url_bucket = {}
    with open(jsonpath,"r") as f:
        file_content = f.read()
        if not file_content and file_content == '{}':
            print(file_content)
            url_bucket = json.loads(f.read())
    url_bucket[id] = url
    with open(jsonpath,"w") as f:
        json.dump(url_bucket, f)
    print(f'shortened the url.. {url}: gr://{id}')
    return f'gr://{id}'

def generate_id_for_long_url(url):
    return str(hashlib.sha256(url.encode('utf-8')).hexdigest())[:8]

def get_json_path(id):
    b1 = str(int(hashlib.sha256(id.encode('utf-8')).hexdigest(), 16) % NUM_BUCKETS1)
    b2 = str(int(hashlib.sha256(f'0_0{id}'.encode('utf-8')).hexdigest(), 16) % NUM_BUCKETS2)
    b1_path = f'{root}/urls/{b1}'
    if not os.path.exists(b1_path):
        os.mkdir(b1_path)
    jsonfile = f'{root}/urls/{b1}/{b2}'
    if not os.path.exists(jsonfile):
        with open(jsonfile,"w") as f:
            json.dump({}, f)
    return jsonfile

main()