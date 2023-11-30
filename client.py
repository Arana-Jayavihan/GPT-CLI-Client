import requests
import json
import argparse

def ask(prompt):
    data = f'{{"messages": [ {{ "role": "system", "content": "Below is an instruction that describes a task. Write a response that appropriately completes the request." }},{{ "role": "user", "content": "{prompt}"}}], "temperature": "0.7","max_tokens": "-1","stream": "false"}}'
    result = requests.post(url, headers=headers, data=data)
    return json.loads(result.text)["choices"][0]["message"]["content"]

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', type=str, required=True, help="Host Address")
args = parser.parse_args()

url = f"http://{args.addr}/v1/chat/completions"
headers = {'Content-Type': 'application/json'}

while True:
    prompt = input("[+] Message : ")
    reply = ask(prompt)
    print(f'[+] Mistral :{reply}')

