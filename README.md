# Django Shopping App

This is a Django-based shopping application where members can enroll and perform transactions against various offers. The project uses Django 5, Python 3, and Django REST Framework (DRF). The application is deployed on AWS EC2.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Deployment to EC2](#deployment-to-ec2)
- [API Usage](#api-usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following installed on your local machine:

- Python 3.x
- Django 5.x
- Django REST Framework
- MySQL Server
- Git
- Homebrew (for macOS users)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## MySQL Installation

1. Install MySQL Server using Homebrew (for macOS users):

    ```bash
    brew install mysql
    brew services start mysql
    ```

    The root password for MySQL will be `root`.

2. Install additional dependencies:

    ```bash
    brew install pkg-config
    brew install mysql-connector-c
    ```

3. Access the MySQL shell:

    ```bash
    sudo mysql
    ```

4. Inside the MySQL shell, run the following commands to set up the database and users:

    ```sql
    CREATE USER 'root'@'localhost' IDENTIFIED BY 'rootpassword';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
    CREATE DATABASE djupdb;
    CREATE USER 'djupuser'@'localhost' IDENTIFIED BY 'djuppassword';
    GRANT ALL PRIVILEGES ON djupdb.* TO 'djupuser'@'localhost';
    ```

## Database Setup

1. Apply migrations to set up your database:

    ```bash
    python3 manage.py migrate
    ```

## Running the Application

1. Start the development server:

    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

2. Access the application at `http://{ECP_Public_IPV4}:8000/`.

## Deployment to EC2

1. Create an AWS account and launch a free tier micro EC2 instance with Ubuntu.

2. Connect to EC2 instance from the AWS Console.

3. Update the package lists and install pip:

    ```bash
    sudo apt update
    sudo apt install python3-pip
    ```

4. Install MySQL Server on the EC2 instance:

    ```bash
    sudo apt install mysql-server
    ```

5. Clone your project repository on the EC2 instance:

    ```bash
    git clone https://github.com/aaditshah18/Dj-Up.git
    cd Dj-Up
    ```

6. Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

7. Configure your database settings and environment variables as mentioned in the [Configuration](#configuration) section.

8. Inside the MySQL shell, run the following commands to set up the database and users (similar to local setup):

    ```sql
    sudo mysql
    CREATE USER 'root'@'localhost' IDENTIFIED BY 'rootpassword';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;
    CREATE DATABASE djupdb;
    CREATE USER 'djupuser'@'localhost' IDENTIFIED BY 'djuppassword';
    GRANT ALL PRIVILEGES ON djupdb.* TO 'djupuser'@'localhost';
    ```

9. Apply migrations and collect static files:

    ```bash
    python manage.py migrate
    python manage.py collectstatic
    ```

## API Usage
Import the collection and use the APIs - 

- Postman Env - [DjUpEnv](Djupenv.postman_environment.json)
- Postman Collection - [DjUpPostmanCollection](DjupAPIs.postman_collection.json)


## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/branch`).
3. Commit your changes (`git commit -m 'Added some feature'`).
4. Push to the branch (`git push origin feature/branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
