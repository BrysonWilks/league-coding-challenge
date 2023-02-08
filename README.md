To run this program please install Python. Link to install Python

https://www.python.org/downloads/

---------------------------------

Once you have downloaded Python please make sure to clone this GitHub repo onto your local machine or download it is as a .zip file

```
git clone https://github.com/BrysonWilks/league-coding-challenge.git
```

---------------------------------

After the repo has been either cloned or downloaded via .zip file onto your local machine, please activate the virtual environment. This will install all of the packages necessary to run the web server 

To activate the virtual environment change your directory to the directory of the virtual environment with the command below

```
cd virtual-env/bin
```
Once that is done, please proceed to activate the virtual environment using the command below

```
source Activate 
```

If this is done correctly you should see the name of the virtual environment next to the directory name like so:

```
(virtual-env) ➜  bin
```

Once your virtual environment has been activate please navigate to the 'mainsite' directory by using this command

```
cd ../../mainsite/
```

Once you are in the mainsite directory, run this command to start the Django web server 

```
python manage.py runserver
```

If your virtual environment is set up correctly you should see this output upon starting your server

```
System check identified no issues (0 silenced).
[month] [day], [year] - [UTC time]
Django version 4.1.6, using settings 'mainsite.settings'
Starting development server at http://127.0.0.1:8080/
Quit the server with CONTROL-C.
```

---------------------------------

Open up a new tab in your terminal / command prompt.

On MacOs this is done by pressing 'command + T'

On Linux this is done by pressing 'Ctrl + Shift + T'

On Windows this is done by pressing 'Ctrl + Win + T'
 
Enter in curl HTTP request like so

```
curl -F 'file=matrix.csv' "localhost:8080/echo"
```

Happy Testing!

---------------------------------

# Key Areas

Keys areas to explore in codebase

utils.py - contains logic to parse csv into 2D array
views.py - contains logic for the different endpoints ('echo', 'sum', 'flatten', 'multiply', 'invert')
mainsite/app/urls.py - contains the routing for the different endpoints

---------------------------------
# FAQ

Q - I'm having trouble creating my virtual environment, is there anyway I can recreate it?

A - Yes! First make sure you have the 'virtualenv' package installed in Python. This can be done by typing 

```
pip install virtualenv
```

Once this is done type the following command in the 'mainsite' directory 

```
virtualenv venv && venv/bin/pip install -r requirements.txt
```

Q - How do I get out of this virtual environment?

A - To leave the virtual environment type 

```
deactivate
```

If done correctly you should not see the name of the virtual environment in parentheses anymore


