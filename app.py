from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import math

# Import services
from services.auth_service import AuthService
from services.vehicle_service import VehicleService
from services.service_center_service import ServiceCenterService
from services.booking_service import BookingService

app = Flask(__name__)
app.secret_key = 'roadside-assistant-secret-key-2024'

# Initialize services
auth_service = AuthService()
vehicle_service = VehicleService()
service_center_service = ServiceCenterService()
booking_service = BookingService()

# Routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = auth_service.login(username, password)
        if user:
            session['user'] = user
            session['username'] = username
            return redirect(url_for('welcome'))
        return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        
        user = auth_service.register(username, password, email, phone)
        if user:
            session['user'] = user
            session['username'] = username
            return redirect(url_for('welcome'))
        return render_template('register.html', error='Username already exists')
    
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('welcome.html', username=session['username'])

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    vehicle_types = vehicle_service.get_vehicle_types()
    return render_template('dashboard.html', username=session['username'], vehicleTypes=vehicle_types)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# API Routes
@app.route('/api/companies')
def get_companies():
    vehicle_type = request.args.get('type')
    companies = vehicle_service.get_companies_by_type(vehicle_type)
    return jsonify(companies)

@app.route('/api/models')
def get_models():
    vehicle_type = request.args.get('type')
    company = request.args.get('company')
    models = vehicle_service.get_models_by_company(vehicle_type, company)
    return jsonify(models)

@app.route('/api/years')
def get_years():
    years = vehicle_service.get_years()
    return jsonify(years)

@app.route('/api/issues')
def get_issues():
    vehicle_type = request.args.get('vehicleType')
    issues = vehicle_service.get_common_issues(vehicle_type)
    return jsonify(issues)

@app.route('/find-services', methods=['POST'])
def find_services():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    vehicle_type = request.form.get('vehicleType')
    company = request.form.get('company')
    model = request.form.get('model')
    year = request.form.get('year')
    issue = request.form.get('issue')
    custom_issue = request.form.get('customIssue', '')
    latitude = float(request.form.get('latitude'))
    longitude = float(request.form.get('longitude'))
    
    # Store in session
    session['vehicle'] = {
        'type': vehicle_type,
        'company': company,
        'model': model,
        'year': year
    }
    session['issue'] = issue
    session['customIssue'] = custom_issue
    session['userLatitude'] = latitude
    session['userLongitude'] = longitude
    
    # Find service centers
    service_centers = service_center_service.find_nearby_service_centers(
        vehicle_type, company, latitude, longitude
    )
    
    display_issue = custom_issue if issue == 'Other' else issue
    
    return render_template('service-list.html', 
                         serviceCenters=service_centers,
                         vehicle=session['vehicle'],
                         issue=display_issue)

@app.route('/book-service', methods=['POST'])
def book_service():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    service_center_id = int(request.form.get('serviceCenterId'))
    
    vehicle = session.get('vehicle')
    issue = session.get('issue')
    custom_issue = session.get('customIssue', '')
    latitude = session.get('userLatitude')
    longitude = session.get('userLongitude')
    
    service_center = service_center_service.get_service_center_by_id(service_center_id)
    
    booking = {
        'username': session['username'],
        'vehicle': vehicle,
        'issue': issue,
        'customIssue': custom_issue,
        'serviceCenter': service_center,
        'userLatitude': latitude,
        'userLongitude': longitude
    }
    
    saved_booking = booking_service.create_booking(booking)
    
    return render_template('booking-confirmation.html', booking=saved_booking)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
