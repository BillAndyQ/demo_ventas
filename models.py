# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    id_negocio = models.ForeignKey('Negocios', models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    id_negocio = models.ForeignKey('Negocios', models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    id_negocio = models.ForeignKey('Negocios', models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boleta'


class DetalleVentas(models.Model):
    id_detalle_venta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_negocio = models.ForeignKey('Negocios', models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)
    id_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='id_venta', blank=True, null=True)
    nombre_producto = models.TextField(blank=True, null=True)
    precio_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cantidadxprod = models.IntegerField(db_column='cantidadXprod', blank=True, null=True)  # Field name made lowercase.
    precio_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_ventas'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    id_negocio = models.ForeignKey('Negocios', models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factura'


class Negocios(models.Model):
    id_negocio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    ruc = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'negocios'


class NegociosUsers(models.Model):
    id_negocios_user = models.AutoField(primary_key=True)
    id_negocio = models.ForeignKey(Negocios, models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'negocios_users'


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=True, null=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)
    codigo_qr = models.TextField(blank=True, null=True)
    codigo_bar = models.TextField(blank=True, null=True)
    id_negocio = models.ForeignKey(Negocios, models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class Serie(models.Model):
    id_serie = models.AutoField(primary_key=True)
    tipo_serie = models.CharField(max_length=20, blank=True, null=True)
    serie = models.CharField(max_length=5, blank=True, null=True)
    id_negocio = models.ForeignKey(Negocios, models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)
    ultimo_num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serie'


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    ids_detalles = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha_hora = models.DateTimeField(blank=True, null=True)
    nombre_cliente = models.CharField(max_length=120, blank=True, null=True)
    dni_ruc = models.IntegerField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    tipo_comprobante = models.CharField(max_length=20, blank=True, null=True)
    metodo_pago = models.CharField(max_length=30, blank=True, null=True)
    id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='id_boleta', blank=True, null=True)
    id_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='id_factura', blank=True, null=True)
    id_serie = models.ForeignKey(Serie, models.DO_NOTHING, db_column='id_serie', blank=True, null=True)
    id_negocio = models.ForeignKey(Negocios, models.DO_NOTHING, db_column='id_negocio', blank=True, null=True)
    numero_serie = models.BigIntegerField(blank=True, null=True)
    total_venta = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'
