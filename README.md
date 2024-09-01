<!-- ABOUT THE PROJECT -->
## Summary

This project consists of two tasks:
- Determines a person's maximum skill level in a sports competition.
- Create a custom odoo module to book a room or a room in a hotel.

### Built With

This project was created using:

* [![Python][Python]][Python-url]
* [![Odoo][Odoo]][Odoo-url]
* [![PostgreSQL][PostgreSQL]][PostgreSQL-url]

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Before running this project, make sure you have installed some of the tools below, because I use the Linux operating system, I will give an example using Linux.
* Python 3
  ```sh
  sudo apt install python3
  ```

### Installation

1. Clone the repo
   ```sh
   https://github.com/Galuh80/tunas_ridean.git
   ```
2. Move to directory
   ```sh
   cd tunas_ridean
   ```

<!-- USAGE EXAMPLES -->
## Usage

If you want to run the first application, then you have to go to the task_one folder:

1. Run application
   ```sh
   cd task_one
   ```
2. Execute command
   ```sh
   python3 main.py
   ```

If you want to run the second application, then you have to go to the task_one folder:

SETUP CONFIG: You have to set several variables in the config.conf file which is in the conf folder

1. Run application
   ```sh
   cd task_two
   ```
2. Execute command
   ```sh
   cd odoo-14.0
   ```
3. Install virtual environment
   ```sh
   python3 -m venv env
   ```
4. Activate the environmnet
   ```sh
   source env/bin/activate
   ```
5. Install requirements
   ```sh
   pip install -r install.txt
   ```
6. Run Odoo
   ```sh
   cd ..
   ```
   ```sh
   python3 odoo-14.0/odoo-server -c conf/config.conf
   ```

<!-- USAGE EXAMPLES -->
## API Swagger
You can access the API at the following URL:

6. API Odoo
   ```sh
   http://localhost:8069/api/room_booking/status/
   ```

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Odoo]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Odoo-url]: https://www.odoo.com/id_ID
[PostgreSQL]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
