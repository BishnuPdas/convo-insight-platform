# Generated by Django 5.0.8 on 2024-08-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_conversationmetrics_sentiment_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='llmagentperformance',
            name='overall_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
