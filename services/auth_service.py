import json
import os
from pathlib import Path

class AuthService:
    def __init__(self):
        self.users = {}
        self.user_id_counter = 1
        self.data_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'users_data.json')
        
        # Load existing users from file
        self.load_users()
        
        # Initialize with demo user if no users exist
        if not self.users:
            self.users['demo'] = {
                'id': self.user_id_counter,
                'username': 'demo',
                'password': 'demo123',
                'email': 'demo@roadside.com',
                'phone': '1234567890'
            }
            self.user_id_counter += 1
            self.save_users()
    
    def load_users(self):
        """Load users from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.users = data.get('users', {})
                    self.user_id_counter = data.get('user_id_counter', 1)
            except (json.JSONDecodeError, IOError):
                self.users = {}
                self.user_id_counter = 1
    
    def save_users(self):
        """Save users to JSON file"""
        try:
            data = {
                'users': self.users,
                'user_id_counter': self.user_id_counter
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving users: {e}")
    
    def login(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            return user
        return None
    
    def register(self, username, password, email, phone):
        if username in self.users:
            return None  # User already exists
        
        new_user = {
            'id': self.user_id_counter,
            'username': username,
            'password': password,
            'email': email,
            'phone': phone
        }
        self.users[username] = new_user
        self.user_id_counter += 1
        self.save_users()  # Save to file
        return new_user
    
    def user_exists(self, username):
        return username in self.users
