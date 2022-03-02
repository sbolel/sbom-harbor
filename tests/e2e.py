import requests
import importlib.resources as pr
import tests.sboms as sboms
from json import loads

INVOKE_URL = 'https://bqetkv0bbh.execute-api.us-east-1.amazonaws.com/prod/store'
SAAS_BOM = loads(pr.read_text(sboms, "SaasBOM.json"))
BIG_BOM = loads(pr.read_text(sboms, "keycloak.json"))

def post_test():

    print("Sending To: %s" % INVOKE_URL)
    print("<SaasBOM>")
    print(SAAS_BOM)
    print("</SaasBOM>")

    rsp = requests.post(INVOKE_URL, json=SAAS_BOM)
    print(rsp.text)

    print("Sending To: %s" % INVOKE_URL)
    print("<BigBOM>")
    print(BIG_BOM)
    print("</BigBOM>")

    rsp = requests.post(INVOKE_URL, json=BIG_BOM)
    print(rsp.text)