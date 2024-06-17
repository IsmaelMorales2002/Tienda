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

