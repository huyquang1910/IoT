# Generated by Django 4.2.6 on 2023-10-09 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=8, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.account')),
            ],
            options={
                'db_table': 'verify_token',
            },
        ),
        migrations.CreateModel(
            name='JwtToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access', models.TextField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='account_user', to='user.account')),
            ],
            options={
                'db_table': 'jwt_token',
            },
        ),
    ]
