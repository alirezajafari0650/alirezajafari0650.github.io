# Generated by Django 4.0.3 on 2022-10-21 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('affairs', '0001_initial'),
        ('words', '0012_alter_linkmanager_word'),
        ('kernel', '0006_rename_is_profetional_customuser_is_professional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_affair', models.ManyToManyField(to='affairs.affair')),
                ('liked_words', models.ManyToManyField(to='words.word')),
                (
                'user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
