# Team Miami Ultras
## Software Development
### Period 8
### Rubin P., Addison H., Hui Min W., and Peter C.

### Launch Instructions
1. Clone repository 

`$ git clone https://github.com/LargeLlama/Miami-Ultras`

2. Make sure you have Python 3.7.1 installed, if not, install from [here](https://www.python.org/downloads/)

3. Install virtualenv by running 
  
      `$ pip install virtualenv`

  - Make a venv by running 
  
      `$ python3 -m venv ENV_DIR`
  - Activate it by running 
  
      `$ . /ENV_DIR/bin/activate `
  - Deactivate it by running 
  
      `$ deactivate`  
    
4. Run the following command in the miami/ folder while your virtual environment is active  

  - `$ pip install -r requirements.txt`

5. Run the following command from the miami/ folder to build the initial databases
  - `$ python util/makeData.py`

6. Run the app.py file  

  - `$ python app.py`

7. Navigate to [here](http://127.0.0.1:5000/) to see the app in action!
