# Flask IT-center application (АЙ-ТІ!)

This is my first serious web project. Created by me for the educational purposes of my university.
In the application, you can view and select the IT services you are interested in. Create an account and login.

### Technology stack
- Python/Flask/Flask-SQLALchemy
- PostgreSQL
- Redis
- CouchDB
- Docker
- HTML/CSS 
#
The project contains 3 different databases, each of which performs its own task.
Running the flask application and related components is done using docker. The connection and activation of
containers is written in the docker-compose.yaml file. It runs the application with the command:
* docker-compose up server.
# Website
On the main page of the site, we can immediately see the opportunities that we can use. Order a service, register or login to an account.
The button to order services and logout of the account will redirect us to new pages, only if the user is in the account.
Otherwise, you will be redirected to the login page.
![image](https://user-images.githubusercontent.com/119871133/219901294-faafbdb6-2d39-44c6-9cf4-7b5a322a1fcd.png)

## Login and Registration (PostgreSQL database)
The Flask Login library helps us with this. In order to register, we need to enter a unique login, as well as a password and repeat it. 
The password is hashed using the function generate_password_hash(). The data puts into the SQL  database "itservice" in the table "user".

![image](https://user-images.githubusercontent.com/119871133/219904812-be8617d3-7fca-469c-8281-a6a5d678251c.png)

The program will issue a flash warning if the fields are not filled, or the passwords do not match.

When logging, the data entered by the user is checked against the data that the database contains. If successful, the user logs into the account.
In case of failure, it displays flash warnings about incorrect data.

![image](https://user-images.githubusercontent.com/119871133/219904449-71583777-f4a0-46af-8b98-d3960990e69a.png)

Logout from the account occurs when you click on the logout button, which works only with an active user.


Flask Migrate was used to create models inside the database.

## Time on site (Redis database)

We can calculate the time a user spends on a site using the redis database. The time  is record when the user logs into the account
and when the user logs out.

![image](https://user-images.githubusercontent.com/119871133/219904716-4202de58-0d0c-4a54-8561-1742e76a7c84.png)

# Website service data (CouchDB database)
The data on the "Services" page is taken from the CouchDB document database. We take each entry from the database as a separate object,
pass it to the html template and display it on the site. The object contains the following data:
* Name
* Description
* Phone number
* Price

![image](https://user-images.githubusercontent.com/119871133/219905068-5b264041-bc9a-45e0-af2f-156a7ef50ff9.png)

Each object looks like this.

![image](https://user-images.githubusercontent.com/119871133/219905111-4b70e1d3-f7bf-46b8-8293-6b4819394e05.png)

The main objective of this project was to use docker to connect all the components of the program in practice.
Creation of registration and login with automatic addition of data to the SQL database. As well as sharing multiple databases in a single project.
