from datetime import datetime

class VehicleService:
    def __init__(self):
        self.vehicle_companies = {
            'Car': ['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes', 'Hyundai', 'Maruti Suzuki'],
            'Bike': ['Honda', 'Yamaha', 'Royal Enfield', 'Bajaj', 'TVS', 'KTM', 'Suzuki']
        }
        
        self.vehicle_models = {
            'Car': {
                'Toyota': ['Camry', 'Corolla', 'RAV4', 'Highlander'],
                'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot'],
                'Ford': ['F-150', 'Mustang', 'Explorer', 'Escape'],
                'BMW': ['3 Series', '5 Series', 'X5', 'X3'],
                'Mercedes': ['C-Class', 'E-Class', 'GLC', 'GLE'],
                'Hyundai': ['i20', 'Creta', 'Verna', 'Venue'],
                'Maruti Suzuki': ['Swift', 'Baleno', 'Dzire', 'Vitara Brezza']
            },
            'Bike': {
                'Honda': ['Activa', 'Shine', 'CB350', 'Hornet'],
                'Yamaha': ['FZ', 'R15', 'MT-15', 'Ray ZR'],
                'Royal Enfield': ['Classic 350', 'Bullet', 'Himalayan', 'Meteor'],
                'Bajaj': ['Pulsar', 'Dominar', 'Avenger', 'CT100'],
                'TVS': ['Apache', 'Jupiter', 'Ntorq', 'Raider'],
                'KTM': ['Duke 200', 'Duke 390', 'RC 200', 'Adventure 390'],
                'Suzuki': ['Gixxer', 'Access', 'Burgman', 'Intruder']
            }
        }
    
    def get_vehicle_types(self):
        return ['Car', 'Bike']
    
    def get_companies_by_type(self, vehicle_type):
        return self.vehicle_companies.get(vehicle_type, [])
    
    def get_models_by_company(self, vehicle_type, company):
        models = self.vehicle_models.get(vehicle_type, {})
        return models.get(company, [])
    
    def get_years(self):
        current_year = datetime.now().year
        return [str(year) for year in range(current_year, current_year - 21, -1)]
    
    def get_common_issues(self, vehicle_type):
        if vehicle_type == 'Car':
            return [
                'Engine Problem',
                'Battery Dead',
                'Flat Tire',
                'Brake Issue',
                'AC Not Working',
                'Transmission Problem',
                'Overheating',
                'Other'
            ]
        elif vehicle_type == 'Bike':
            return [
                'Engine Problem',
                'Battery Dead',
                'Flat Tire',
                'Brake Issue',
                'Chain Problem',
                'Electrical Issue',
                'Fuel System',
                'Other'
            ]
        return []
