# Generated by Django 5.0.2 on 2024-03-03 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_alter_customuser_job_alter_customuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='token',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='typejob',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
