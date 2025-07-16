# Real-Time Blogging Project

A simple real-time blog and chat application built with Flask, Flask-SocketIO, and JavaScript.

## Features

- Real-time messaging between users
- Submit new blog posts (title + content)
- Display a list of all blog posts on the main page
- In-memory storage for blog posts (can be upgraded to use a database)

## Setup

1. Clone the repository.
2. Ensure you have Python 3 installed.
3. Install dependencies:
    ```bash
    pip install flask flask-socketio
    ```
4. Place `index.html` in a folder named `templates` in the project directory.
5. Run the app:
    ```bash
    python app.py
    ```
6. Open your browser and go to [http://localhost:5000](http://localhost:5000).

## Upgrading to Database Storage

To use SQLite, install Flask-SQLAlchemy and update `app.py` as needed.

## License

MIT