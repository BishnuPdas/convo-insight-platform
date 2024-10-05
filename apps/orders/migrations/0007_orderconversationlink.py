# Generated by Django 5.0.8 on 2024-10-02 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convochat', '0001_initial'),
        ('orders', '0006_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderConversationLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_links', to='convochat.conversation')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_links', to='orders.order')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('order', 'conversation')},
            },
        ),
    ]