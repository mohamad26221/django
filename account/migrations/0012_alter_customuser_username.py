# Generated by Django 5.0.2 on 2024-03-03 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]