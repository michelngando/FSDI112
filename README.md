# Important notes for Django Projects

1. Open Terminal and create a folder to store the project (e.g. Code/SDGKU/blog)
2. Move to the respective folder (make sure you're on the right location)
3. craete a virtual env (python3 -m venv venv)
4. Activate the venv (source venv/bin/activate)
4. Install django (pip install django)
5. Save dependencies into requirements.txt file (pip freeze > requirements.txt)
6. Create the project (django-admin startproject config .)
7. Create the respective structure
    - Create the static, templates, img, css, js folders --> mkdir command
    - Create the .gitignore, README.md (optional) --> touch command
8. To create an app in django --> python3 manage.py startapp <name of your app>

# Additional notes  
- All of the subcommands for django are going to be called followed by python3 manage.py (e.g. python3 manage.py runserver, python3 manage.py migrate...)
- If we want to check the full list, we can run python3 manage.py
