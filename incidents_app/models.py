from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Utilisateur(AbstractUser):
    ROLES=(('Adminstrateur','Adminstrateur'),('Citoyen','Citoyen'))
    role=models.CharField(max_length=15 , choices=ROLES)
    
    def __str__(self):
        return f'{self.username} - {self.role}'
    
    
class Catagorie(models.Model):
    Catagories_choices=(('incendie','incendie'),
                        ('accident', 'accident'),
                        ('poublles','poublles'),
                        ('fuites d\'eau','fuites d\'eau'))
    id_catagorie=models.AutoField(primary_key=True),
    nome=models.CharField(choices=Catagories_choices , max_length=12 , default='incendie')
    
    def __str__(self):
        return self.nome
    
    
    
class Incident(models.Model):
    
    etat_choices=(('En attante','En attante'),('traite','traite'))
    
    longitude=models.FloatField()
    latitude=models.FloatField()
    photo_incident = models.ImageField(upload_to='media/', blank=True)
    descriptions_text= models.TextField(max_length=400 , blank=True)
    descriptions_vocal=models.FileField(upload_to='media/' , blank=True)
    etat=models.CharField(max_length=12 , choices=etat_choices)
    date_creation=models.DateTimeField(auto_now_add=True)
    catagorie=models.ForeignKey(Catagorie ,on_delete=models.SET_DEFAULT ,default='non determine')
    user = models.ForeignKey('Utilisateur', on_delete=models.CASCADE)
    
    
