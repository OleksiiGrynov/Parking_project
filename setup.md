# Instructions

1. Instal virtual env
```
python3.9 -m venv env
```

2. Activate virtual env

```
source env/bin/acivate
```

3. Install deps

```
pip3 install -r requirements.txt
```

4. Migrate database

```
python3 manage.py migrate
```

5. Load test data

```
python3 manage.py loaddata data.json
```

6. Create super user

```
python3 manage.py createsuperuser
```

7. Run server

```
python3 manage.py runserver
```


Links

[swagger](http://localhost:8000/swagger/)
