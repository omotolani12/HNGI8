# Generated by Django 3.2.6 on 2021-08-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('message', models.TextField()),
            ],
        ),
    ]
