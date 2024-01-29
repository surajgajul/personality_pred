# Generated by Django 3.2.3 on 2024-01-28 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('per', '0002_delete_applicant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('personality', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('openness', models.IntegerField()),
                ('neuroticism', models.IntegerField()),
                ('conscientiousness', models.IntegerField()),
                ('agreeableness', models.IntegerField()),
                ('extraversion', models.IntegerField()),
            ],
        ),
    ]