from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from datetime import date
from email_system.models import Event  # Import your Event model


class Command(BaseCommand):
    help = 'Send automated event emails'

    def add_arguments(self, parser):
        parser.add_argument('email', nargs='+', type=str, help='Recipient email addresses')

    def handle(self, *args, **options):
        recipients = options['email']

        if not recipients:
            self.stderr.write(
                self.style.ERROR('No email addresses provided. Use: python manage.py sendtestemail email@example.com'))
            return

        events_today = Event.objects.filter(event_date=date.today())

        for event in events_today:
            employee = event.employee
            event_type = event.event_type
            template = event_type.template

            subject = f'Event Reminder: {event_type.name}'
            message = template.format(employee_name=employee.name)
            from_email = 'mahendrakawade07@gmail.com'

            try:
                send_mail(subject, message, from_email, recipients)
                self.stdout.write(self.style.SUCCESS(f'Successfully sent email to {employee.name}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error sending email to {employee.name}: {str(e)}'))


