import my_code

api_url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=DEMO_KEY"

def test_getresponse():
    ret = my_code.get_response(api_url)
    assert ret.status_code == 200

def test_sum():
    assert 3 == 3