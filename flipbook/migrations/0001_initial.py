# Generated by Django 4.0.1 on 2022-01-24 02:51

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFlipbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flipbook_title', models.CharField(max_length=24)),
                ('modified_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('flipbook_document', models.FileField(upload_to='flipbook/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('flipbook_image', models.ImageField(editable=False, upload_to='flipbook/')),
            ],
            options={
                'ordering': ['-modified_date'],
            },
        ),
    ]