import pytest

def test_endpoint_ok(client):

	data = {
		"address": {
			"colorKeys": ["A", "G", "Z"],
			"values": [74, 117, 115, 116, 79, 110]
		},
		"meta": {
			"digits": 33,
			"processingPattern": "d{5}+[a-z&$§]"
		}
	}	
	
	response = client.post("/compute_sum", json  = data, content_type="Application/Json")
	assert response.status == "200 OK"
	assert response.get_json().get("result")  == 611

def test_missing_field_colorKeys(client):
	
	data = {
		"address": {
			"values": [74, 117, 115, 116, 79, 110]
		},
		"meta": {
			"digits": 33,
			"processingPattern": "d{5}+[a-z&$§]"
		}
	}	
	
	response = client.post("/compute_sum", json  = data, content_type="Application/Json")
	assert response.status == "200 OK"
	assert response.get_json().get("result")  == 611

def test_missing_field_meta(client):

	data = {
		"address": {
			"colorKeys": ["A", "G", "Z"],
			"values": [74, 117, 115, 116, 79, 110]
		}
	}	
	
	response = client.post("/compute_sum", json  = data, content_type="Application/Json")
	assert response.status == "200 OK"
	assert response.get_json().get("result")  == 611


def test_empty_list(client):
	
	data = {
		"address": {
			"colorKeys": ["A", "G", "Z"],
			"values": []
		},
		"meta": {
			"digits": 33,
			"processingPattern": "d{5}+[a-z&$§]"
		}
	}	
	
	response = client.post("/compute_sum", json  = data, content_type="Application/Json")
	assert response.status == "200 OK"
	assert response.get_json().get("result")  == 0 

def test_missing_address_field(client):

	data = {
		"meta": {
			"digits": 33,
			"processingPattern": "d{5}+[a-z&$§]"
		}
	}	
	
	response = client.post("/compute_sum", json  = data, content_type="Application/Json")
	assert response.status_code == 400
