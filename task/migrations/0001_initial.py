# Generated by Django 4.2.7 on 2023-11-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=150, null=True)),
                ('status', models.CharField(choices=[('TODO', 'Todo'), ('DONE', 'Done')], default='TODO', max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(null=True)),
            ],
        ),
    ]