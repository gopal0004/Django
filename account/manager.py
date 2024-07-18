from django.contrib.auth.base_user import BaseUserManager




class UserManager(BaseUserManager):

    def create_user(self , phone_number , password = None , **extra_feilds):
        if not phone_number:
            raise ValueError("phone number is required")

        email = extra_feilds.get('email')
        if email:
            extra_feilds['email'] = self.normalize_email(email)

        user = self.model(phone_number = phone_number , **extra_feilds)
        user.set_password(password)
        user.save(using = self.db)

        return user


    def create_superuser(self , phone_number , password = None , **extra_feilds):
        extra_feilds.setdefault('is_staff' , True)
        extra_feilds.setdefault('is_active' , True)
        extra_feilds.setdefault('is_superuser' , True)

        return self.create_user(phone_number , password , **extra_feilds)