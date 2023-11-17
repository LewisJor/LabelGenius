# LabelGenius

## Overview
LabelGenius is a Python application for enabling one-shot or zero-shot labeling with Large Language Models (LLM). It's built on Flask and SQLAlchemy and offers both a frontend and a backend component.

## Features
- Easy-to-use frontend for setting up labeling tasks
- Can interact with any LLM using an API key or run locally
- Backend built on FastAPI for performance and optimization
- Stores labeling configurations in an SQLite database

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/LabelGenius.git

# Go into the repository
cd LabelGenius

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage

To run the application, execute:

```bash
flask run
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Database Configuration

The application uses SQLite for database needs. The database connection is configured through the `SQLALCHEMY_DATABASE_URI` parameter in `app.py`.

## License

Choose an appropriate license for your project and mention it here.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

