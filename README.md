# webapp_model
## ความรู้ที่ได้
### 1. การติดตั้ง __django__.<br>
```python
pip install django
```
### 2. เริ่มโปรเจคและแอป
```python
pythom manage.py startproject
```
```python
pythom manage.py startapp
```

### 3. การสร้างบัญชี admin
```python
pythom manage.py createsuperuser
```
### 4. การทดลองรัน server
```python
pythom manage.py runserver
```
### 5. การสร้างไฟล์ requirements.txt 
#### >> เพื่อติดตั้งโปรแกรมต่างๆ ที่จะใช้

```python
pip install -r requirements.txt
```
![image](https://github.com/Porpathom/my-webapp-model/blob/main/immage/re.png)

### 6. การตั้งค่า urls
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]
```

### 7. การสร้าง folder templates และ statics
#### >> เพื่อที่จะสร้างหน้า page home/about/contect   
![image](https://github.com/Porpathom/my-webapp-model/blob/main/immage/page.png)
![image](https://github.com/Porpathom/my-webapp-model/blob/main/immage/tem.png)

### 8. การใช้ prefix choices และ django model 
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
### 9. Screen Capture 
![image](https://github.com/Porpathom/my-webapp-model/blob/main/immage/admin.png)


# สรุปความรู้ที่เกี่ยวกับ ความสัมพันธ์ของ Model แบบ Many-to-One
## ความสัมพันธ์แบบ Many-to-One หมายถึงกระบวนการที่โมเดลรับข้อมูลหลายๆ อินพุต (Many inputs) และคืบหน้าไปสู่เอาต์พุตเดียวเท่านั้น (One output) โดยที่เอาต์พุตนี้มักเป็นตัวแทนของคำตอบที่ต้องการทราบในแต่ละกรณี
## โมเดลแบบ Many-to-One มักถูกนำมาใช้ในงานที่เกี่ยวข้องกับการจำแนกและการทำนาย โดยมีตัวอย่างดังนี้:

    - การจำแนกภาพ: ทำนายว่าภาพนั้นอยู่ในหมวดหมู่ใด เช่น จำแนกว่าภาพเป็นรูปของสุนัขหรือแมว
    - การจำแนกข้อความ: ทำนายหมวดหมู่ของประโยคหรือข้อความ เช่น จำแนกว่าคำว่า "เราหิว" เป็นประโยคที่แสดงความต้องการรับประทานอาหาร
    - การทำนายราคา: ทำนายราคาของสินค้าหรือหุ้นตามข้อมูลทางเศรษฐกิจและการเงิน

![image](https://github.com/Porpathom/my-webapp-model/blob/main/immage/many-to-one-function.png)

**____________________________________________________________________________________________________________________**

# 10. psycopg2 และ  Supabase
#### 10.1  การติดตั้ง psycopg2
```py
pip install psycopg2
```
#### 10.2 การเชื่อมต่อฐานข้อมูลไปยัง Supabase ใน settings.py
```py
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' : 'postgres',
        'USER' : 'postgres',
        'PASSWORD' : 'pathom0966788627',
        'HOST' : 'db.bzyjuuuqdvmtppxnydqb.supabase.co',
        'PORT' : '',
    }
}

```
##### มีการใช้คำสั่ง dumpdata ให้ข้อมูลอยู่ในรูปแบบของ JSON และ loaddata เพื่อย้ายไปยังฐานข้อมูลใหม่
```py
python manage.py dumpdatautf8 --output data.json
```
```py
python manage.py loaddatautf8 data.json
```
#### 10.3 การแยกส่วนพัฒนา Projects
##### การแยกส่วนพัฒนาโดยมีการเพิ่มไฟล์ manage_dev.py เพื่อเรียกใช้ settings_dev.py สำหรับการพัฒนา Projects โดยแยกออกจาก Deploy
```py
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings_dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

```
**____________________________________________________________________________________________________________________**
