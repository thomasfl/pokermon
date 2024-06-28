# Pokermon game backend
Invoke URL: https://djfcgckvy3.execute-api.eu-west-1.amazonaws.com

---
### Quick start
To install dependencies and run locally on Windows:

```
$ py -m pip install virtualenv
$ py -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ pip install uvicorn
$ uvicorn main:app --reload
```

To install dependencies and run locally on Linux or Mac:
```
$ python -m pip install --upgrade pip
$ python -m pip install virtualenv
$ python -m venv venv
$ source ./venv/bin/activate
$ brew install postgresql
$ pip install -r requirements.txt
$ uvicorn main:app --reload
```

To add authorization header, click the green "Authorize" button. Log into Prisma and copy the authorization header for one of the requests. Paste the token

Ctrl + C to stop uvicorn. Type "deactivate" to stop venv.

---
### Testing

Deactivate venv first. Then in Windows and the cmd shell type:
```
$ py -m pytest -s
```

In PowerShell on Windows:
```
> py -m pytest -s
```

In MacOS and Linux: 
```
$ python -m pytest -s
```
