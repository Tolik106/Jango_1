# Generated by Django 4.2.6 on 2023-10-06 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_scope_delete_articletag_alter_tag_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scope',
            old_name='scope',
            new_name='tag',
        ),
    ]
