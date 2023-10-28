# Generated by Django 4.2.1 on 2023-10-28 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitymeta',
            name='status',
            field=models.CharField(choices=[('in review', 'in review'), ('published', 'published'), ('accepted', 'accepted'), ('submitted', 'submitted'), ('rejected by user', 'rejected by user'), ('rejected', 'rejected')], max_length=255),
        ),
        migrations.AlterField(
            model_name='communityrequests',
            name='status',
            field=models.CharField(choices=[('approved', 'approved'), ('rejected', 'rejected'), ('pending', 'pending')], max_length=10),
        ),
    ]