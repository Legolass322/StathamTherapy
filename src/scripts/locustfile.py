from locust import HttpUser, task, between

class Statham(HttpUser):
    wait_time = between(1, 5)
    
    access_token = None

    @task
    def me(self):
        self.client.get("/api/auth/me", headers={
            "Authorization": f"Bearer {self.access_token}"
        })

    def on_start(self):
        r = self.client.post("/api/auth/login", json={"username":"Statham", "password":"AlphaSigma"})
        self.access_token = r.json()["access_token"]
