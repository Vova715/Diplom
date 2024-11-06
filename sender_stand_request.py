import configuration
import requests
import data

def post_new_order(order_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = order_body,
	                     headers = data.headers)

def get_order_from_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACK_PATH + str(track),
	                    headers = data.headers)

def assertion_code_200():
	response_pno = post_new_order(data.order_body)
	track = response_pno.json()["track"]
	return get_order_from_track(track).status_code

def test_get_order_from_track_code_200():
	assert assertion_code_200() == data.status_code_200