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

