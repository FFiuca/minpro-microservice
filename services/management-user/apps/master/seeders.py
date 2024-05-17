from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry # if your pylance not auto discover lib. you can check Lib in venv and search your lib you want.
from .models import Status

@SeederRegistry.register
class StatusSeeder(seeders.ModelSeeder):
    id = 'StatusSeeder'
    priopity = 1
    model = Status
    data = [
        {
            'status_name': 'Active'
        },
        {
            'status_name': 'Non Active'
        }
    ]
