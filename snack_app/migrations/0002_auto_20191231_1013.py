# Generated by Django 2.2.5 on 2019-12-31 10:13

from django.db import migrations, models
import django.db.models.deletion
import snack_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('snack_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='friend',
            name='name',
            field=models.CharField(max_length=100, validators=[snack_app.models.number_only]),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snack_app.Friend')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
