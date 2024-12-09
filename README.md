# Performance Testing Tutorial

This repository demonstrates how to set up and perform performance testing for a sample application using tools like Locust and Docker.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup and Running the Application](#setup-and-running-the-application)
- [Performing Load Tests](#performing-load-tests)
- [Monitoring the Application](#monitoring-the-application)
- [Reference Links](#reference-links)

---

## Overview

This project serves as a tutorial for performance testing using Locust. The tutorial demonstrates:
- Setting up a simple application with Docker Compose.
- Running performance tests.
- Monitoring application performance.

---

## Prerequisites

Before starting, ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Python 3.7+](https://www.python.org/)
- Pip (Python package manager)

---

## Setup and Running the Application

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd performance-testing-tutorial
   ```

2. Build and start the application using Docker Compose:
   ```bash
   docker compose up -d --build
   ```

3. Verify the application is running by making a POST request:
   ```bash
   curl -X POST http://127.0.0.1:5000/search -H "Content-Type: text/plain" -d 'sample_query'
   ```

---

## Performing Load Tests

1. Navigate to the `loadtest` directory:
   ```bash
   cd loadtest
   ```

2. Install required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run Locust to start performance testing:
   ```bash
   locust -f main.py
   ```

4. Open the Locust web interface at [http://localhost:8089](http://localhost:8089) to configure and execute load tests.

---

## Monitoring the Application

1. Monitoring stack will be deployed together with the main docker compose file. Monitoring stack is maintained at [docker-compose.monitoring.yml](./docker-compose.monitoring.yml)

2. Access monitoring dashboards:
   - Grafana: [http://localhost:3000](http://localhost:3000)

---

## Reference Links

- [Locust Documentation](https://docs.locust.io/en/stable/)
- [P99 Latency Explained](https://www.baeldung.com/cs/whats-the-p99-latency)
- [Processes vs. Threads](https://www.baeldung.com/linux/process-vs-thread)
- [Docker compose](https://docs.docker.com/reference/compose-file/services/#simple-example)
- [GIL](https://realpython.com/python-gil/)

---

## Contributing

Feel free to contribute by opening issues or submitting pull requests.
