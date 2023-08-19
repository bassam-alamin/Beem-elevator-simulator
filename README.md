### Version: 1.0.0

# Beem Elevator backend
Beem Elevator backend

## How To Run:  
1. Download all requirements from the requirements.txt file  
    ``` pip install -r requirements.txt```

2. create .env file and copy contents of .env.example. 

3. Update .env file with the correct values. Some variables are required and should be added
if they are not already provided in the example file.

4. Run migrations  
    ```alembic upgrade head```

5. Run the server locally  
    ```uvicorn apps.main:app --reload```

6. Alternatively, you can also run the following command to run the server locally  
    ```python main.py```


To view Api endpoints and test them:  
On Your browser enter [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 

To view API documentation in a nicely presented way:  
On Your browser enter [127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)