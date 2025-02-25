from pharmacy.models import Pharmacy
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populates the database with sample pharmacy data'

    def handle(self, *args, **options):
        # Sample pharmacy data
        pharmacies = [
            {'name': 'City Pharmacy', 'address': '123 Main Street', 'phone': '555-0123', 'email': 'city.pharmacy@example.com'},
            {'name': 'Health Plus', 'address': '456 Oak Avenue', 'phone': '555-0456', 'email': 'health.plus@example.com'},
            {'name': 'MediCare', 'address': '789 Pine Road', 'phone': '555-0789', 'email': 'medicare@example.com'},
            {'name': 'Quick Meds', 'address': '321 Elm Street', 'phone': '555-0321', 'email': 'quickmeds@example.com'},
            {'name': 'Family Pharmacy', 'address': '654 Maple Lane', 'phone': '555-0654', 'email': 'family.pharmacy@example.com'},
            {'name': 'Central Drugstore', 'address': '987 Cedar Blvd', 'phone': '555-0987', 'email': 'central.drugs@example.com'},
            {'name': 'Wellness Pharmacy', 'address': '741 Birch Street', 'phone': '555-1111', 'email': 'wellness@example.com'},
            {'name': 'Care Plus Drugs', 'address': '852 Willow Road', 'phone': '555-2222', 'email': 'careplus@example.com'},
            {'name': 'Metro Medicines', 'address': '963 Cherry Lane', 'phone': '555-3333', 'email': 'metro.meds@example.com'},
            {'name': 'Star Pharmacy', 'address': '159 Rose Avenue', 'phone': '555-4444', 'email': 'star.pharm@example.com'},
            {'name': 'Downtown Drugs', 'address': '753 Lake Street', 'phone': '555-5555', 'email': 'downtown@example.com'},
            {'name': 'Green Cross', 'address': '951 Forest Road', 'phone': '555-6666', 'email': 'green.cross@example.com'},
            {'name': 'Sunrise Pharmacy', 'address': '357 Beach Blvd', 'phone': '555-7777', 'email': 'sunrise@example.com'},
            {'name': 'Valley Meds', 'address': '852 Mountain View', 'phone': '555-8888', 'email': 'valley.meds@example.com'},
            {'name': 'Prime Care', 'address': '753 River Road', 'phone': '555-9999', 'email': 'prime.care@example.com'},
            {'name': 'Express Pharmacy', 'address': '147 Station Square', 'phone': '555-1234', 'email': 'express@example.com'},
            {'name': 'Neighborhood Drugs', 'address': '258 Park Avenue', 'phone': '555-2345', 'email': 'neighborhood@example.com'},
            {'name': 'United Pharmacy', 'address': '369 Union Street', 'phone': '555-3456', 'email': 'united@example.com'},
            {'name': 'Royal Drugs', 'address': '147 Kings Road', 'phone': '555-4567', 'email': 'royal@example.com'},
            {'name': 'Bridge Pharmacy', 'address': '258 Harbor View', 'phone': '555-5678', 'email': 'bridge@example.com'},
            {'name': 'Pacific Meds', 'address': '369 Ocean Drive', 'phone': '555-6789', 'email': 'pacific@example.com'},
            {'name': 'Sunshine Drugs', 'address': '147 Beach Road', 'phone': '555-7890', 'email': 'sunshine@example.com'},
            {'name': 'Care First', 'address': '258 Health Street', 'phone': '555-8901', 'email': 'care.first@example.com'},
            {'name': 'Village Pharmacy', 'address': '369 Rural Route', 'phone': '555-9012', 'email': 'village@example.com'},
            {'name': 'Essential Meds', 'address': '147 Central Ave', 'phone': '555-0147', 'email': 'essential@example.com'},
            {'name': 'Modern Pharmacy', 'address': '258 Tech Road', 'phone': '555-0258', 'email': 'modern@example.com'},
            {'name': 'Reliable Drugs', 'address': '369 Trust Street', 'phone': '555-0369', 'email': 'reliable@example.com'},
            {'name': 'Community Care', 'address': '147 Social Circle', 'phone': '555-0147', 'email': 'community@example.com'},
            {'name': 'Quality Pharmacy', 'address': '258 Standard Road', 'phone': '555-0258', 'email': 'quality@example.com'},
            {'name': 'Save Plus Drugs', 'address': '369 Economy Way', 'phone': '555-0369', 'email': 'saveplus@example.com'}
        ]

        # Create pharmacy records
        for pharmacy_data in pharmacies:
            pharmacy = Pharmacy.objects.create(**pharmacy_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created pharmacy: {pharmacy.name}')
            )