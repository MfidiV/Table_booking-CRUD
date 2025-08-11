# Table Booking App Deployment Guide

This guide explains how to deploy the **Table Booking App** on a Linux server (Ubuntu/Debian) using **Gunicorn** as the WSGI server and **Nginx** as a reverse proxy.

---

## Prerequisites

- A Linux server (Ubuntu/Debian recommended)  
- Python 3 installed  
- Nginx installed (`sudo apt install nginx -y`)  
- Virtual environment created and activated  
- Project dependencies installed (`pip install -r requirements.txt`)

---

## Step 1: Update System and Install Dependencies

Update your package list and install Nginx, Python3 pip, and venv:

```
sudo apt update
sudo apt install nginx -y
sudo apt install python3-pip python3-venv -y
```
## Step 2: Set Up Python Environment and Install Project Dependencies

Create and activate a virtual environment, then install the required Python packages:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Step 3: Create a .env File for Environment Variables

Create a .env file to store sensitive information such as database credentials and secret keys:
```
touch .env
```
Add environment variables inside .env like:
```
DATABASE_URL=your_database_connection_string
SECRET_KEY=your_secret_key
DEBUG=True
```
## Step 4: Configure Nginx

Create a new Nginx configuration file for your Flask app:
```
sudo nano /etc/nginx/sites-available/flask-app
```
Paste the following configuration (replace localhost with your server domain or IP if applicable):
```
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    error_log /var/log/nginx/flask-app-error.log;
    access_log /var/log/nginx/flask-app-access.log;
}
```
Enable the site by creating a symbolic link:
```
sudo ln -s /etc/nginx/sites-available/flask-app /etc/nginx/sites-enabled/
```
Test the Nginx configuration for syntax errors:
```
sudo nginx -t
```
If no errors, reload Nginx to apply changes:
```
sudo systemctl reload nginx
```
### Step 5: Run the Flask Application with Gunicorn

From your project directory, start Gunicorn to serve your app:
```
gunicorn --bind 127.0.0.1:8000 run:app
