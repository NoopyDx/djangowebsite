# Generated by Django 2.1.5 on 2019-01-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formtest', '0002_mail_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail2', models.CharField(max_length=200)),
                ('name2', models.CharField(max_length=50)),
            ],
        ),
    ]
