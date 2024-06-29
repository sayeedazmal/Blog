from django import forms
from .models import CustomUser
from ckeditor.fields import RichTextField
from web_blog.models import Post


class UserLoginFrom(forms.Form):
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
   class Meta:
      model = CustomUser
      fields = ("user_name","email","password",)

      def clean_user_name(self):
            username = self.cleaned_data.get('user_name')
            model = self.Meta.model
            user = model.objects.filter(username_iexact=username)
           
            if user.exists():
                raise forms.ValidationError("A user All ready exists")
            return self.cleaned_data.get('username')
      
      def clean_email(self):
            email = self.cleaned_data.get('email')
            model = self.Meta.model
            user = model.objects.filter(email_iexact=email)
            if user.exists():
             raise forms.ValidationError("A user All ready exists")
            return self.cleaned_data.get('email')
      def clean_password(self):
            password = self.cleaned_data.get('password')
            confirm_pass = self.data.get('confirm_password')

            if password != confirm_pass:
                
                raise forms.ValidationError("Password do not match")
            return self.cleaned.data.get('password')

class UserUpdateProfile(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","user_name","email",)

        def clean_user_name(self):
                username = self.cleaned_data.get('user_name')
                model = self.Meta.model
                user = model.objects.filter(username_iexact=username).exclude(pk=self.instance.pk)
                if user.exists():
                    raise forms.ValidationError("A user All ready exists")
                return self.cleaned_data.get('username')
        
        def clean_email(self):
                email = self.cleaned_data.get('email')
                model = self.Meta.model
                user = model.objects.filter(email_iexact=email).exclude(pk=self.instance.pk)
                if user.exists():
                    raise forms.ValidationError("A user All ready exists")
                return self.cleaned_data.get('email')
      
    def change_password(self):
        if 'new_password' in self.data and 'confirm_password' in self.data:
            new_password = self.data['new_password']
            confirm_password = self.data['confirm_password']
            
            if new_password != '' and confirm_password !='':
                if new_password != confirm_password:
                    raise forms.ValidationError("password do not match")
                else:
                    self.instance.set_password(new_password)
                    self.instance.save()
        
    def clean(self):
        self.change_password()

class ProfilePictureUpdate(forms.Form):
    profile_picture = forms.ImageField(required=True)

class BlogForm(forms.ModelForm):
    description = RichTextField()
    class Meta:
        model = Post
        fields = (
            'post_title',
            'category',
            'banner',
            'description',
        )