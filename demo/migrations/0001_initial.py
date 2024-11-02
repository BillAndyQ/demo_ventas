# Generated by Django 4.2.16 on 2024-11-02 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleVentas',
            fields=[
                ('id_detalle_venta', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'detalle_ventas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'factura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Negocios',
            fields=[
                ('id_negocio', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('ruc', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'negocios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NegociosUsers',
            fields=[
                ('id_negocios_user', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'negocios_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=200, null=True)),
                ('precio_venta', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('codigo_qr', models.TextField(blank=True, null=True)),
                ('codigo_bar', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id_serie', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_serie', models.CharField(blank=True, max_length=20, null=True)),
                ('serie', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'serie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('ids_detalles', models.TextField(blank=True, null=True)),
                ('fecha_hora', models.DateTimeField(blank=True, null=True)),
                ('nombre_cliente', models.CharField(blank=True, max_length=120, null=True)),
                ('dni_ruc', models.IntegerField(blank=True, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('tipo_comprobante', models.CharField(blank=True, max_length=20, null=True)),
                ('metodo_pago', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'venta',
                'managed': False,
            },
        ),
    ]