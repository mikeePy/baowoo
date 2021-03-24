# Generated by Django 3.1.7 on 2021-03-23 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_helper_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.user'),
        ),
    ]
