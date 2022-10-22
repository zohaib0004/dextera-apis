# from django.db import models

# class State(models.Model):
#     name = models.CharField(max_length=255)
#     abb = models.CharField(max_length=5)
    
#     def __str__(self):
#         return self.name

# class County(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="county", )
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name
    

# class City(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="city")
#     county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="city")
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name

# class ZipCode(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="zipcode")
#     county = models.ForeignKey(County, on_delete=models.CASCADE, related_name="zipcode")
#     city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="zipcode")
#     zip_code = models.PositiveIntegerField(default=11111)
#     count = models.PositiveIntegerField(default=4)

#     def __str__(self):
#         return self.city + " " + self.county + " " + self.state
