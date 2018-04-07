# Generated by Django 2.0.4 on 2018-04-07 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.TextField()),
                ('office_address', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('total_employee', models.IntegerField()),
                ('year_established', models.IntegerField()),
                ('business_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_portal.BusinessType')),
            ],
        ),
    ]