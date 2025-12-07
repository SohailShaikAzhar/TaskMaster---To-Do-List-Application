from flask import Flask, render_template, redirect, request, flash, url_for
from models import db, User, Task
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secrect'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:root@localhost:3306/todo'
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

with app.app_context(): 
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get_or_404(user_id)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        bname = request.form.get('username' , '')
        bemail = request.form.get('useremail' , '')
        bpassword = request.form.get('userpassword', '')
        check_email = User.query.filter_by(email = bemail).first()
        if check_email:
            flash('You are already registered 🤨, Login now')
            return render_template('login.html')
        else:
            user  = User(name=bname, email=bemail, password=bcrypt.generate_password_hash(bpassword))
            db.session.add(user)
            db.session.commit()
            flash('Yeahh...!🥳, Account created successfully')
            return redirect( url_for('login'))
    return render_template('home.html')

@app.route('/login/', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('useremail', '')
        password = request.form.get('userpassword', '')
        user = User.query.filter_by(email = email).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash('You were successfully logged in')
                return redirect( url_for('dashboard') )
            else:
                flash('User id or password is wrong ')
                return redirect( url_for('login') )
        else:
            flash('no account found')
            return redirect(url_for('login'))
    return render_template('login.html', message='')

@app.route('/dashboard/', methods= ['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        task_name = request.form.get('task_name', '')
        task_desc = request.form.get('task_desc', '')
        com_date = request.form.get('com_date', '')
        prio = request.form.get('prio', '')
        cato = request.form.get('cato', '')
        task = Task()
        task.task_name = task_name
        task.task_desc = task_desc
        task.com_date = com_date
        if prio:
            task.task_priority = prio
        if cato:
            task.category = cato
        task.relation = current_user.id
        db.session.add(task)    
        db.session.commit()
        return redirect( url_for('dashboard') )
    task = Task.query.filter_by(relation=current_user.id).all()
    date_time = datetime.now()
    dt = date_time.strftime("%Y-%m-%dT%H:%M")
    return render_template('dashboard.html', today_date= dt, tasks = task)

@app.route('/profile/')
@login_required
def profile():
    # Calculate statistics based on your Task model
    tasks_count = Task.query.filter_by(relation=current_user.id).count()
    
    # Get completed tasks (you might need to add a 'completed' field to your Task model)
    # If you don't have completed status, we'll use deadline comparison
    from datetime import datetime
    now = datetime.now()
    completed_tasks = Task.query.filter(
        Task.relation == current_user.id,
        Task.com_date < now  # Tasks past deadline considered "completed"
    ).count()
    
    pending_tasks = Task.query.filter(
        Task.relation == current_user.id,
        Task.com_date >= now  # Tasks with future deadline
    ).count()
    
    # Format member_since date
    member_since = current_user.created_at.strftime('%B %Y') if hasattr(current_user, 'created_at') else 'Recent'
    
    # Recent activity - get last 5 tasks
    recent_tasks = Task.query.filter_by(relation=current_user.id)\
                             .order_by(Task.com_date.desc())\
                             .limit(5)\
                             .all()
    
    # Prepare recent activity data
    recent_activity = []
    for task in recent_tasks:
        activity = {
            'type': 'task_created',
            'title': f'Created task: {task.task_name}',
            'description': task.task_desc[:50] + '...' if task.task_desc and len(task.task_desc) > 50 else task.task_desc or '',
            'time': task.com_date.strftime('%b %d') if task.com_date else 'Recently'
        }
        recent_activity.append(activity)
    
    return render_template('profile.html',
                         tasks_count=tasks_count,
                         completed_tasks=completed_tasks,
                         pending_tasks=pending_tasks,
                         member_since=member_since,
                         account_type='Standard',  # Add premium field to User model if needed
                         recent_activity=recent_activity)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)