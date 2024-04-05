# IITK Mail Client
A Mail Client that resembles the IITK Mail Client.
It is built with Python, MySQL and the Django framework.
You can create user accounts, login into your accounts, check mails and even compose and send mails.

## How to Run
### Step 1 : 
Clone the github repository
### Step 2 :
Open terminal in the cloned repo directory

You might choose to run the entire project in a virtual environment too
### Step 3 :
Using pip, install all the requirements
```
pip install --upgrade -r requirements.txt
```
### Step 4 :
Install [MySQL](https://dev.mysql.com/downloads/installer/) for your device

### Step 5 :
Open a terminal window in the ui/mysql_helper/ directory and enter the following command.
This will start to setup MySQL for the mail client.

Also, you would need to change some parameters on basis of your configuration of MySQL i.e. MySQL password.
In the mailclient/ directory, you will find a settings.py file. Onen the file and search for 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mailclient',
        'USER': 'root',
        'PASSWORD': '{ENTER_YOUR_PASSWORD}',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
```
Here, replace the <code>{ENTER_YOUR_PASSWORD}</code> with your actual MySQL password.
Also, in the ui/mysql_helper/ directory, you need to open dbconnect.py
```
con = mysql.connector.connect(host="localhost", user="root", passwd="{YOUR_PASSWORD}")
```
Here, you will need to replace the same password. Also in the same directory, open user_functions.py
```
con = mysql.connector.connect(host="localhost", user="root", passwd="{YOUR_PASSWORD}", database="mailclient")
```
In this file, you will find this line 3 times, you need to replace your password here too.

Now, we are ready to proceed further.
```
python dbconnect.py estabilish_connection
```
Now, in the old terminal window pass the following commands to finish setting up the database.
```
python manage.py runserver
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
When you run the runserver command you will get a link that looks like 
http://127.0.0.1:8000/ but that link isn't complete.So, at the end of the link add a <code>ui/login/</code>
.That will take you to the login from where you can begin to create you account by clicking on the Create account option
and then explore the mail client.
