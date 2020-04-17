import sys
sys.path.append('.')

from src.line_notify import LineNotify

def test_getting_api_status():
    """
    should get a dict response
    """
    
    line = LineNotify()
    status = line.get_api_status()
    assert isinstance(status, dict)
    assert 'status_code' in status
    assert 'body' in status
    assert status['status_code'] == 200
    assert status['body']['message'] == 'ok'
