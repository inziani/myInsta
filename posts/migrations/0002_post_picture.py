# Generated by Django 3.1.2 on 2020-10-21 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='static/images/database_login.jpg', upload_to='pictures/'),
        ),
    ]