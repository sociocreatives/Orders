# Generated by Django 3.2.7 on 2022-09-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_faq_partners_terms'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pictures/%Y/%m/%d/'),
        ),
    ]