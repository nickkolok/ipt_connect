<a href="https://github.com/vbonvin/ipt_connect"><img style="position: absolute; top: 0; left: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_left_green_007200.png" alt="Fork me on GitHub"></a>

# ipt_connect

A python/django web-based interface to track the grades, compute the rankings and display a lot of interesting statistics on the <a href="https://iptnet.info">International Physicists' Tournament</a>. 

### Status
* Code: working, v2.0, minor display bugs to fix
* Documentation: work in progress
* CI: None

 <a href='http://ipt-connect.readthedocs.io/en/latest/?badge=latest'>
    <img src='https://readthedocs.org/projects/ipt-connect/badge/?version=latest' alt='Documentation Status' /></a>

### Starting:
* Install the requirements `pip install -r requirements.txt`
* Run `python manage.py runserver`
* Open <a href="http://127.0.0.1:8000/IPTdev/">http://127.0.0.1:8000/IPTdev/</a>


### Requirements:
- Python 2.x
- Django > 1.9
- Pillow


## F.A.Q:

### How to add superuser and sign in to site?
* Run `python manage.py createsuperuser`
* Set username, email address and password.
* Run `python manage.py runserver`
* Open <a href="http://127.0.0.1:8000/admin/">http://127.0.0.1:8000/admin/</a> and sign in.

### How to switch between languages?
Сhange `LANGUAGE_CODE` values in [this](../master/ipt_connect/ipt_connect/settings.py) file to switch the language.  
Available values:
* en-us
* ru

### I added new text to the template. How сan I update language files?
Run `python manage.py makemessages -a -e=html -i=grappelli/*`

### How to compile language files?
Language files compiled automatically when the server starts.

### How to add a new language?
* Run `python manage.py makemessages -l de -e=html -i=grappelli/*` where `de` is the [locale name](https://docs.djangoproject.com/en/2.0/topics/i18n/#term-locale-name) for the message file you want to create.
* Translate all text in the file, which will be create.
* Run application.

### How to download certificates?
* Sign in as superuser.
* <a href="http://127.0.0.1:8000/IPTdev/download_certs/">http://127.0.0.1:8000/IPTdev/download_certs/</a> - download all certificates.
* <a href="http://127.0.0.1:8000/IPTdev/download_certs?best=1/">http://127.0.0.1:8000/IPTdev/download_certs?best=1/</a> - download certificates for the best participants.
* <a href="http://127.0.0.1:8000/IPTdev/download_certs?team=1/">http://127.0.0.1:8000/IPTdev/download_certs?team=1/</a> - download certificates for the best teams.

### How to add participants from .csv file?
* Sign in as superuser.
* Go to <a href="http://127.0.0.1:8000/IPTdev/upload_csv/">http://127.0.0.1:8000/IPTdev/upload_csv/</a> and upload your .csv file.

.csv file must be in the following format:
```
"Gender","Class","Educational institution","Surname","Name","Patronymic"
"м",9,"МБОУ Лицей №15","Иванов","Иван","Иванович"
"ж",10,"МБОУ СОШ № 80","Петрова","Мария","Петровна"
...
```

### How to start a new tournament?
* Run `python manage.py flush`
* Sign in as superuser and add new participants, jury members and etc.

