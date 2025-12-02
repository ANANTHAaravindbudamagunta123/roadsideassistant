import math

class ServiceCenterService:
    def __init__(self):
        self.service_centers = []
        self.service_center_id_counter = 1
        
        # Initialize mock service centers
        # Car service centers
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Toyota Service Center',
            'address': '123 Main St, City',
            'phone': '+1-555-0101',
            'vehicleType': 'Car',
            'company': 'Toyota',
            'latitude': 17.385044,
            'longitude': 78.486671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Honda Auto Care',
            'address': '456 Park Ave, City',
            'phone': '+1-555-0102',
            'vehicleType': 'Car',
            'company': 'Honda',
            'latitude': 17.395044,
            'longitude': 78.496671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Universal Car Service',
            'address': '789 Oak Rd, City',
            'phone': '+1-555-0103',
            'vehicleType': 'Car',
            'company': 'All',
            'latitude': 17.375044,
            'longitude': 78.476671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'BMW Service Center',
            'address': '321 Elite Blvd, City',
            'phone': '+1-555-0104',
            'vehicleType': 'Car',
            'company': 'BMW',
            'latitude': 17.405044,
            'longitude': 78.506671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Maruti Authorized Service',
            'address': '654 Gandhi Nagar, City',
            'phone': '+1-555-0105',
            'vehicleType': 'Car',
            'company': 'Maruti Suzuki',
            'latitude': 17.365044,
            'longitude': 78.466671
        })
        self.service_center_id_counter += 1
        
        # Bike service centers
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Royal Enfield Service',
            'address': '111 Bike Lane, City',
            'phone': '+1-555-0201',
            'vehicleType': 'Bike',
            'company': 'Royal Enfield',
            'latitude': 17.380044,
            'longitude': 78.481671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Yamaha Bike Care',
            'address': '222 Speed St, City',
            'phone': '+1-555-0202',
            'vehicleType': 'Bike',
            'company': 'Yamaha',
            'latitude': 17.390044,
            'longitude': 78.491671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Universal Bike Repair',
            'address': '333 Rider Rd, City',
            'phone': '+1-555-0203',
            'vehicleType': 'Bike',
            'company': 'All',
            'latitude': 17.370044,
            'longitude': 78.471671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'KTM Service Point',
            'address': '444 Racing Ave, City',
            'phone': '+1-555-0204',
            'vehicleType': 'Bike',
            'company': 'KTM',
            'latitude': 17.400044,
            'longitude': 78.501671
        })
        self.service_center_id_counter += 1
        
        self.service_centers.append({
            'id': self.service_center_id_counter,
            'name': 'Bajaj Authorized Service',
            'address': '555 Pulsar St, City',
            'phone': '+1-555-0205',
            'vehicleType': 'Bike',
            'company': 'Bajaj',
            'latitude': 17.360044,
            'longitude': 78.461671
        })
        self.service_center_id_counter += 1
    
    def find_nearby_service_centers(self, vehicle_type, company, user_lat, user_lon):
        # Filter by vehicle type and company
        filtered = [
            sc for sc in self.service_centers
            if sc['vehicleType'] == vehicle_type and (sc['company'] == 'All' or sc['company'] == company)
        ]
        
        # Calculate distances
        for sc in filtered:
            distance = self._calculate_distance(user_lat, user_lon, sc['latitude'], sc['longitude'])
            sc['distance'] = round(distance, 1)
        
        # Sort by distance
        filtered.sort(key=lambda x: x['distance'])
        
        return filtered
    
    def _calculate_distance(self, lat1, lon1, lat2, lon2):
        # Haversine formula for distance calculation
        R = 6371  # Radius of the earth in km
        
        lat_distance = math.radians(lat2 - lat1)
        lon_distance = math.radians(lon2 - lon1)
        
        a = (math.sin(lat_distance / 2) * math.sin(lat_distance / 2) +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(lon_distance / 2) * math.sin(lon_distance / 2))
        
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        
        return distance
    
    def get_service_center_by_id(self, service_center_id):
        for sc in self.service_centers:
            if sc['id'] == service_center_id:
                return sc
        return None
