from django.db import models



class Restaurant(models.Model):
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name + ' : '+ str(self.id)

class MenuItem(models.Model):
	item = models.CharField(max_length=100)
	price = models.IntegerField()
	restaurant = models.ForeignKey(Restaurant)
	def __str__(self):
		return self.item 


class Monument(models.Model):
	name = models.CharField(max_length=200)
	desc = models.TextField()	

	def __str__(self):
		return self.name
