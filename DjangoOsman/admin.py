from django.contrib import admin
from .models import (Signup,Login,Email,Feedback,Selection,CarType,
                     Customer,Operator,Contact,Accept,Agreeing,Resigning)

admin.site.register(Signup)
admin.site.register(Login)
admin.site.register(Email)
admin.site.register(Feedback)
admin.site.register(Selection)
admin.site.register(CarType)
admin.site.register(Customer)
admin.site.register(Operator)
admin.site.register(Contact)
admin.site.register(Accept)
admin.site.register(Agreeing)
admin.site.register(Resigning)
