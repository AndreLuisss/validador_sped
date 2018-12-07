# Generated by Django 2.1.4 on 2018-12-07 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('participantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IND_OPER', models.BooleanField()),
                ('IND_EMIT', models.BooleanField()),
                ('COD_MOD', models.CharField(max_length=2)),
                ('COD_SIT', models.CharField(max_length=2)),
                ('SER', models.CharField(max_length=3)),
                ('NUM_DOC', models.CharField(max_length=9)),
                ('CHV_NFE', models.CharField(max_length=44)),
                ('DT_DOC', models.DateField()),
                ('DT_E_S', models.DateField()),
                ('VL_DOC', models.FloatField()),
                ('IND_PGTO', models.CharField(max_length=1)),
                ('VL_DESC', models.FloatField(default=0.0)),
                ('VL_ABAT_NT', models.FloatField(default=0.0)),
                ('VL_MERC', models.FloatField(default=0.0)),
                ('IND_FRT', models.CharField(default=0, max_length=1)),
                ('VL_FRT', models.FloatField(default=0.0)),
                ('VL_SEG', models.FloatField(default=0.0)),
                ('VL_OUT_DA', models.FloatField(default=0.0)),
                ('VL_BC_ICMS', models.FloatField(default=0.0)),
                ('VL_ICMS', models.FloatField(default=0.0)),
                ('VL_BC_ICMS_ST', models.FloatField(default=0.0)),
                ('VL_ICMS_ST', models.FloatField(default=0.0)),
                ('VL_IPI', models.FloatField(default=0.0)),
                ('VL_PIS', models.FloatField(default=0.0)),
                ('VL_COFINS', models.FloatField(default=0.0)),
                ('VL_PIS_ST', models.FloatField(default=0.0)),
                ('VL_COFINS_ST', models.FloatField(default=0.0)),
                ('COD_PART', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='participantes.Participantes')),
            ],
        ),
    ]
