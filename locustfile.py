from locust import HttpUser, task, between
import logging

class SearchUser(HttpUser):
    wait_time = between(1, 3)
    MAX_RESPONSE_TIME_MS = 1000
    host = "https://www.n11.com"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    SEARCH_KEYWORDS = ["klima", "iphone", "buzdolabi", "televizyon", "airfryer"]

    @task
    def search_keywords(self):
        for keyword in self.SEARCH_KEYWORDS:
            self.perform_search(keyword)

    def perform_search(self, keyword):
        with self.client.get(f"/arama?q={keyword}", headers=self.headers, catch_response=True) as response:
            errors = []

            if not 200 <= response.status_code < 300:
                errors.append(f"Status code: {response.status_code}")

            if keyword.lower() not in response.text.lower():
                errors.append(f"Keyword '{keyword}' not found in response")

            elapsed_ms = response.elapsed.total_seconds() * 1000
            if elapsed_ms > self.MAX_RESPONSE_TIME_MS:
                errors.append(f"Slow response: {elapsed_ms:.2f} ms")

            if errors:
                response.failure(" | ".join(errors))
                logging.warning(f"[{keyword}] FAILED → " + " | ".join(errors))
            else:
                response.success()
                logging.info(f"[{keyword}] OK ({elapsed_ms:.2f} ms)")