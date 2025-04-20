from django.db import models

# Create your models here.
class Catagorie(models.Model):
    Catagories_choices=(('incendie','incendie'),
                        ('accident', 'accident'),
                        ('poublles','poublles'),
                        ('fuites d\'eau','fuites d\'eau'))
    id_catagorie=models.AutoField(primary_key=True),
    nome=models.CharField(choices=Catagories_choices , max_length=12 , default='incendie')
    
    
    
class Incident(models.Model):
    
    etat_choices=(('En attante','En attante'),('traitee','traitee'))
    photo_incident = models.ImageField(upload_to='media/images_incidents'),
    descriptions_text= models.TextField(max_length=400),
    descriptions_vocal=models.FileField(upload_to='media/audio_incidents'),
    etat=models.CharField(max_length=12 , choices=etat_choices)
    date_creation=models.DateTimeField(auto_now_add=True)
    catagorie=models.ForeignKey(Catagorie ,on_delete=models.SET_DEFAULT ,default='non determine')