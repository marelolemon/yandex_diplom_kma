import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
def get_order_by_track_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" + str(track),
                        headers=data.headers)
# Мария Клыкова, 1-я когорта — Финальный проект. Инженер по тестированию плюс
def test_get_created_order():
    create_order_response = post_new_order(data.order_body)
    track_number = create_order_response.json()["track"]
    get_order_response = get_order_by_track_number(track_number)
    assert get_order_response.status_code == 200
