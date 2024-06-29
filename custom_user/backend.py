from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.db.models.base import Model
from django.contrib.auth import get_user_model

User = get_user_model()

class UsernameOrEmail(ModelBackend):
    def authenticate(self, request, username=None,  password = None, **kwargs):
        try:
            user = User.objects.get(Q(user_name__iexact=username) | Q(email__iexact=username))
           
        except User.DoesNotExist:
            User().set_password(password)
            return
                
        except User.MultipleObjectsReturned:
           user = User.objects.filter(Q(user_name__iexact=username) | Q(email__iexact=username)).order_by('id').first()
          
       
        if user.check_password(password) and self.user_can_authenticate(user):
           
            return user