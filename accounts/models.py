from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class GerenciadorUsuario(BaseUserManager):
    def criar_usuario(self, matricula, password=None):
        if not matricula:
            raise ValueError("O usuário precisa adicionar uma matrícula.")
        usuario = self.model(matricula=matricula)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def criar_superusuario(self, matricula, password=None):
        usuario = self.criar_superusuario(matricula, password)
        usuario.is_admin = True
        usuario.save(using=self._db)
        return usuario
    
class Usuario(AbstractBaseUser):
    matricula = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = GerenciadorUsuario()

    USERNAME_FIELD = 'matricula'

    def __str__(self):
        return self.matricula
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    



