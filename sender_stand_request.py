import requests
import configuration
import data


def post_new_order(order_body):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = order_body,
	                     headers = data.headers)


def get_order_from_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACK_PATH + str(track),
	                    headers = data.headers)