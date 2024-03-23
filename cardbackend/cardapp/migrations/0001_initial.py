# Generated by Django 5.0.3 on 2024-03-23 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Numero')),
                ('credit', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='Credito Total')),
                ('name_of_owner', models.CharField(max_length=120, verbose_name='Nombres')),
                ('email_of_owner', models.CharField(max_length=120, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono')),
                ('type_of_card', models.CharField(choices=[('VISA', 'Visa'), ('MASTERCARD', 'Mastercard'), ('AMEX', 'Amex')], default='VISA', max_length=10, verbose_name='Tipo de documento')),
            ],
            options={
                'verbose_name': 'Card',
                'verbose_name_plural': 'Cards',
                'db_table': 'card',
                'ordering': ['id'],
            },
        ),
    ]
