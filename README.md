<img align="right" src="https://notion-emojis.s3-us-west-2.amazonaws.com/v0/svg-twitter/1f40d.svg" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" width="200" height="400" />

## **Simple app for restaurant booking**

Made by **Denis Krepak**

## **Project Descrtiption**

Simple app for restaurant booking that accepts and responds to HTTP requests. 

What can you do?

- See all the tables 
- Use filters for getting information about tables via flags: capacity, is reserved 
- See information about current table
- See information about current client
- See all reservations
- Use filters for getting information about reservations via flags: exact day, exact client, exact table
- See information about current reservation
- See all the reservations(history)
- Change flags via classic Django Admin Panel
- Create POST requests to add new reservations 

Wrote on **Python** using **Django**, **Django Rest Framework**. **PostgreSQL** is used as a **DBMS**

## **Deployment on a local machine via Docker**
1. Clone the repository and go to the folder with app:
```
git clone https://github.com/dvkrepak/simple_app_for_restaurant_reservation.git && cd simple_app_for_restaurant_reservation/
```
2. Up containers after building:
```
docker-compose up -d --build
```
3. Make migrations:
```
docker-compose exec web python manage.py makemigrations --noinput \
    && docker-compose exec web python manage.py migrate --noinput
```
4. Fill the DB(optional):
```
docker-compose exec web python manage.py loaddata reservation/fixtures/table.json
docker-compose exec web python manage.py loaddata reservation/fixtures/client.json
docker-compose exec web python manage.py loaddata reservation/fixtures/reservation.json
```


Project will be available at **http://127.0.0.1:8000/**



## **Views:**
#### **localhost/admin/** - classic Django admin panel 
#### **localhost/tables/** - list of tables (Can be filtred via capacity,  is_reserved(0 or 1)) (GET)
#### **localhost/tables/<table_id>/** - detail table view (GET)
#### **localhost/clients/<client_id>/** - detail client view (GET)
#### **localhost/reservations_history/** - list of all reservations (GET)
#### **localhost/reservations/** - list of active reservations (GET)
### **localhost/reservations/<reservation_id>** detail reservation view (GET)
### **localhost/new_reservation/** - create new reservation (POST)
