本项目由GPT4.0生成，仅供参考:

---

# Flask Web Navigation Project

This project is a simple web navigation page built with Flask. It allows you to manage and display a collection of web links in a user-friendly interface. The project includes features for adding, editing, and deleting web links, with the data stored in a JSON file for persistence.

![](https://raw.githubusercontent.com/JeckChen666/Jc-Private-Repository/main/image/202420240814235103.png)
![](https://raw.githubusercontent.com/JeckChen666/Jc-Private-Repository/main/image/202420240814235116.png)

## Features

- **Web Navigation Home**: Displays a list of web links with associated notes in a card-based layout.
- **Management Interface**: Provides functionality to add, edit, and delete web links.
- **Data Persistence**: Web links and their notes are stored in a `cards.json` file, which is automatically created if it doesn't exist.

## Getting Started

### Prerequisites

- **Python 3.11** or later
- **Docker** (optional, for containerization)

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/flask-web-navigation.git
    cd flask-web-navigation
    ```

2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application**:
    ```bash
    python app.py
    ```
    The application will be available at `http://127.0.0.1:5000`.

### Using Docker

To containerize and run the project with Docker:

1. **Build the Docker Image**:
    ```bash
    docker build -t flask-nav-app .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -d -p 5000:5000 -v $(pwd):/app flask-nav-app
    ```
    The application will be available at `http://localhost:5000`.

## Project Structure

```
flask-web-navigation/
│
├── app.py                 # Main Flask application
├── cards.json             # JSON file for storing web links (auto-created)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Dockerfile for containerization
├── templates/
│   ├── index.html         # HTML template for the home page
│   └── manage.html        # HTML template for the management interface
└── static/
    └── style.css          # CSS file for styling
```

## File Mapping and Port Exposure

- **Port 5000**: Exposed for Flask.
- **Volume Mapping**: The current directory (`$(pwd)`) is mapped to `/app` in the container to persist data in `cards.json`.

## Customization

- **Font and Styling**: The project uses `Noto Sans` and `Microsoft YaHei` fonts for a clean and modern look, supporting both Chinese and English characters.
- **CSS**: Modify `static/style.css` to customize the appearance of the navigation and management pages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Conclusion

This project provides a simple yet effective way to manage and display web links. With the help of Docker, it's easy to deploy and run in a containerized environment. Feel free to customize and extend the functionality as needed.