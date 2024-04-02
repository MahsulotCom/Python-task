# Generated by Django 5.0.3 on 2024-04-02 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_remove_product_category_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_categories', to='store.category'),
        ),
    ]
