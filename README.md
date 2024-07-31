# Python Flask Project

This project is designed to demonstrate various methods and features of Python, along with the use of Flask to create a web server. It also showcases the integration of MySQL as the database, hosted locally.

## Table of Contents
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Project Structure


## Features

- Demonstrates Python functions and methods.
- Utilizes Flask for web server creation.
- Integrates with MySQL database hosted locally.
- Basic HTML templating with Flask.
- Includes CSS for basic styling.

## Installation

### Prerequisites

- Python 3.x
- MySQL Server

### Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/python-flask-project.git
    cd python-flask-project
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**
    - Create a new database named `flask_demo`.
    - Update `config.py` with your MySQL username, password, and database name.

5. **Run the application:**
    ```sh
    python run.py
    ```

## Usage

- Navigate to `http://127.0.0.1:5000` in your web browser to view the application.

## Endpoints

- `/`: The home page displaying a welcome message.
- `/data`: A page displaying data retrieved from the MySQL database.

## Database

- **Database Name:** flask_demo
- **Table:** demo_table

**Table Structure:**

```sql
CREATE TABLE demo_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    value INT
);
