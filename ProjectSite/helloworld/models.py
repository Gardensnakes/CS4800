from django.db import models

class Game(models.Model):
	name = models.CharField(primary_key = True, max_length=50)
	release_date = models.DateTimeField('Date Released')
	discount_price = models.DecimalField(max_digits=6, decimal_places=2)
	current_price = models.DecimalField(max_digits=6, decimal_places=2)
	platform = models.CharField(max_length=20)
	launcher = models.CharField(max_length=20)
	savings_price = models.DecimalField(max_digits=6, decimal_places=2)
	developer = models.CharField(max_length=30)
	publisher = models.CharField(max_length=30)