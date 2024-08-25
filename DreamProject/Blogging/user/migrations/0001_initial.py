# Generated by Django 3.2.4 on 2021-10-05 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorid', models.CharField(max_length=100)),
                ('blogcategory', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=600)),
                ('attachment', models.ImageField(default='', upload_to='static/blogattach/')),
                ('thumbnail', models.ImageField(default='', upload_to='static/blogthumb/')),
                ('bdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('cimage', models.ImageField(default='', upload_to='static/category/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=400)),
                ('college', models.CharField(max_length=400)),
                ('pic', models.ImageField(default='', upload_to='static/profile/')),
            ],
        ),
    ]
