from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

#Save data request in temporary memory
requests = []

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/request', methods=['GET'])
def request_taxi():
    return render_template('form.html')

@main.route('/submit-request', methods=['POST'])
def submit_request():
    #Take data from form
    name = request.form['name']
    pickup = request.form['pickup']
    time = request.form['time']
    dept = request.form['dept']

    #save to temporary list
    requests.append({'name':name, 'pickup': pickup, 'time': time, 'dept':dept})

    return redirect(url_for('main.view_requests'))

@main.route('/view-requests', methods=['GET'])
def view_requests():
    #tampilkan semua data request
    return render_template('view_requests.html', requests=requests)
