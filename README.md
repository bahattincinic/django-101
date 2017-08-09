![django101av_400x400a](https://cloud.githubusercontent.com/assets/1684999/7142166/27a82dc8-e2df-11e4-8537-d4db8ab90b3c.png)

Django 101 sunumu örnek uygulaması.

[![Build Status](https://travis-ci.org/bahattincinic/django-101.svg?branch=master)](https://travis-ci.org/bahattincinic/django-101)

**Sunum:** http://slides.com/bahattincinic/django-introduction/

**Ekran Görüntüleri:** [Link](screenshots.md)

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
    pip install -r django-101/requirements/dev.txt

**Ayarların özelleştirilmesi**

    cp django-101/slideshare/settings/settings_local.py-dist django-101/slideshare/settings/settings_local.py

**Migrationların yapılması ve Projenin çalıştırılması**

    cd django-101/
    python manage.py migrate
    python manage.py runserver

**Testlerin çalıştırılması**

    python manage.py test

**Admin için Superuser oluşturmak**

    python manage.py createsuperuser

**Örnek Verileri içeri aktarmak için**

    python manage.py loaddata speaker
    python manage.py loaddata presentation
