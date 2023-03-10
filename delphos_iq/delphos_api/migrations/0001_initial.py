# Generated by Django 4.0.3 on 2023-01-07 17:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('country', models.CharField(db_index=True, max_length=50)),
                ('sector', models.CharField(db_index=True, max_length=128)),
                ('amount', models.CharField(db_index=True, max_length=25)),
            ],
        ),
    ]
