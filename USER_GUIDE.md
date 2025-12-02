# Roadside Assistant - User Guide

## How to Use the Application

### Step 1: Login or Register

When you first open the application, you'll see the login page.

**To Login:**
- Enter your username and password
- Click "Sign In"
- Demo account: username `demo`, password `demo123`

**To Register:**
- Click "Register here" link
- Fill in your details (username, email, phone, password)
- Click "Create Account"

### Step 2: Welcome Animation

After successful login/registration, you'll see a welcome animation for 3 seconds, then automatically redirect to the dashboard.

### Step 3: Select Vehicle Type

On the dashboard, you'll see two options:
- 🚗 **Car**
- 🏍️ **Bike**

Click on your vehicle type to continue.

### Step 4: Enter Vehicle Details

Fill in the following information:
1. **Company** - Select from the dropdown (e.g., Toyota, Honda, Royal Enfield)
2. **Model** - Select your vehicle model (options change based on company)
3. **Year** - Select the year of your vehicle

Click **Next** to continue.

### Step 5: Report the Issue

Select the problem you're experiencing from the grid:
- Engine Problem
- Battery Dead
- Flat Tire
- Brake Issue
- AC Not Working (Cars) / Chain Problem (Bikes)
- Transmission Problem (Cars) / Electrical Issue (Bikes)
- Overheating (Cars) / Fuel System (Bikes)
- **Other** - For custom issues

If you select "Other", a dialog box will appear where you can describe your specific problem.

Click **Next** to continue.

### Step 6: Share Your Location

Click **Get My Location** button.

The browser will ask for permission to access your location:
- **Allow** - Your actual location will be used
- **Deny** - Default location (Hyderabad) will be used

Once location is obtained, click **Find Services**.

### Step 7: View Nearby Service Centers

You'll see a list of service centers sorted by distance from your location.

Each service center shows:
- Name and address
- Phone number
- Distance from you
- Specialization

You have two options for each center:
- **📞 Call Now** - Opens your phone dialer
- **📅 Book Repair** - Creates a booking

### Step 8: Booking Confirmation

After clicking "Book Repair", you'll see a confirmation page with:
- Booking ID
- Your vehicle details
- Reported issue
- Service center information
- Booking status (Pending)

From here you can:
- **📞 Call Service Center** - Contact them directly
- **🏠 Back to Dashboard** - Start a new request

## Tips

- All data is stored in memory, so it resets when you restart the server
- You can create multiple accounts
- The service centers are mock data for demonstration
- Distance calculation uses the Haversine formula for accuracy
- The app works best on modern browsers (Chrome, Firefox, Edge)

## Common Issues

**Modal appearing on dashboard?**
- Hard refresh the page (Ctrl+F5 or Cmd+Shift+R)
- Clear browser cache

**Can't select vehicle type?**
- Make sure JavaScript is enabled in your browser
- Try refreshing the page

**Location not working?**
- Grant location permission when browser asks
- If denied, the app will use a default location

**Service centers not showing?**
- Make sure you completed all previous steps
- Check that you selected a valid vehicle type and company
