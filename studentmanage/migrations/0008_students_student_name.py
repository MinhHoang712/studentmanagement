# Generated by Django 4.0.1 on 2022-12-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentmanage', '0007_staffs_staff_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='student_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
