
## Features

- SignIn, LogIn, LogOut
- Email verification after registration/signup
- Reset password
- Cool theme integrated for admin-panel
## Tech Stack

**Client Side:** HTML, SCSS, TailwindCSS

**Server Side:** Django


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG = TRUE`

`SECRET_KEY = 'django-insecure-)0!=5k5jmoawok1arzz(^#!o=8ck8=($^-2m#^1f_p(*!jwvl%'`

### For sending emails
`EMAIL_HOST_USER = 'email address from which email will be send'`

`EMAIL_HOST_PASSWORD = 'its app password' `

Note : You have to create app password for the email you are using in `EMAIL_HOST_USER` and put it in `EMAIL_HOST_PASSWORD`
## Installation

Create a folder and open terminal and install this project by
command 
```bash
git clone https://github.com/Mr-Atanu-Roy/Authentication-System

```
or simply download this project from https://github.com/Mr-Atanu-Roy/Authentication-System

In project directory Create a virtual environment(say env)

```bash
  virtualenv env

```
Activate the virtual environment

For windows:
```bash
  env\Script\activate

```
Install dependencies
```bash
  pip install -r requirements.txt

```
To migrate the database run migrations commands
```bash
  py manage.py magemigrations
  py manage.py migrate

```

Create a super user
```bash
  py manage.py createsuperuser

```

To run the project in your localserver
```bash
  py manage.py runserver

```
Then go to http://127.0.0.1:8000 in your browser to see the project

## Author

- [@Mr-Atanu-Roy](https://www.github.com/Mr-Atanu-Roy)

