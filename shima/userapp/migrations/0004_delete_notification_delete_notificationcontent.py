# Generated by Django 4.2.4 on 2023-08-23 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_notificationcontent_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.DeleteModel(
            name='NotificationContent',
        ),
    ]