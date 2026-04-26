# 🧠 HackerSpace

A web-based platform inspired by Mr. Robot aesthetics, designed to simulate a hacker-style community where users can register, log in, and interact with dynamically generated data.

# 🚀 Overview

HackerSpace is a Flask-powered web application that combines:

User authentication (login & registration)
Database integration using MySQL
Data processing with pandas
Dynamic data visualization

The project focuses on learning full-stack fundamentals, including backend logic, database design, and frontend rendering.

# 🛠️ Tech Stack
Backend: Python (Flask)
Database: MySQL
Data Handling: pandas
Frontend: HTML, CSS (Bootstrap)
Templating: Jinja2

# ⚙️ Features
🔐 User registration and login system
🗄️ MySQL database integration
📊 Display CSV / database data dynamically
📈 Data visualization (graphs)
🧑‍💻 Hacker-themed UI (fsociety-inspired)
📁 Project Structure
Hackerspace/
│
├── app.py              # Main Flask application
├── templates/          # HTML templates (Jinja2)
├── static/             # CSS, JS, assets
├── database/           # SQL files / schemas
├── data/               # CSV datasets
└── README.md

# 🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/LoelStark/Hackerspace.git
cd Hackerspace
2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
3. Install dependencies
pip install flask pandas mysql-connector-python
4. Configure MySQL
Create a database
Import your SQL schema
Update your database connection in app.py
▶️ Running the App
python app.py

Then open:

http://127.0.0.1:5000/
📊 Data Handling
Data can be loaded from CSV files using pandas:
df = pd.read_csv("file.csv")
data = df.to_dict(orient="records")
This data is then passed to templates for display or visualization.
📈 Future Improvements
Password hashing & security enhancements
User roles (admin / members)
Real-time dashboards
API integration
Advanced data analytics
#  🤝 Contributing

Contributions are welcome.

Fork the repo
Create a new branch
Commit your changes
Open a pull request
📜 License

This project is for educational purposes.
