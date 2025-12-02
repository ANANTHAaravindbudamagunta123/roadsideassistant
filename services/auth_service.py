class AuthService:
    def __init__(self):
        self.users = {}
        self.user_id_counter = 1
        
        # Initialize with demo user
        self.users['demo'] = {
            'id': self.user_id_counter,
            'username': 'demo',
            'password': 'demo123',
            'email': 'demo@roadside.com',
            'phone': '1234567890'
        }
        self.user_id_counter += 1
    
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
        return new_user
    
    def user_exists(self, username):
        return username in self.users
