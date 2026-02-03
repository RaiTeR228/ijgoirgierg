from django.db import models

# Название класса это название таблицы, в данном случии Product
class Product(models.Model):
    #название переменной это название столбика
    name_car = models.CharField(max_length=100, verbose_name="Название машины") #название машины
    horses = models.DecimalField(max_digits=10,decimal_places=2, verbose_name="Мощность в лошадиных силах") # Мощность в лошадиных силах
    in_stock = models.BooleanField(default=True, verbose_name="В наличии") #в наличии
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    #Создаем метод
    def apply_discount(self,percent):
        #применяем скидку
        self.price = self.price*(100-percent)/100
        self.save ()
