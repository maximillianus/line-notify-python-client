import os
import json
from urllib.parse import urljoin

import requests
from dotenv import load_dotenv
load_dotenv()

from src.config import LINE_NOTIFY_BASE_URL


class LineNotify:
    def __init__(self):
        self.ACCESS_TOKEN=os.getenv('LINE_NOTIFY_API_TOKEN', '')
        self.headers = {
            'Authorization' : f'Bearer {self.ACCESS_TOKEN}'
        }
        self.LINE_NOTIFY_BASE_URL = 'https://notify-api.line.me'
        endpoint_api_notify = '/api/notify'
        endpoint_api_status = '/api/status'
        self.LINE_NOTIFY_URL = urljoin(self.LINE_NOTIFY_BASE_URL, endpoint_api_notify)
        self.LINE_STATUS_URL = urljoin(self.LINE_NOTIFY_BASE_URL, endpoint_api_status)

        self.sess = requests.Session()
        self.sess.headers.update(self.headers)
    
    def send_notification(self, payload):
        r = self.sess.post(
            url=self.LINE_NOTIFY_URL,
            data=payload)
        if r.status_code == 200:
            print(r.json())
        else:
            print('HTTP Error during sending message')
        pass
    
    def get_api_status(self):
        r = self.sess.get(self.LINE_STATUS_URL)
        resp = {
            'status_code': r.status_code,
            'body': r.json()
        }
        return resp

def main():
    line = LineNotify()
    # line.get_api_status()
    msg = {'hello': 'world'}
    if isinstance(msg, dict):
        msg = json.dumps(msg)
    payload = {
        'message': msg,
        'stickerPackageId': 1,
        'stickerId': 11
    }
    line.get_api_status()
    line.send_notification(payload)

if __name__ == "__main__":
    main()