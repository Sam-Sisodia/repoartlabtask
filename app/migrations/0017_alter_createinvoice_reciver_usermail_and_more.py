# Generated by Django 4.1.3 on 2022-11-24 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_createinvoice_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createinvoice',
            name='reciver_usermail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='createinvoice',
            name='send_usermail',
            field=models.EmailField(max_length=254),
        ),
    ]