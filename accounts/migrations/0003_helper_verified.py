# Generated by Django 3.1.7 on 2021-03-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_helper'),
    ]

    operations = [
        migrations.AddField(
            model_name='helper',
            name='verified',
            field=models.CharField(choices=[('Yes', 'Verified.'), ('No', 'Not Verified')], default='No', max_length=222),
        ),
    ]
