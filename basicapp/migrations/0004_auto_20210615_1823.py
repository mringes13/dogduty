# Generated by Django 3.2.2 on 2021-06-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0003_alter_event_reporter'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='activity',
            field=models.CharField(choices=[('Peed', 'Peed'), ('Poop', 'Poop'), ('Walk', 'Walk'), ('Ate', 'Ate'), ('Medicine', 'Medicine'), ('Nothing', 'Nothing')], default='', max_length=20),
        ),
    ]