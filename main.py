from fastapi import FastAPI

app = FastAPI()           #object of fastapi
list_of_account_id = list()

@app.get('/accounts')
async def accounts():
    return{"Message":"Up and Running"}

@app.get('/accounts/{account_id}')        #@ is for decorator
async def account_id(account_id: int):
    return{"Account_ID": account_id}

@app.post('/accounts/create')
async def create_account_id(account_id: int):
    list_of_account_id.append(account_id)
    return{"Account_ID": list_of_account_id}

@app.put('/accounts/{account_id}')
async def update_account(account_id: int):
    print(account_id)
    list_of_account_id.append(account_id)
    return{"Account_ID": account_id}

@app.delete('/accounts/{account_id}')
async def delete_account(account_id: int):
    list_of_account_id.remove(account_id)
    return{"Account_ID": list_of_account_id}