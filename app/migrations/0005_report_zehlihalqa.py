# Generated by Django 4.2.1 on 2023-06-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_zimmedar_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="zehliHalqa",
            field=models.CharField(default="", max_length=100, null=True),
        ),
    ]
