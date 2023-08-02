# webapp_model
## ความรู้ที่ได้
### 1. การติดตั้ง __django__.<br>
```python
pip install django
```

### 2. การสร้างบัญชี admin
```python
pythom manage.py createsuperuser
```

### 3. การตั้งค่า urls
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
```

### 4. การสร้าง folder templates และ statics
#### >> เพื่อที่จะสร้าง page home,about,contect   
![image](https://github.com/Porpathom/my-webapp-model/blob/main/immage/page.png)
![image]()

### 5. การใช้ prefix choices และ django model 
```python
from django.db import models

prefix_choices = (
    (1, "นาย"),
    (2, "นางสาว"),
    (3, "นาง"),
)


class Student(models.Model):
    std_id = models.IntegerField()
    prefix = models.IntegerField(choices=prefix_choices, default=1)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reversed("Student_detail", kwargs={"pk": self.pk})

```
### 6. Screen Capture 
![image]()
