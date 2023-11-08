# book_rec


### How to install
1. Install Python
2. Install VS Code
3. Install Git
4. Click CTRL+SHIFT+P in VS Code and type in "clone". Select clone repository and click enter "https://gitgub.com/uzmahamid01/book_rec". Then store it where you would like.
5. Setup git by running:
    \
    git config --global user.name "myGithubUsername"
    \
    git config --global user.email "myGithubEmail"
6. Open the terminal and run "python3 -m pip install Django" to install Django
7. Read and follow the instructions in the Database Changes section below
8. Run "python3 manage.py runserver" to start the server
9. The project should be up and running. In the terminal, click the provided link and look at the website!

### Database Changes
Whenver there is a database change or the project is being setup for the first time, you must generate the database
1. Run "python3 manage.py makemigrations". This will check for database changes
2. Run "python3 manage.py migrate". This will apply the changes to the database

If this is a fresh setup, you will want to also create an admin user
1. Run "python manage.py createsuperuser" and follow its instructions. You do not need to enter a real email.
2. You can use this login and password to login to the website at the /admin url
