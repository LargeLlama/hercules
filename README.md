# Team Miami Ultras
## Software Development
### Period 8
### Rubin P., Addison H., Hui Min W., and Peter C.

### Launch Instructions

## From Local Machine (As Flask App)
1. Clone repository 

    `$ git clone https://github.com/LargeLlama/Miami-Ultras`

2. Navigate to the `dev` branch in the newly created folder for the repository with the following command 

    `$ git checkout dev`

3. Make sure you have Python 3.7.1 installed, if not, install from [here](https://www.python.org/downloads/)

4. Install virtualenv by running 
  
      `$ pip install virtualenv`

  - Make a venv by running 
  
      `$ python3 -m venv ENV_DIR`
  - Activate it by running 
  
      `$ . /ENV_DIR/bin/activate `
  - Deactivate it by running 
  
      `$ deactivate`  
    
5. Run the following command in the miami/ folder while your virtual environment is active  

    `$ pip install -r requirements.txt`
    
6. Make a data directory in the miami/ folder to store the databases
    `$ mkdir data`

7. Run the following command from the miami/ folder to build the initial databases

    `$ python util/makeData.py`

8. Run the app.py file  

    `$ python app.py`

9. Navigate to [here](http://127.0.0.1:5000/) to see the app in action!

## As Apache App on Server

1. Clone the repository with the following command in the `/var/www/` directory

    `$ git clone https://github.com/LargeLlama/Miami-Ultras miami`

2. Run the following commands on the folder `miami`

    `$ chgrp -R www-data miami`
    
    `$ chmod -R g+w miami`
    
     (This allows for read and write permissions by Apache)
  
3. Move the `.conf` file with the following command

    `$ mv /var/www/miami/miami.conf /etc/apache2/sites-available/` 


4. Enable the site in Apache

    `$ a2ensite appname`

5. Reload/Restart Apache with either of the following commands

    `$ service apache2 reload`
    
      or
    
    `$ service apache2 restart`

6. The app should be live on your droplet/server! Just connect to the server IP or whatever DNS you have setup to see it live.
