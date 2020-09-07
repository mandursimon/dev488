# building_access
## how to run it

You can run building_access by going to it's directory and then typing building_access\Scripts\Activate.bat, if you're on Linux you need to type:
```bash
sudo building_access\Scripts\Activate
```

This will activate scripts in which are stored pip files(virtual environment) after that just simply do:
```bash
python manage.py runserver
```

This will run the project on localhost http://localhost:8000/, use /home/ or /admin/, to create admin, you need to type.

Python manage.py create superuser, then it will tell you what to do, on /admin/ page you simply need to put in there the name and password you created, to sync database,
use python manage.py migrate --run-syncdb, python manage.py makemigrations, python manage.py migrate

## models

Models are stored on /admin/ page, you can remove them, edit them, add them, and much more, if you go to models.py you'll see few models.
Everytime you create a model, you need to register it in admin.py, accordingly to previous things.
You can find more info on this link: https://docs.djangoproject.com/en/3.1/topics/db/

## settings

If you're installing new stuff such as pynumbers and others you need to put them to settings.py, among installed apps.

## urls

If you wanna create your own url, such as http://localhost:8000/admin/,/home/,/about/, you can create it by going to urls.py, and doing it accordingly to previous urls.
