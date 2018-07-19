# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-18 23:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commentator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_list_of_comments', to='first_app.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_messages', to='first_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message_related',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_for_message', to='first_app.Message'),
        ),
    ]
