# Generated by Django 3.0 on 2020-09-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr', '0002_auto_20200928_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[('terrible', 'Terrible'), ('poor', 'Poor'), ('average', 'Average'), ('verygood', 'Very Good'), ('excellent', 'Excellent')]),
        ),
    ]
