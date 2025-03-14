import requests


class TestPets:
    
    #URL for swagger API Pets
    base_url = "https://petstore.swagger.io/v2"
    #Json Data for Pet requests
    pet_data = {
        "id": 122,
        "name": "patricio",
        "photoUrls": [],
        "tags": [],
        "status": "available"
    }

    def test_post_pet(self):
        #Send POST Request 
        response = requests.post(f"{self.base_url}/pet", json=self.pet_data)

        # ASSERTIONS
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["id"] == self.pet_data["id"]
        assert response_data["name"] == self.pet_data["name"]
        assert response_data["status"] == self.pet_data["status"]

    def test_get_pet(self):
        # Send GET Request
        response = requests.get(f"{self.base_url}/pet/{self.pet_data['id']}")
        # ASSERTIONS
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['id'] == self.pet_data['id']
        assert response_data["name"] == self.pet_data["name"]
        assert response_data["status"] == self.pet_data["status"]

    def test_update_pet(self):
        #New data modified pet
        pet_new_data = {
        "id": 122,
        "name": "zeus",
        "photoUrls": [],
        "tags": [],
        "status": "sold"
        }
        #Send PUT Request
        response = requests.put(f"{self.base_url}/pet",json=pet_new_data)

        #ASSERTIONS 
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['id'] == pet_new_data['id']
        assert response_data["name"] == pet_new_data["name"]
        assert response_data["status"] == pet_new_data["status"]

    def test_delete_pet(self):
        #Send Delete request
        response = requests.delete(f"{self.base_url}/pet/{self.pet_data['id']}")

        #ASSERTIONS
        assert response.status_code == 200