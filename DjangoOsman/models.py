from django.db import models

class Signup(models.Model):
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField( max_length=30,blank=True, null=True)
    last_name=models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Login(models.Model):
      user_name=models.CharField(max_length=30)
      password=models.CharField()

      def __str__(self):
          return self.user_name
      
class Email(models.Model):
      email=models.CharField(max_length=40)
      birth_day_time=models.CharField(max_length=40)

      def __str__(self):
          return self.email

class  Feedback(models.Model):
        massage=models.TextField()

        def __str__(self):
            return self.massage

class Selection(models.Model):
       bike=models.CharField(max_length=30)
       car=models.CharField(max_length=30)
       boat=models.CharField(max_length=30)

       def __str__(self):
           return f"{self.bike} : {self.car} : {self.boat}"

class CarType(models.Model):
      name = models.CharField(max_length=30)

      def __str__(self):
          return self.name


class Customer(models.Model):
      customer_name=models.CharField(max_length=30)
      bin=models.CharField(max_length=4)

      def __str__(self):
          return self.customer_name

class Operator(models.Model):
      operator=models.CharField(max_length=30)
      operator_level=models.CharField(max_length=30)

      def __str__(self):
          return self.operator

class Contact(models.Model):
      Phone=models.CharField(max_length=30)

      def __str__(self):
          return self.Phone

class Accept(models.Model):
      student=models.CharField(max_length=30)
      grade=models.CharField(max_length=30)

      def __str__(self):
          return self.student


class Resigning(models.Model):
      staff=models.CharField(max_length=30)
      level=models.CharField(max_length=30)

      def __str__(self):
          return self.staff


class Agreeing(models.Model):
      employee=models.CharField(max_length=30)
      manager=models.CharField(max_length=30)
      area=models.CharField(max_length=30)

      def __str__(self):
          return self.employee

