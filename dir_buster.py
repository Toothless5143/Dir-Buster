import argparse
import requests

def directory_buster(url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            word = line.strip()
            full_url = url + '/' + word
            response = requests.get(full_url)

            if response.status_code == 200:
                print('[+] Found: {}'.format(full_url))

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Directory Buster')
parser.add_argument('-u', '--url', help='Target URL', required=True)
parser.add_argument('-w', '--wordlist', help='Wordlist file', required=True)
args = parser.parse_args()

# Execute directory buster
directory_buster(args.url, args.wordlist)
