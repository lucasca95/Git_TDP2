import http.client
import urllib
import pytest
import os

def test_start_match():
    port = int(os.getenv("FLASK_RUN_PORT")) if os.getenv("FLASK_RUN_PORT") != None else 8888
    conn = http.client.HTTPConnection('localhost',port)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    params = urllib.parse.urlencode( {
        "team1":1,
        "team2":2,
        "place":"LP"
    })
    conn.request("GET", "/start_match", params, headers)
    response = conn.getresponse()
    conn.close()
    assert response.status == 200

def test_stop_match():
    port = int(os.getenv("FLASK_RUN_PORT")) if os.getenv("FLASK_RUN_PORT") != None else 8888
    conn = http.client.HTTPConnection('localhost',port)
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn.request("GET", "/stop_match", headers=headers)
    response = conn.getresponse()
    conn.close()
    assert response.status == 200