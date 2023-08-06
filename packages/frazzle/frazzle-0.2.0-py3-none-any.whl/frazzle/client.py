import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument("course", help="The course number you are taking.")
parser.add_argument("lab", help="The lab number.")
parser.add_argument(
    "part", help="The part number of the assignment to get a hint for.")
parser.add_argument(
    "source", help="The name of the source file to get a hint for.")
parser.add_argument("question", help="The question to ask Prof. Frazzle.")

args = parser.parse_args()

with open(args.source, "r") as f:
    source = f.read()
    
# construct json
api_request = {
    "course": int(args.course),
    "lab": int(args.lab),
    "part": int(args.part),
    "code":source,
    "question": args.question,
}

cloud_function_url = "https://us-central1-frazzle.cloudfunctions.net/frazzle-hinty"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post(cloud_function_url, data=json.dumps(api_request), headers=headers)

if response.status_code == 200:
    feedback = response.text
else:
    feedback = "Error: " + response.text

print(feedback)
