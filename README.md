# TaskMaster - To-Do List Application

## 📋 Overview
**TaskMaster** is a feature-rich, web-based to-do list application built with Flask. It provides users with a secure and intuitive platform to manage daily tasks, set priorities, and track productivity through comprehensive user profiles.

## ✨ Features
- **User Authentication**: Secure registration and login system with password hashing
- **Task Management**: Create, view, and organize tasks with detailed attributes
- **Task Categorization**: Organize tasks by categories and priorities
- **User Dashboard**: Clean interface to view all tasks at a glance
- **Profile Analytics**: Track task statistics and recent activity
- **Responsive Design**: User-friendly interface for seamless task management
- **Deadline Tracking**: Set and monitor task completion dates

## 🛠️ Technologies Used
- **Backend**: Python, Flask
- **Database**: MySQL with SQLAlchemy ORM
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Frontend**: HTML, CSS, JavaScript
- **Templating**: Jinja2

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- pip package manager

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/taskmaster-todo.git
   cd taskmaster-todo
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```sql
   CREATE DATABASE todo;
   CREATE USER 'root'@'localhost' IDENTIFIED BY 'root';
   GRANT ALL PRIVILEGES ON todo.* TO 'root'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. **Configure Application**
   - Update database credentials in `app.config['SQLALCHEMY_DATABASE_URI']` if needed
   - Change `app.secret_key` for production

6. **Run the Application**
   ```bash
   python app.py
   ```

7. **Access the Application**
   Open browser and navigate to `http://localhost:5000`

## 🗂️ Project Structure
```
taskmaster-todo/
├── app.py                 # Main application file
├── models.py             # Database models (User, Task)
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── home.html        # Landing/registration page
│   ├── login.html       # Login page
│   ├── dashboard.html   # Main task interface
│   └── profile.html     # User profile page
└── static/              # CSS, JS, images (if any)
```

## 🚀 Usage Guide

### 1. Registration
- Navigate to the home page
- Fill in name, email, and password
- Submit to create an account

### 2. Login
- Use registered credentials
- Access dashboard upon successful authentication

### 3. Creating Tasks
- Click "Add Task" on dashboard
- Fill in task details:
  - Task name
  - Description
  - Completion date
  - Priority (optional)
  - Category (optional)
- Submit to add to your task list

### 4. Profile View
- Access profile page to view:
  - Total tasks created
  - Completed vs pending tasks
  - Recent activity
  - Account information

### 5. Logout
- Securely logout from the application

## 🔒 Security Features
- Password hashing using Bcrypt
- Session management with Flask-Login
- SQL injection prevention via SQLAlchemy
- Secure authentication flow

## 📊 Database Schema

### Users Table
- `id`: Primary key
- `name`: User's full name
- `email`: Unique email address
- `password`: Hashed password
- `created_at`: Account creation timestamp

### Tasks Table
- `id`: Primary key
- `task_name`: Task title
- `task_desc`: Task description
- `com_date`: Completion deadline
- `task_priority`: Priority level
- `category`: Task category
- `relation`: Foreign key to User.id

## 🔧 Configuration Options

### Environment Variables (Recommended for Production)
```python
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.secret_key = os.environ.get('SECRET_KEY')
```

### Customization
- Modify port: Change `app.run(debug=True, port=8000)`
- Add SSL: Configure for HTTPS in production
- Email notifications: Integrate with SMTP for reminders

## 🚧 Future Enhancements
- [ ] Email verification during registration
- [ ] Task editing and deletion functionality
- [ ] Task sharing/collaboration features
- [ ] Mobile application
- [ ] Email/SMS reminders
- [ ] Dark/light theme toggle
- [ ] Task search and filtering
- [ ] Export tasks to PDF/CSV
- [ ] Calendar integration

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Important Notes
- Change default database credentials in production
- Implement proper error handling for production use
- Add CSRF protection for forms
- Consider adding rate limiting
- Regular database backups recommended

## 🆘 Support
For issues, questions, or suggestions:
1. Check existing issues in GitHub
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

---

**Made with ❤️ using Flask**
