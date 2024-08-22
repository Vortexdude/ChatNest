# ChatNest
###### projectname - ChatNest
###### version - 0.0.1
###### description - ChatNest application is a robust, production-ready API that leverages SQLAlchemy for ORM,


## Overview

ChatNest application is a robust, production-ready API that leverages SQLAlchemy for ORM, PostgreSQL as the database, and `dependency_injector` for managing dependencies. It provides a structured and scalable approach to building and managing RESTful APIs.

## Features

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs with Python 3.8+ based on standard Python type hints.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: Powerful, open-source object-relational database system.
- **Dependency Injection**: Using `dependency_injector` to manage application components and services.

## Getting Started

### Prerequisites

- Python 3.10 
- PostgreSQL database
- Virtual environment (recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/vortexdude/ChatNest.git
   cd ChatNest
   ```
2. Create and Activate a Virtual Environment:
    ``` bash
        python3 -m venv .venv
        source .venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ``` bash
        pip3 install -r requiremenets.txt
    ```

4. **Run the server:**
    ``` bash
        python3 src/app.py
    ```

#### Configuration
Create a .env file in the root directory of the project and add the following environment variables:
   ```
   TITLE=ChatNest
   POSTGRES_PORT=5432
   POSTGRES_PASSWORD=
   POSTGRES_USER=
   POSTGRES_DB=
   POSTGRES_HOST=
   ```
