# Generated by Django 5.0.2 on 2024-03-03 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_customuser_city_alter_customuser_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='job',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
