# DOCKER-WEB_HONEYPOT
# Web Honeypot (Flask)

A simple low-interaction web honeypot built with Python and Flask to log suspicious login and search attempts.  
This project is for educational and research purposes only.

---

## Features
- Fake login page that captures:
  - Username
  - Password
  - IP address
  - User-Agent
- Fake search page that captures:
  - Search query
  - IP address
  - User-Agent
- Logs all activity to `honeypot.log`
- Easy to run with Python or Docker

- ## Installation & Setup
  1. Make a folder and clone the repository**
  2. cd that folder in docker.
  3. Build the docker image.
  4. you can either push that image into dockerhub or run it directly.
  5. make a container and run it.
 
- **Usage**

Login page: http://localhost:5000/login

Search page: http://localhost:5000/search?q=test 

**you can check the log by : 

docker exec -it {docker container name} cat honeypot.log**



**Example Log Entry** : 

2025-08-15 18:34:12,456 - Login attempt - Username: admin, Password: 12345, IP: 192.168.1.10



**Disclaimer**

⚠ This honeypot is intended for educational and research purposes only.
  Do not deploy it on production networks without permission.
  The author is not responsible for any misuse of this code.
