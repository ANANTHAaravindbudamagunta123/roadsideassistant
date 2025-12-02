# Roadside Assistant Application

## Quick Start Guide

### Prerequisites
- Python 3.14+ (Already installed ✓)
- Flask 3.0.0 (Already installed ✓)

### Running the Application

**Option 1: Using the startup script**
```bash
# Double-click run.bat (Windows)
# Or run from command line:
run.bat
```

**Option 2: Manual start**
```bash
cd c:/Users/budamagunta/.gemini/antigravity/playground/empty-armstrong
python app.py
```

### Accessing the Application

1. Open your web browser
2. Navigate to: **http://localhost:5000** or **http://127.0.0.1:5000**
3. Login with demo credentials:
   - **Username**: `demo`
   - **Password**: `demo123`
4. Or register a new account

### Stopping the Application

Press `Ctrl+C` in the terminal window where the app is running.

### Application Features

✅ **User Authentication** - Login/Register with session management  
✅ **Vehicle Selection** - Choose vehicle type, company, model, and year  
✅ **Issue Reporting** - Select from common issues or describe custom problems  
✅ **Location Services** - Browser-based geolocation with fallback  
✅ **Service Centers** - Find nearby repair shops sorted by distance  
✅ **Booking System** - Book repairs with confirmation  

### Default Demo Account
- Username: `demo`
- Password: `demo123`

### Troubleshooting

**Port already in use?**
- The app runs on port 5000 by default
- If you get a port error, another app might be using it
- Stop other Flask apps or change the port in `app.py`

**Can't access the app?**
- Make sure the Flask server is running (you should see "Running on http://127.0.0.1:5000")
- Try http://localhost:5000 instead of 127.0.0.1
- Check your firewall settings

**Modal appearing on dashboard?**
- Clear your browser cache (Ctrl+Shift+Delete)
- Hard refresh the page (Ctrl+F5)

### File Structure

```
empty-armstrong/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── run.bat                   # Windows startup script
├── README.md                 # This file
├── services/                 # Backend services
│   ├── auth_service.py
│   ├── vehicle_service.py
│   ├── service_center_service.py
│   └── booking_service.py
├── templates/                # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── welcome.html
│   ├── dashboard.html
│   ├── service-list.html
│   └── booking-confirmation.html
└── static/
    └── css/
        └── style.css         # Global styles
```

### Support

For issues or questions, check the implementation plan and walkthrough documents in the brain folder.
