# Generated by Django 2.0.4 on 2018-04-19 17:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('job_portal', '0012_auto_20180419_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businesstype',
            old_name='added',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='businesstype',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='added',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
