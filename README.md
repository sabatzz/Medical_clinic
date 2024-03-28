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

 Make sure that in your browser you’re going to http://localhost:8000/patients/ and not http://localhost:8000/.

// if you can't start the server and it shows an error like this: ModuleNotFoundError: No module named 'django' it means that you have to install django using command:
pip install django
