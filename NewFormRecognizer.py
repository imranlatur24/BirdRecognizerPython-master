########### Python 3.2 #############
import http.client,\
    urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '74baf1f73c244ea9ad88fc00eccaba56',
}

params = urllib.parse.urlencode({
    # Request parameters
    'includeTextDetails': 'true',
    'locale': 'en',
})

try:
    conn = http.client.HTTPSConnection('https://pancarddemo.cognitiveservices.azure.com/')
    conn.request("POST", "/formrecognizer/v2.1-preview.1/prebuilt/businessCard/analyze?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))