from django.db import models

# Create your models here.

class Writer:
    def __init__(self,name1,name2):
        self.first_name = name1
        self.last_name = name2

    def displayBothNames(self):
        return self.first_name + "" + self.last_name

    def __str__(self):
        return self.first_name     


    



