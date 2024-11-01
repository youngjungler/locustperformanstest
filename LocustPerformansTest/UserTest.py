from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def user_create(self):
        payload = {
            "id": 249897,
            "username": "denemekullanici",
            "firstName": "deneme",
            "lastName": "kullanici",
            "email": "denemekullanici@gmail.com",
            "password": "123456789",
            "phone": "5362264319",
            "userStatus": 0
        }
        self.client.post("/v2/user", json=payload)

    @task
    def user_update(self):
        payload = {
            "id": 24985,
            "username": "guncelkullanici",
            "firstName": "guncel",
            "lastName": "kullanici",
            "email": "guncelkullanici@gmail.com",
            "password": "123456",
            "phone": "5452126585",
            "userStatus": 0
        }
        self.client.put("/v2/user/denemekullanici", json=payload)

    @task
    def get_user_info(self):
        self.client.get("/v2/user/denemekullanici")

    @task
    def user_delete(self):
        self.client.delete("/v2/user/denemekullanici")
