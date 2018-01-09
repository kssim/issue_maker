# -*- coding: utf-8 -*-

import json
import requests

from mod_python import apache
from issue_maker import IssueMaker

def parser(text):
    ret = text.split("\n")
    title = ("%s" % ret[0])
    content = ("%s" % "\n".join(ret[1:]))
    return (title, content)

def handler(request, response_url, text):
    req.content_type = "application/json"

    payload = {"response_url":response_url, "text":text}
    try:
        requests.post("[URL of delay_reponse_handler]", data=payload, timeout=0.5)
    except:
        return {"text":"After a while, it will be done."}

    return {"text":"It's done."}

def delay_response_handler(request, response_url, text):
    url_of_created_issue = open_issueu(text)

    headers = {"Content-Type":"application/json"}
    payload = {"text":url_of_created_issue, "response_type":"[in_channel or ephemeral]"}

    requests.post(response_url, headers=headers, data=json.dumps(payload))

def open_issue(text):
    title, content = parser(text)
    issue = IssueMaker()
    return issue.create_issue(title, content)
