# Generated by Django 3.1.7 on 2021-02-28 19:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(blank=True, default=None, null=True)),
                ('current_status', models.CharField(blank=True, choices=[('Inquired', 'Inquired'), ('Contacted', 'Contacted'), ('Sold', 'Sold')], default='Inquired', max_length=9, null=True)),
                ('date_sold', models.DateField(blank=True, default=None, null=True)),
                ('notes', tinymce.models.HTMLField(blank=True, default=None, null=True)),
                ('message_from_client', tinymce.models.HTMLField(blank=True, default=None, null=True)),
                ('medium', models.CharField(blank=True, choices=[('Phone call', 'Phone call'), ('Online form', 'Online form'), ('Manually created', 'Manually created')], default='Manually created', max_length=16, null=True, verbose_name='How was the lead generated?')),
                ('phone_number', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('email_address', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('state', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('zip_code', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('street_address', models.CharField(blank=True, default=None, max_length=150, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
