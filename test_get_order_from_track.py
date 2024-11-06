# Владимир Пальянов, 23-я когорта — Диплом. Инженер по тестированию плюс
import data
import sender_stand_request



def assertion_code_200():
	response_pno = sender_stand_request.post_new_order(data.order_body)
	track = response_pno.json()["track"]
	return sender_stand_request.get_order_from_track(track).status_code


def test_get_order_from_track_code_200():
	assert assertion_code_200() == data.status_code