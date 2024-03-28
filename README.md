# Medical clinic
Simple application for managing patients in a medical clinic.
You can open the app using command:
1) Windows:
py manage.py runserver
2) Linux/ macOS:
python manage.py runserver

By default, the runserver command starts the development server on the internal IP at port 8000.
If you want to change the server’s port, pass it as a command-line argument: 
  python manage.py runserver 8080

The last step is to create the tables in the database. To do that, run the following command:
1) Windows:
py manage.py migrate
2) Linux/macOS:
python manage.py migrate
