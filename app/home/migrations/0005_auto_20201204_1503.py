# Generated by Django 3.1.2 on 2020-12-04 12:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_posts_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
