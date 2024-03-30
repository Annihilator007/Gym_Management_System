from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Database connection
# for mysql use name run query( SELECT USER(); )
# -- This query will return a result like 'username'@'hostname'.
conn = mysql.connector.connect(
    host="localhost",
    user="your_my_sql_server_ussername",
    password="your_my_sql_server_password",
    database="gym_management_system"
)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Staff dashboard

# @app.route('/staff_dashboard')
# def staff_dashboard():
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM STAFF")
#     staff = cursor.fetchall()
#     cursor.close()
#     return render_template('staff_dashboard.html', staff=staff)

@app.route('/staff_dashboard')
def staff_dashboard():
    if 'login_id' in session:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STAFF")
        staff = cursor.fetchall()
        cursor.close()
        return render_template('staff_dashboard.html', staff=staff)
    else:
        return redirect(url_for('login'))


# Add staff member
@app.route('/add_staff', methods=['GET', 'POST'])
def add_staff():
    if request.method == 'POST':
        cursor = conn.cursor()
        name = request.form['name']
        mobile = request.form['mobile']
        salary = request.form['salary']
        experience=request.form['experience']
        login_id=request.form['login_id']
        password=request.form['password']
        cursor.execute("INSERT INTO STAFF (NAMES, MOB_NO, SALARY, EXPERIENCE, LOGIN_ID, PASSWORDS) VALUES (%s, %s, %s, %s, %s, %s)", (name, mobile, salary, experience, login_id, password))
        conn.commit()
        cursor.close()
        return redirect(url_for('staff_dashboard'))
    return render_template('add_staff.html')

# Add Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_id = request.form['login_id']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM STAFF WHERE LOGIN_ID = %s AND PASSWORDS = %s", (login_id, password))
        staff = cursor.fetchone()
        cursor.close()
        if staff:
            # Authentication successful, redirect to staff dashboard
            session['login_id'] = login_id
            return redirect(url_for('staff_dashboard'))
        else:
            # Authentication failed, show error message
            return render_template('login.html', error="Invalid login credentials. Please try again.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('login_id', None)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
