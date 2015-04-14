![django101av_400x400a](https://cloud.githubusercontent.com/assets/1684999/7142166/27a82dc8-e2df-11e4-8537-d4db8ab90b3c.png)


Istanbul Şehir Üniversitesi Django 101 sunumu örnek uygulaması.

**Sunum:** http://slides.com/bahattincinic/django-introduction/

### Gereksinimler

1. Python 2.7x

### Kurulum

**Pip ve virtualenv kurulumu**

    sudo apt-get install python-pip python-dev build-essential
    sudo apt-get install python-pip
    sudo pip install --upgrade pip
    sudo pip install --upgrade virtualenv

**Virtualenv oluşturmak**

    virtualenv env
    source env/bin/activate

**Proje klonlanması ve gereksinimlerin kurulması**

    git clone git@github.com:bahattincinic/django-101.git
    pip install -r django-101/requirements/local.txt

**Ayarların özelleştirilmesi**

    cp django-101/slideshare/settings/settings_local.py.ex django-101/slideshare/settings/settings_local.py

**Migrationların yapılması ve Projenin çalıştırılması**

    cd django-101/
    python manage.py migrate
    python manage.py runserver

**Testlerin çalıştırılması**

    python manage.py test
