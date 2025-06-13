# N11 Load Testing Project

A lightweight Locust-based load test for the search functionality of [n11.com](https://www.n11.com).

## Overview

Simulates a user searching for keywords (e.g. "iphone") and validates:
- HTTP status code
- Response time (max 2000ms)
- Presence of the search keyword in the response

## Requirements

- Python 3.9+
- Locust (`pip install locust`)

## Configuration

- Wait time: 1–3 seconds between requests  
- Max response time: 2000ms  
- Custom headers (e.g. User-Agent)

## Running the Test

```bash
locust -f locustfile.py
```

Then open [http://localhost:8089](http://localhost:8089) to configure:
- Number of users  
- Spawn rate  
- Target host (e.g. https://www.n11.com)

## Logging & Validation

- Logs failures, slow responses, and success status  
- Ensures functional accuracy and basic performance