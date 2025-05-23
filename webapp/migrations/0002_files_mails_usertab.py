# Generated by Django 4.2.20 on 2025-04-08 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=49)),
                ('username', models.CharField(max_length=49)),
                ('filename', models.CharField(max_length=149)),
                ('filetitle', models.CharField(max_length=149)),
                ('access', models.CharField(max_length=149)),
                ('filedata', models.TextField()),
                ('stz', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=49)),
                ('sendername', models.CharField(max_length=49)),
                ('recipient', models.CharField(max_length=149)),
                ('title', models.CharField(max_length=149)),
                ('data', models.CharField(max_length=149)),
                ('datetime', models.CharField(max_length=149)),
            ],
        ),
        migrations.CreateModel(
            name='usertab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_a_m_e', models.CharField(max_length=149)),
                ('e_mail', models.CharField(max_length=149)),
                ('pass_word', models.CharField(max_length=149)),
                ('phone', models.CharField(max_length=149)),
                ('role', models.CharField(max_length=149)),
            ],
        ),
    ]
