# Generated by Django 4.1.4 on 2023-07-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuturaApp', '0006_message_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=250)),
                ('ques_name', models.CharField(max_length=250)),
                ('ques_ans', models.CharField(max_length=250)),
            ],
        ),
    ]
