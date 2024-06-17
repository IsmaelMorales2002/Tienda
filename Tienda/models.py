from django.db import models

# Create your models here.
class Usuario(models.Model):
        correo = models.CharField(max_length=50,primary_key=True,verbose_name='Correo Usuario')
        primerNombre = models.CharField(max_length=30,verbose_name='Primer Nombre')
        segundoNombre = models.CharField(max_length=30,verbose_name='Segundo Nombre',blank=True,null=True)
        primerApellido = models.CharField(max_length=30,verbose_name='Primer Apellido',blank=True,null=True)
        segundoApellido = models.CharField(max_length=30,verbose_name='Segundo Apellido',blank=True,null=True)
        dui = models.CharField(max_length=11,verbose_name="DUI",blank=True,null=True)
        direccion = models.CharField(max_length=50,verbose_name='Direccion',blank=True,null=True)
        password = models.CharField(max_length=10,verbose_name="Contraseña",blank=True,null=True)
        imagen = models.ImageField(upload_to='usuarios/',verbose_name="Fotografia",blank=True,null=True)
        tipo = models.CharField(max_length=1,verbose_name='Tipo De Usuario',blank=True,null=True)

        def __str__(self):
            texto = "{0}"
            return texto.format(self.correo)
    
        class Meta:
            db_table = 'Usuario'
            verbose_name = 'Usuario'
            verbose_name_plural = 'Usuarios'

class Pago(models.Model):
    idPago = models.IntegerField(auto_created=True,verbose_name='Id Pago',primary_key=True)
    correo = models.ForeignKey(Usuario, verbose_name="Correo Usuario", on_delete=models.RESTRICT)
    monto = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Total Pago')

    def __str__(self):
         texto = "Total: {0} Correo: {1}"
         return texto.format(self.monto,self.correo)
    
    class Meta:
        db_table = 'Pago'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
     
class Carrito(models.Model):
     idCarrito = models.IntegerField(auto_created=True,verbose_name="Id Carrito",primary_key=True)
     correo = models.ForeignKey(Usuario,on_delete=models.RESTRICT,verbose_name="Correo Usuario")
     total = models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Total Carrito")

     def __str__(self):
          texto = "Total: {0} Correo:{1}"
          return texto.format(self.monto,self.correo)
     
     class Meta:
        db_table = 'Carro'
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

class Factura(models.Model):
     idFactura = models.IntegerField(auto_created=True,primary_key=True,verbose_name='Id Factura')
     idPago = models.ForeignKey(Pago,on_delete=models.RESTRICT,verbose_name="Id Pago")
     idCarro = models.ForeignKey(Carrito,on_delete=models.RESTRICT,verbose_name='Id Carro')
     totalFactura = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Total Factura')
     fechaFactura = models.DateField(verbose_name='Fecha')

     def __str__(self):
          texto = "Total: {0}"
          return texto.format(self.totalFactura)
     
     class Meta:
        db_table = 'Factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


class Producto(models.Model):
     idProducto = models.IntegerField(auto_created=True,primary_key=True,verbose_name='Id Producto')
     correo = models.ForeignKey(Usuario,on_delete=models.RESTRICT,verbose_name='Correo Usuario')
     nombreProducto = models.CharField(max_length=30,verbose_name='Nombre Del Producto')
     precio = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Precio Unitario')
     existencia = models.IntegerField()
     imagen = models.ImageField(upload_to='productos/',verbose_name='Imagen del Producto')

     def __str__(self):
          texto = "Nombre Producto: {0} Existencia: {1}"
          return texto.format(self.nombreProducto,self.existencia)
     
     class Meta:
        db_table = 'Producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class Detalle_Producto(models.Model):
     idCarrito = models.ForeignKey(Carrito,on_delete=models.RESTRICT,verbose_name='Id Carro')
     idProducto = models.ForeignKey(Producto,on_delete=models.RESTRICT,verbose_name='Producto')
     cantidadProducto = models.IntegerField(verbose_name='Cantidad de Productos')

     def __str__(self):
          texto = "Cantidad: {0} Producto {1}"
          return texto.format(self.cantidadProducto,self.idProducto)
     
     class Meta:
        db_table = 'Detalle_Producto'
        verbose_name = 'Detalle_Producto'
        verbose_name_plural = 'Detalle_Productos'


class Proveedor(models.Model):
     idProveedor = models.IntegerField(auto_created=True,primary_key=True,verbose_name='Id Proveedor')
     correo = models.ForeignKey(Usuario,on_delete=models.RESTRICT,verbose_name='Correo Usuario')
     nombreProveedor = models.CharField(max_length=30,verbose_name='Nombre Producto')

     def __str__(self):
          texto = "Correo: {0} Nombre Producto: {1}"
          return texto.format(self.correo,self.nombreProveedor)
     
     class Meta:
        db_table = 'Proveedor'
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


class Detalle_Compra(models.Model):
    idProducto = models.ForeignKey(Producto,verbose_name='Id Producto',on_delete=models.RESTRICT)
    idProveedor = models.ForeignKey(Proveedor,verbose_name='Id Proveedor',on_delete=models.RESTRICT)
    cantidadCompra = models.IntegerField(auto_created=True,verbose_name='Cantidad Comprada')
    fechaCompra = models.DateField(verbose_name='Fecha de Compra')

    def __str__(self):
        texto = "Cantidad: {0}  Fecha Compra: {1}"
        return texto.format(self.cantidadCompra,self.fechaCompra)
     
    class Meta:
        db_table = 'Detalle_Compra'
        verbose_name = 'Detalle_Compra'
        verbose_name_plural = 'Detalle_Compras'



