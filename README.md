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

## How To Test APi's:  
1. Open documentation above to see these 2 endpoints
2. Depending on the number of elevators configured on the environment enter the elevator_id and the name of person requesting the elevator for instance.
    ![image](https://github.com/bassam-alamin/Beem-elevator-simulator/assets/31857273/782ee90b-f682-436e-a667-dec7440cc86e)
   
3. You can as well monitor the lifts positions by constantly calling the endpoint below.
    ![image](https://github.com/bassam-alamin/Beem-elevator-simulator/assets/31857273/9b83dc64-aafe-43c5-bb2c-7e630c2cf098)
    
4. Also to get real time position/ logs of the elevator you can look at your terminal i.e
   ![image](https://github.com/bassam-alamin/Beem-elevator-simulator/assets/31857273/94b45225-c184-4ffd-93f9-4951040450f4)

5. Also to test the persistence of Logs on database u can install Sqlitebrowser on your machine and view the details.
   Also note that SQLite3 for easy testing.Since no further configurations are required.
   
   Elevator Logs:
   
   ![image](https://github.com/bassam-alamin/Beem-elevator-simulator/assets/31857273/06b18cdf-345b-4fc0-bd25-0e011086379e)
   
   Query Logger Table
   
   ![Screenshot from 2023-08-21 10-28-49](https://github.com/bassam-alamin/Beem-elevator-simulator/assets/31857273/cd852ea0-27cd-4d31-bef7-48cba99ed30e)


