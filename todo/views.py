from django.shortcuts import render, redirect
from django.contrib import messages
import mysql.connector as sql

# Signup View
def signup(request):
    if request.method == 'POST':
        try:
            # Connect to MySQL
            m = sql.connect(host='localhost', user='root', passwd='anubhav2004', database='test_db')
            cursor = m.cursor()

            # Extract Form Data
            fnm = request.POST.get('fnm', '')
            emailid = request.POST.get('emailid', '')
            pwd = request.POST.get('pwd', '')

            # Insert Data (Using Parameterized Query)
            query = "INSERT INTO users (first_name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (fnm, emailid, pwd))
            m.commit()

            messages.success(request, "Signup successful! Please log in.")
            return redirect('login')  # Redirect to login page

        except sql.Error as e:
            messages.error(request, f"Database Error: {e}")
    
    return render(request, 'signup.html')


# Login View
def login(request):
    if request.method == "POST":
        try:
            # Connect to MySQL
            m = sql.connect(host="localhost", user="root", passwd="anubhav2004", database='test_db')
            cursor = m.cursor()

            # Extract Form Data
            emailid = request.POST.get("emailid", "")
            pwd = request.POST.get("pwd", "")

            # Check Credentials
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (emailid, pwd))
            t=tuple(cursor.fetchall())  # Fetch one row

            if t==():
                return redirect('/login')
            else:
                return render(request,'todo.html')

        except sql.Error as e:
            messages.error(request, f"Database Error: {e}")
    
    return render(request, 'login.html')

def todo(request):
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="anubhav2004", database='test_db')
        cursor = m.cursor()
    todo = request.POST.get('title', '')

    query = "INSERT INTO TODOO (todo) VALUES (%s)"
    cursor.execute(query, (todo))
    m.commit()

    return render(request,'todo.html')

def signout(request):
    logout(request)
    return redirect('/login')

def logout(request):
    return redirect('/login')