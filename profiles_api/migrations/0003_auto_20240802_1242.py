# Generated by Django 2.2 on 2024-08-02 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='state_text',
            new_name='status_text',
        ),
    ]