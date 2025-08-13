# Deploying a Flask App on AWS EC2 Instance

This guide walks you through launching an AWS EC2 instance, uploading your Flask app, and running it using Gunicorn. AWS HAS A FREE TIER THAT FOR A12 MONTHS WE GOING TO USE THAT TO TEST 

---

## Prerequisites
- AWS account with permissions to create EC2 instances.
- Your Flask app ready locally.
- An SSH key pair (`.pem` file) generated on AWS for EC2 access.
- Basic terminal knowledge.

---

<img width="1913" height="386" alt="image" src="https://github.com/user-attachments/assets/fa17e78d-d80f-4f48-8c79-b2b0c039120d" />


## 1. Launch an EC2 Instance

1. Log in to your [AWS Management Console](https://aws.amazon.com/console/).
2. Navigate to **EC2** > **Instances** > **Launch Instances**.
3. Choose an Amazon Machine Image (AMI), preferably **Ubuntu Server 22.04 LTS**.
4. Select an instance type like **t2.micro** (free tier eligible).
5. Configure instance details:
   - Leave defaults for VPC and subnet (default is fine).
6. Configure Security Group:
   - Allow **SSH (port 22)** from your IP only.
   - Allow **HTTP (port 80)** from anywhere (for web traffic).
   - Allow **Custom TCP (port 8000)** from anywhere (optional, for testing Gunicorn).
7. Review and launch.
8. When prompted, create or select an existing key pair (.pem file). Download and save it securely on project directory(recommended).
   **You can leave other fields with default setting**
---

## 2. Get the Public IP Address

- After the instance launches, find its **IPv4 Public IP** on the instance details page.  
- This is the address you'll SSH into and access your Flask app.

---

### 3. Connect to Your EC2 Instance via SSH

Before connecting, make sure your private key has the correct permissions, below ensures that your key is readable only by you, which SSH requires.

```
chmod 400 booking_key.pem
```

## 4. Transfer files to EC2/alternatively clone from github
Use **SCP** to send files from your local machine to EC2:

```
scp -i booking_key.pem -r ~/Table_booking-CRUD ubuntu@<EC2ls_PUBLIC_IP>:~/

You can type Yes when prompted to continue
 or
git clone https://github.com/username/Table_booking-CRUD.git
---

Once set, you can root to directory and set up environment:
```
cd ~/Table_booking-CRUD
```
```
```
sudo apt update
sudo apt install python3.10-venv python3-pip -y
python3 -m venv --copies venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

```

Test locally:

```

Once done you can test gunicorn, use daemon to keep app running in the background

```

sudo ~/Table_booking-CRUD/venv/bin/gunicorn --bind 0.0.0.0:80 run:app --daemon

```

You can use below to kill the server

```
sudo pkill gunicorn
```

**Instance Shutdown vs Termination:**  
  Stopping (shutting down) your EC2 instance does **not** stop billing completely — you will still be charged for any allocated storage (EBS volumes). To avoid unexpected charges, **terminate** the instance once you finish testing.

- **How to Terminate Your EC2 Instance:**  
  1. Go to the EC2 dashboard.  
  2. Select your running instance.  
  3. Click **Actions** > **Instance State** > **Terminate Instance**.  
  4. Confirm termination. 
