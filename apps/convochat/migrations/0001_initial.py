# Generated by Django 5.0.8 on 2024-08-28 10:34

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analysis', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(default='Untitled Conversation', max_length=255)),
                ('status', models.CharField(choices=[('AC', 'Active'), ('AR', 'Archived'), ('EN', 'Ended')], default='AC', max_length=2)),
                ('overall_sentiment', models.FloatField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversations', to=settings.AUTH_USER_MODEL)),
                ('dominant_topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='conversations', to='convochat.topic')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('content_type', models.CharField(choices=[('AU', 'Audio'), ('DO', 'Document'), ('IM', 'Image'), ('TE', 'Text')], default='TE', max_length=2)),
                ('is_from_user', models.BooleanField(default=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='convochat.conversation')),
                ('in_reply_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='convochat.message')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='AIText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('confidence_score', models.FloatField(blank=True, null=True)),
                ('recommendation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applied_messages', to='analysis.recommendation')),
                ('message', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ai_text', to='convochat.message')),
            ],
        ),
        migrations.CreateModel(
            name='UserText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('sentiment_score', models.FloatField(blank=True, null=True)),
                ('intent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_text', to='convochat.intent')),
                ('message', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_text', to='convochat.message')),
                ('primary_topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='primary_user_texts', to='convochat.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('PO', 'Positive'), ('NE', 'Negative'), ('NU', 'Neutral')], max_length=2)),
                ('score', models.FloatField()),
                ('granular_category', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detailed_sentiment', to='convochat.usertext')),
            ],
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['conversation', 'created'], name='convochat_m_convers_c28d4c_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['is_from_user', 'created'], name='convochat_m_is_from_bffef1_idx'),
        ),
        migrations.AddIndex(
            model_name='conversation',
            index=models.Index(fields=['user', 'created'], name='convochat_c_user_id_188084_idx'),
        ),
        migrations.AddIndex(
            model_name='conversation',
            index=models.Index(fields=['status'], name='convochat_c_status_9c50cd_idx'),
        ),
    ]
