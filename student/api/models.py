from django.db import models

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
          db_table = "section"

    def __str__(self):
        return str(self.id)
    
    def save(self,*args,**kwargs):
        super(Section,self).save()
        return self



class Student(models.Model):
     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)
     section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section',null=True,blank=True)
     
     class Meta:
          db_table = "student"

     def __str__(self):
        return str(self.id) + " " + str(self.name)
    
     def save(self,*args,**kwargs):
        super(Student,self).save()
        return self