# Generated by Django 3.2.7 on 2021-10-01 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserId', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=150)),
                ('LastName', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=350)),
                ('password', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]