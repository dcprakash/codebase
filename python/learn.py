import getopt
import os
import sys
import requests
import subprocess
import time
import socket
import json
import random
import glob
import shutil
import zipfile
import logging

logging.basicConfig(filename='/Users/dprakash/Documents/Git/codebase/python/learn.log',
                    level=logging.INFO)


def parse_url(url):
    response = requests.get("".join(["https://", url]))
    if response.status_code == 200:
        domain = socket.gethostbyname(url)
        try:
            proc = subprocess.Popen(["traceroute", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(3)
            proc.kill()
            out, err = proc.communicate()
            logging.info(out)
            logging.info(err)
        except Exception as e:
            print("Error {}".format(e))
            proc.kill()


def parse_file(file):
    with open(file, "r") as f:
        list_data = [word.strip('\n') for word in f.readlines()]
        print("List data \n {}".format(list_data))
        f.close()

    with open(file, "r") as f:
        string_data = f.read()
        print("\n String data {}".format(string_data))
        f.close()

    with open(file, "r") as f:
        print("\n Redline")
        for line in f:
            print(line, end="")


def parse_dir(dir):
    results = {}
    for root, dirs, files in os.walk(dir):
        for name in files:
            print(os.path.join(root,name))
        for name in dirs:
            print(os.path.join(root,name))
        for file in files:
            with open(os.path.join(root, file), "r") as f:
                data = f.read()
                results.update({os.path.join(root, file): data})
    print(results)


def parse_metadata(json_path):
    dependent_services = []
    metadata = json.loads(open('/Users/dprakash/Documents/IDA/Cloud9/1IDA/LocalCode/content/metadata.json').read())
    for i,(k, v) in enumerate(metadata.items()):
        if k == "api_dependencies" and isinstance(v, list):
            for idx in v:
                dependent_services.append(idx["name"])
    print("Dependent services are {}".format(dependent_services))


def generate_file():
    data = [word.strip('\n') for word in open('/Users/dprakash/Documents/IDA/Cloud9/1IDA/LocalCode/content/randomWords.txt', "r").readlines()]
    count = 10
    for i in range(1, count+1):
        amount = random.uniform(1.0, 1000.0)
        content = {
            'topic': random.choice(data),
            'amount': amount
        }
        with open('/Users/dprakash/Documents/IDA/Cloud9/1IDA/LocalCode/content/files/receipts-%s.json' %i, "w") as f:
            json.dump(content, f)
    print("Completed creating files")


# reads only json file []0-9, get the amount and move file to processed dir (create process dir if not exist)
# to re-run this method, delete files from processed; create files using generate_file method
def process_file():
    logging.info("\n \n processing files")
    try:
        os.mkdir('/Users/dprakash/Documents/Git/codebase/python/test')
    except OSError as e:
        print("Error creating dir {}".format(e))

    receipt_files = glob.glob('/Users/dprakash/Documents/Git/codebase/python/test/receipts/receipts-[0-4].json')
    subtotal = 0
    for file in receipt_files:
        data = json.loads(open(file, "r").read())
        subtotal += float(data['amount'])
        dest_file_name = file.split('/')[-1]
        destination_path = '/Users/dprakash/Documents/Git/codebase/python/test/receipts/processed/%s' % dest_file_name
        shutil.move(file, destination_path)
        logging.info("Moved file from {} to {}".format(file, destination_path))
    print("Total amount {}".format(subtotal))


def zip_processed_file():
    # file_list = glob.glob('/Users/dprakash/Documents/IDA/Cloud9/1IDA/LocalCode/content/processed/receipts-[0-9]*.json')
    # file_list.extend(glob.glob('/Users/dprakash/Documents/IDA/Cloud9/1IDA/LocalCode/content/Test/**/*.txt', recursive=True))

    file_list = []
    base_dir = '/Users/dprakash/Documents/Git/codebase/python/test/receipts/processed/'
    z = zipfile.ZipFile("".join([base_dir, "processed.zip"]), "w")
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if os.path.join(root, f).endswith(".txt") or os.path.join(root, f).endswith(".json"):
                file_list.append(os.path.join(root, f))
                z.write(os.path.join(root, f), os.path.join(root, f).split('/')[-1])
    z.close()
    print(file_list)


if __name__=='__main__':
    url = "www.bbc.com"
    file_path = "/Users/dprakash/Documents/Git/codebase/python/test/file1.txt"
    dir_path = "/Users/dprakash/Documents/Git/codebase/python/test"
    json_path = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:u:f:d:", ["help=", "url=", "file=", "dir="])
        print(opts)
        print(args)
        
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print("Usage Help: -u url -f file_path")
            elif opt in ("-u", "--url"):
                url = arg
            elif opt in ("-f", "--file"):
                file_path = arg
            elif opt in ("-d", "--dir"):
                dir_path = arg
            elif opt in ("-j", "--json"):
                json_path = arg
    except getopt.error as e:
        print("Error: {}".format(e))

    # parse_url(url)
    # parse_file(file_path)
    # parse_dir(dir_path)
    # parse_metadata(json_path)
    # generate_file()
    # process_file()
    zip_processed_file()
    # pro_file()