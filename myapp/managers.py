from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.forms import ValidationError

class CustomUserManager(BaseUserManager):

    def get_objects_by_public_id(self,public_id):
        try:
            instanse = self.get(public_id=public_id)
            
            return instanse
        except ObjectDoesNotExist as ex:
           raise Http404("Object Does Not Exist")

        except(ValueError,TypeError, ValidationError):
            raise Http404("Invalid public_id")


    def create_user(self,email,firts_name,last_name,password:None,**extra_fields):
        if email is None:
            raise ValueError("email sizda kiritilmagan")

        if firts_name is None:
            raise ValueError("ismingiz sizda kiritilmagan")   

        if last_name is None:
            raise ValueError("familya sizda kiritilmagan") 

        email = self.normalize_email(email)    

        user = self.model(email=email,firts_name=firts_name,last_name=last_name,**extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self,email,firts_name,last_name,password:None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        return self.create_user(email=email,firts_name=firts_name,last_name=last_name,password=password,**extra_fields)