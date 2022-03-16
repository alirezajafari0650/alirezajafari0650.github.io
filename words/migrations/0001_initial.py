# Generated by Django 4.0.3 on 2022-03-16 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(blank=True, null=True, upload_to='icon/')),
                ('sort_id', models.IntegerField(default=0)),
                ('farsi_name', models.CharField(blank=True, max_length=50, null=True)),
                ('english_name', models.CharField(blank=True, max_length=50, null=True)),
                ('arabic_name', models.CharField(blank=True, max_length=50, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='words.wordcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farsi_name', models.CharField(blank=True, max_length=50, null=True)),
                ('farsi_description', models.CharField(blank=True, max_length=256, null=True)),
                ('farsi_description2', models.CharField(blank=True, max_length=256, null=True)),
                ('english_name', models.CharField(blank=True, max_length=50, null=True)),
                ('english_description', models.CharField(blank=True, max_length=256, null=True)),
                ('english_description2', models.CharField(blank=True, max_length=256, null=True)),
                ('arabic_name', models.CharField(blank=True, max_length=50, null=True)),
                ('arabic_description', models.CharField(blank=True, max_length=256, null=True)),
                ('arabic_description2', models.CharField(blank=True, max_length=256, null=True)),
                ('sort_id', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.wordcategory')),
            ],
        ),
    ]
