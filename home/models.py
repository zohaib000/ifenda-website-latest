from django.db import models





class Individual_Pricing(models.Model):
     product_name=models.CharField(max_length=20000)
     product_plan=models.CharField(max_length=20000) 
     plan_type=models.CharField(max_length=20000) 
     orignal_price=models.DecimalField(max_digits=50,decimal_places=2)
     sell_price=models.DecimalField(max_digits=50,decimal_places=2)
     discount=models.DecimalField(max_digits=50,decimal_places=2)
     vat_price=models.DecimalField(max_digits=50,decimal_places=2)
     total_price=models.DecimalField(max_digits=50,decimal_places=2) # final price_
    
     
class Business_Pricing(models.Model):
     product_name=models.CharField(max_length=20000)
     plan_type=models.CharField(max_length=20000) 
     orignal_price=models.DecimalField(max_digits=50,decimal_places=2)
     sell_price=models.DecimalField(max_digits=50,decimal_places=2)
     discount=models.DecimalField(max_digits=50,decimal_places=2)
     vat_price=models.DecimalField(max_digits=50,decimal_places=2)
     total_price=models.DecimalField(max_digits=50,decimal_places=2) # final price_
     orignal_cost_per_extra=models.DecimalField(max_digits=50,decimal_places=5)
     current_cost_per_extra=models.DecimalField(max_digits=50,decimal_places=5)
    
     