# Generated by Django 4.0.1 on 2022-01-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0002_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments'),
        ),
    ]