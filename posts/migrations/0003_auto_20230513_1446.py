# Generated by Django 3.2.19 on 2023-05-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='country_choices',
            field=models.CharField(choices=[('India', 'India'), ('China', 'China'), ('United States', 'United States'), ('Nigeria', 'United States'), ('Brazil', 'Brazil'), ('Bangladesh', 'Bangladesh'), ('Pakistan', 'Pakistan'), ('Indonesia', 'Indonesia'), ('Mexico', 'Mexico'), ('Russia', 'Russia'), ('Japan', 'Japan'), ('Philippines', 'Philippines'), ('Ethiopoa', 'Ethiopoa'), ('United Kingdom', 'United Kingdom'), ('Germany', 'Germany'), ('Egypt', 'Egypt'), ('Tanzania', 'Tanzania'), ('Iran', 'Iran'), ('Thailand', 'Thailand'), ('France', 'France'), ('South Korea', 'South Korea'), ('Sudan', 'Sudan'), ('Algeria', 'Algeria'), ('South Africa', 'South Africa'), ('Angola', 'Angola'), ('Peru', 'Peru'), ('Saudi Arabia', 'Saudi Arabia'), ('Myanmar', 'Myanmar'), ('Canada', 'Canada'), ('Argentina', 'Argentina'), ('Poland', 'Poland'), ('Ghana', 'Ghana'), ('Madagascar', 'Madagascar'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Uganda', 'Uganda'), ('Chad', 'Chad'), ('Libya', 'Libya'), ('Mali', 'Mali'), ('Mauritania', 'Mauritania'), ('Niger', 'Niger'), ('Nepal', 'Nepal'), ('Yemen', 'Yemen'), ('Uzbekistan', 'Uzbekistan'), ('Malaysia', 'Malaysia'), ('Iraq', 'Iraq'), ('Afghanistan', 'Afghanistan'), ('Burundi', 'Burundi'), ('Rwanda', 'Rwanda'), ('Bolivia', 'Bolivia')], default='normal', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]