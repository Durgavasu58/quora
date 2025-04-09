Installation steps:

1.create a virtual environment (u can use any method)
  --> pip install virtualenv
  --> virtualenv "env"
  --> cd env/scripts/activate
	
2. clone or pull the repistory and in the project directory
   run the command
   
   --> pip install -r requirements.txt
4. --> python manage.py makemigrations && python manage.py migrate
5. create a superuser for admin interface
  --> python manage.py createsuperuser


**Note:**


1. **Users can view questions and answers posted by other users.**
2. 

3. **Authentication is required for users to like answers and to answer questions.**


