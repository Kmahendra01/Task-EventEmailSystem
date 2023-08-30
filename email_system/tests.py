from django.test import TestCase
from .models import EventType, Employee, Event

class EmailSystemTestCase(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name='Birthday')
        self.employee = Employee.objects.create(name='maheek', email='mahee@example.com')
        self.event = Event.objects.create(employee=self.employee, event_type=self.event_type, date='2023-08-21')

    def test_event_creation(self):
        self.assertEqual(self.event.employee, self.employee)
        self.assertEqual(self.event.event_type, self.event_type)
        self.assertEqual(str(self.event), f"{self.employee.name}'s {self.event_type.name} on {self.event.date}")

    def test_email_sent_default(self):
        self.assertFalse(self.event.email_sent)

    # Add more test cases for other functionalities
