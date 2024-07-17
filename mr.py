import requests
import json
import time
import datetime

def read_tokens(file_path):
    with open(file_path, 'r') as file:
        tokens = file.read().splitlines()
    return tokens

def claim(token, account_number):
    url = "https://mirrionbeyond.com/api/main"
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        "act": "claim",
        "token": token
    }
    response = requests.post(url, headers=headers, json=payload)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if response.status_code == 200:
        print(f"Successfully claimed for account {account_number} on {current_time}")
    else:
        print(f"Failed to claim for account {account_number} on {current_time}, Status Code: {response.status_code}")

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Countdown: {timeformat}", end='\r')
        time.sleep(1)
        seconds -= 1

def main():
    tokens = read_tokens('data.txt')
    total_accounts = len(tokens)
    print(f"Total accounts: {total_accounts}")

    for index, token in enumerate(tokens):
        print(f"Processing account {index + 1} of {total_accounts}")
        claim(token, index + 1)
        print(f"Waiting for 5 seconds before switching to the next account...")
        time.sleep(5)
    
    print("All accounts have been processed. Starting 1-hour countdown.")
    countdown_timer(3600)
    print("Restarting the process...")
    main()

if __name__ == "__main__":
    main()
