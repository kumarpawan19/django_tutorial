from pharmacy.models import Medicine
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help = 'Populates the database with sample medicine data'

    def handle(self, *args, **options):
        # Sample medicine data
        medicines = [
            {'name': 'Aspirin', 'price': 5.99, 'quantity': random.randint(50, 200)},
            {'name': 'Paracetamol', 'price': 4.99, 'quantity': random.randint(50, 200)},
            {'name': 'Ibuprofen', 'price': 6.99, 'quantity': random.randint(50, 200)},
            {'name': 'Amoxicillin', 'price': 12.99, 'quantity': random.randint(50, 200)},
            {'name': 'Ciprofloxacin', 'price': 15.99, 'quantity': random.randint(50, 200)},
            {'name': 'Omeprazole', 'price': 8.99, 'quantity': random.randint(50, 200)},
            {'name': 'Metformin', 'price': 7.99, 'quantity': random.randint(50, 200)},
            {'name': 'Amlodipine', 'price': 9.99, 'quantity': random.randint(50, 200)},
            {'name': 'Lisinopril', 'price': 11.99, 'quantity': random.randint(50, 200)},
            {'name': 'Simvastatin', 'price': 13.99, 'quantity': random.randint(50, 200)},
            {'name': 'Metoprolol', 'price': 10.99, 'quantity': random.randint(50, 200)},
            {'name': 'Losartan', 'price': 14.99, 'quantity': random.randint(50, 200)},
            {'name': 'Gabapentin', 'price': 16.99, 'quantity': random.randint(50, 200)},
            {'name': 'Sertraline', 'price': 18.99, 'quantity': random.randint(50, 200)},
            {'name': 'Fluoxetine', 'price': 17.99, 'quantity': random.randint(50, 200)},
            {'name': 'Citalopram', 'price': 19.99, 'quantity': random.randint(50, 200)},
            {'name': 'Escitalopram', 'price': 21.99, 'quantity': random.randint(50, 200)},
            {'name': 'Duloxetine', 'price': 23.99, 'quantity': random.randint(50, 200)},
            {'name': 'Venlafaxine', 'price': 20.99, 'quantity': random.randint(50, 200)},
            {'name': 'Tramadol', 'price': 22.99, 'quantity': random.randint(50, 200)},
            {'name': 'Hydrocodone', 'price': 25.99, 'quantity': random.randint(50, 200)},
            {'name': 'Oxycodone', 'price': 24.99, 'quantity': random.randint(50, 200)},
            {'name': 'Cyclobenzaprine', 'price': 8.49, 'quantity': random.randint(50, 200)},
            {'name': 'Meloxicam', 'price': 9.49, 'quantity': random.randint(50, 200)},
            {'name': 'Prednisone', 'price': 7.49, 'quantity': random.randint(50, 200)},
            {'name': 'Methylprednisolone', 'price': 11.49, 'quantity': random.randint(50, 200)},
            {'name': 'Azithromycin', 'price': 13.49, 'quantity': random.randint(50, 200)},
            {'name': 'Cephalexin', 'price': 12.49, 'quantity': random.randint(50, 200)},
            {'name': 'Doxycycline', 'price': 10.49, 'quantity': random.randint(50, 200)},
            {'name': 'Metronidazole', 'price': 14.49, 'quantity': random.randint(50, 200)}
        ]

        # Create medicine records
        for medicine_data in medicines:
            medicine = Medicine.objects.create(**medicine_data)
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created medicine: {medicine.name}')
            )

