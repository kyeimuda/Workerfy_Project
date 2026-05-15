from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from MainWorkerfy.models import Country, TradespersonProfile, ClientProfile,TradeCategory, TradeSpecialty, TradeSkillTag, Region, Certificate, PortfolioItem, JobPost, JobPostAttachment, City, Area
from datetime import datetime
from django.db import transaction

User = get_user_model()


class Command(BaseCommand):
    help = 'Seeds the data base with data(dammy data)'

    def add_arguments(self, parser):
        parser.add_argument('modelName',
                            type=str,
                            choices=['user','Region', 'Country', 'City',\
                                     'TradeCategory', 'TradeSpecialty', 'ClientProfile', 'TradespersonProfile',
                                    'JobPost'],
                            help='Model to be seeded')
        
        parser.add_argument('--file', type=str, help='CSV file to be with seeding data')
        parser.add_argument('--entryNumber', type=int, help='Number of entries to seed')

    def handle(self, *args, **options):
        modelName = options['modelName']
        entryNumber = options['entryNumber']
        CSV_file = options['file']
        self.stdout.write(self.style.SUCCESS(f'hello {modelName} {CSV_file}'))


        def safe_input(val):
                return True if val else False

        if modelName == 'user' and not CSV_file:
            
            if entryNumber is None or entryNumber <= 0:
                self.stdout.write(self.style.WARNING('No CSV file or entry number provided, or entry number is not positive. Defaulting to 1 entry. To continue enter - Yes, To stop enter: - No:'))
                entryNumber = 1
                res = input().lower()
                
                if res == 'yes':
                    try:
                        with transaction.atomic():
                            User.objects.create_user(email=f'user-{datetime.now()}@gamil.com', password='defaultPass123')
                            self.stdout.write( self.style.SUCCESS( f'Email: user-{datetime.now()}@gamil.com \n Password: defaultPass123 \n Created Successfully'))
                            self.stdout.write(f'Password: defaultPass123')
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f'{e}'))
                return
            elif entryNumber > 0:
                try:
                    with transaction.atomic():
                        for i in range(entryNumber):
                            try:
                                User.objects.create_user(email=f'user-{datetime.now()}@gamil.com', password='defaultPass123')
                                self.stdout.write( self.style.SUCCESS( f'Email: user-{datetime.now()}@gamil.com \n Password: defaultPass123 \n Created Successfully'))
                                self.stdout.write(f'Password: defaultPass123')
                            except Exception as e:
                                self.stderr.write(self.style.ERROR(f'{e}'))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'{e}'))
                return

        elif modelName == 'user' and CSV_file:
            import csv

            if not CSV_file.endswith('.csv'):
                self.stderr.write(self.style.ERROR('Invalid file format. Please provide a CSV file.'))
                return
            if not entryNumber or entryNumber <= 0:
                self.stdout.write(self.style.WARNING('Entry number is not positive. Defaulting to all entries in the CSV file. To continue enter - Yes, To stop enter: - No:'))
                res = input().lower()
                if res != 'yes':
                    return
                try:
                    with open(CSV_file, newline='') as csvfile:
                        reader = csv.DictReader(csvfile)
                        with transaction.atomic():
                            for row in reader:
                                try:
                                    User.objects.create_user(email=row['email'], password=row['password'])
                                    self.stdout.write(self.style.SUCCESS(f"User {row['email']} created successfully."))
                                except Exception as e:
                                    self.stderr.write(self.style.ERROR(f"Error creating user {row['email']}: {e}"))
                except FileNotFoundError as e:
                    self.stderr.write(self.style.ERROR(f'File not found: {CSV_file}'))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error reading CSV file: {e}'))

            elif entryNumber or entryNumber > 0:
                try:
                    with open(CSV_file, newline='') as csvfile:
                        reader = csv.DictReader(csvfile)
                        with transaction.atomic():
                            for i, row in enumerate(reader):
                                if i >= entryNumber:
                                    self.stdout.write(self.style.SUCCESS(f'{entryNumber} entries created successfully. Stopping further processing.'))
                                    break
                                try:
                                    User.objects.create_user(email=row['email'], password=row['password'])
                                    self.stdout.write(self.style.SUCCESS(f"User {row['email']} created successfully."))
                                except Exception as e:
                                    self.stderr.write(self.style.ERROR(f"Error creating user {row['email']}: {e}"))
                        return
                except FileNotFoundError as e:
                    self.stderr.write(self.style.ERROR(f'File not found: {CSV_file}'))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error reading CSV file: {e}'))

        if modelName == 'TradespersonProfile':
            if not CSV_file:
                self.stderr.write(self.style.ERROR('CSV file is required for seeding TradespersonProfile data.'))
                return
            import csv
            try:
                with open(CSV_file, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    with transaction.atomic():
                        for row in reader:
                            try:
                                user = User.objects.get(pk=row['user_id'])
                                TradespersonProfile.objects.create(
                                    user=user,
                                    first_name=row['first_name'] if safe_input(row['first_name']) else '',
                                    last_name=row['last_name'] if safe_input(row['last_name']) else '',
                                    other_names=row['other_names'] if safe_input(row['other_names']) else '',
                                    profile_picture=row['profile_picture'] if safe_input(row['profile_picture']) else None,
                                    bio=row['bio'] if safe_input(row['bio']) else '',
                                    tagline=row['tagline'] if safe_input(row['tagline']) else '',
                                    contact_number=row['contact_number'] if safe_input(row['contact_number']) else '',
                                    contact_number2=row['contact_number2'] if safe_input(row['contact_number2']) else '',
                                    gender=row['gender'] if safe_input(row['gender']) else None,
                                    social_links=row['social_links'] if safe_input(row['social_links']) else '',
                                    website=row['website'] if safe_input(row['website']) else '',
                                    date_of_birth=row['date_of_birth'] if safe_input(row['date_of_birth']) else None,
                                    experience_years=int(row['experience_years']) if safe_input(row['experience_years']) else 0,
                                    trade_category=TradeCategory.objects.get(name=row['trade_category']) if safe_input(row['trade_category']) else None,
                                    trade_specialties=TradeSpecialty.objects.filter(name__in=row['trade_specialties']).all() if safe_input(row['trade_specialties']) else None,
                                    skills=TradeSkillTag.objects.filter(name__in=row['skills']).all() if safe_input(row['skills']) else None,
                                    sub_location=Region.objects.get(name=row['sub_location']) if safe_input(row['sub_location']) else None,
                                    availability_status=row['availability_status'] if safe_input(row['availability_status']) else None,
                                    education_schools=row['education_schools'] if safe_input(row['education_schools']) else '',
                                    other_skills=row['other_skills'] if safe_input(row['other_skills']) else '',
                                    rate_charged=float(row['rate_charged']) if safe_input(row['rate_charged']) else 0.0,
                                    is_verified=row['is_verified'].lower() == 'true' if safe_input(row['is_verified']) else False,
                                    is_featured=row['is_featured'].lower() == 'true' if safe_input(row['is_featured']) else False,
                                    is_active=row['is_active'].lower() == 'true' if safe_input(row['is_active']) else False,
                                )
                                self.stdout.write(self.style.SUCCESS(f"TradespersonProfile for user {row['user_id']} created successfully."))
                            except User.DoesNotExist:
                                self.stderr.write(self.style.ERROR(f"User with ID {row['user_id']} does not exist. Skipping row."))
                            except Exception as e:
                                self.stderr.write(self.style.ERROR(f"Error creating TradespersonProfile for user {row['user_id']}: {e}"))
            except FileNotFoundError as e:
                self.stderr.write(self.style.ERROR(f'File not found: {CSV_file}'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error reading CSV file: {e}'))
                
        if modelName == 'ClientProfile':
            if not CSV_file:
                self.stderr.write(self.style.ERROR('CSV file is required for seeding ClientProfile data.'))
                return
            import csv
            try:
                with open(CSV_file, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    with transaction.atomic():
                        for row in reader:
                            try:
                                user = User.objects.get(pk=row['user_id'])
                                ClientProfile.objects.create(
                                    user=user,
                                    first_name=row['first_name'] if safe_input(row['first_name']) else '',
                                    last_name=row['last_name'] if safe_input(row['last_name']) else '',
                                    other_names=row['other_names'] if safe_input(row['other_names']) else '',
                                    profile_picture=row['profile_picture'] if safe_input(row['profile_picture']) else None,
                                    contact_number=row['contact_number'] if safe_input(row['contact_number']) else '',
                                    contact_number2=row['contact_number2'] if safe_input(row['contact_number2']) else '',
                                    gender=row['gender'] if safe_input(row['gender']) else None,
                                    data_of_birth=row['date_of_birth'] if safe_input(row['date_of_birth']) else None,
                                    sub_location=City.objects.get(name=row['sub_location']) if safe_input(row['sub_location']) else None, 
                                    )
                                self.stdout.write(self.style.SUCCESS(f"TradespersonProfile for user {row['user_id']} created successfully."))
                            except User.DoesNotExist:
                                self.stderr.write(self.style.ERROR(f"User with ID {row['user_id']} does not exist. Skipping row."))
                            except Exception as e:
                                self.stderr.write(self.style.ERROR(f"Error creating ClientProfile for user {row['user_id']}: {e}"))
            except FileNotFoundError as e:
                self.stderr.write(self.style.ERROR(f'File not found: {CSV_file}'))
            except Exception as e:  
                self.stderr.write(self.style.ERROR(f'Error reading CSV file: {e}'))

        if modelName == 'Country':
            if not CSV_file:
                self.stderr.write(self.style.ERROR('CSV file is required for seeding Country data.'))
                return
            import csv
            try:
                with open(CSV_file, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    with transaction.atomic():
                        for row in reader:
                            try:
                                Country.objects.create(
                                    name=row['name'] if safe_input(row['name']) else '',
                                    initials=row['initials'] if safe_input(row['initials']) else None,
                                    code=row['code'] if safe_input(row['code']) else '',
                                )
                                self.stdout.write(self.style.SUCCESS(f"Country {row['name']} created successfully."))
                            except Exception as e:
                                self.stderr.write(self.style.ERROR(f"Error creating Country {row['name']}: {e}"))
            except FileNotFoundError as e:
                self.stderr.write(self.style.ERROR(f'File not found: {CSV_file}'))
            except Exception as e:  
                self.stderr.write(self.style.ERROR(f'Error reading CSV file: {e}'))

        if modelName == 'Region':
            if not CSV_file:
                self.stderr.write(self.style.ERROR('CSV file is required for seeding Region data.'))
                return
            import csv
            try:
                with open(CSV_file, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    with transaction.atomic():
                        for row in reader:
                            try:
                                Region.objects.create(
                                    name=row['name'] if safe_input(row['name']) else '',
                                    country=Country.objects.get(name=row['country']) if safe_input(row['country']) else None,
                                )
                                self.stdout.write(self.style.SUCCESS(f"Region {row['name']} created successfully."))
                            except Country.DoesNotExist:
                                self.stderr.write(self.style.ERROR(f"Country with name {row['country']} does not exist. Skipping row."))
                            except Exception as e:
                                self.stderr.write(self.style.ERROR(f"Error creating Region {row['name']}: {e}"))
            except FileNotFoundError as e:
                self.stderr.write(self.style.ERROR(f'File not found: {CSV_file}'))
            except Exception as e:  
                self.stderr.write(self.style.ERROR(f'Error reading CSV file: {e}'))

        if modelName == 'City':
            if not CSV_file:
                self.stderr.write(self.style.ERROR('CSV file is required for seeding City data.'))
                return
            import csv
            try:
                with open(CSV_file, newline='') as csvfile:
                    reader = csv.DictReader(csvfile)
                    with transaction.atomic():
                        for row in reader:
                            try:
                                City.objects.create(
                                    name=row['name'] if safe_input(row['name']) else '',
                                    region=Region.objects.get(name=row['region']) if safe_input(row['region']) else None,
                                )
                            except Region.DoesNotExist:
                                self.stderr.write(self.style.ERROR(f"Region with name {row['region']} does not exist. Skipping row."))
                            except Exception as e:
                                self.stderr.write(self.style.ERROR(f"Error creating City {row['name']}: {e}"))
            except FileNotFoundError as e:
                self.stderr.write(self.style.ERROR(f'File not found: {CSV_file}'))
            except Exception as e:  
                self.stderr.write(self.style.ERROR(f'Error reading CSV file: {e}'))
                