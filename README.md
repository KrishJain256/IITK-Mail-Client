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
This will start to setup MySQL for the mail client
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