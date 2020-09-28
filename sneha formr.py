########### Python Form Recognizer Async Receipt #############

import json
import time
from requests import get, post

# Endpoint URL
endpoint = r"https://pancarddemo.cognitiveservices.azure.com/"
apim_key = "74baf1f73c244ea9ad88fc00eccaba56"
post_url = endpoint + "/formrecognizer/v2.0/prebuilt/receipt/analyze"
source = r"cosmos.jpg"

headers = {
    # Request headerso
    'Content-Type': 'image/jpeg',
    'Ocp-Apim-Subscription-Key': apim_key,
}

params = {
    "includeTextDetails": True
}

with open(source, "rb") as f:
    data_bytes = f.read()

try:
    resp = post(url=post_url, data=data_bytes, headers=headers, params=params)
    if resp.status_code != 202:
        print("POST analyze failed:\n%s" % resp.text)
        quit()
    print("POST analyze succeeded:\n%s" % resp.headers)
    get_url = resp.headers["operation-location"]
except Exception as e:
    print("POST analyze failed:\n%s" % str(e))
    #quit()


#new code here
n_tries = 10
n_try = 0
wait_sec = 6
while n_try < n_tries:
    try:
        resp = get(url = get_url, headers = {"Ocp-Apim-Subscription-Key": apim_key})
        resp_json = json.loads(resp.text)
        if resp.status_code != 200:
            print("GET Receipt results failed:\n%s" % resp_json)
            quit()
        status = resp_json["status"]
        if status == "succeeded":
            print("Receipt Analysis succeeded:\n%s" % resp_json)
            quit()
        if status == "failed":
            print("Analysis failed:\n%s" % resp_json)
            quit()
        # Analysis still running. Wait and retry.
        time.sleep(wait_sec)
        n_try += 1
    except Exception as e:
        msg = "GET analyze results failed:\n%s" % str(e)
        print(msg)
        quit()

