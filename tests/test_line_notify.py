import sys
sys.path.append('.')

import requests_mock
from urllib.parse import urljoin

from src.line_notify.line_notify import LineNotify

def test_getting_api_status():
    """
    should get a dict response
    """
    LINE_NOTIFY_BASE_URL = 'https://notify-api.line.me'
    endpoint_api_status = '/api/status'
    LINE_STATUS_URL = urljoin(LINE_NOTIFY_BASE_URL, endpoint_api_status)

    with requests_mock.mock() as m:
        stub_json = {
            'status': 200,
            'message': 'ok',
            'targetType': 'USER',
            'target': 'someName'
        }
        m.get(LINE_STATUS_URL, json=stub_json)
        line = LineNotify()
        status = line.get_api_status()
        print(status)

        assert isinstance(status, dict)
        assert 'status_code' in status
        assert 'body' in status
        assert status['status_code'] == 200
        assert status['body']['message'] == 'ok'
