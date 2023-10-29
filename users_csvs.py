import csv 
from fastapi  import FastAPI
from pydantic import BaseModel


app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    article: str

#CRUD operation
#Create - POST
@app.post("/user/")
async def create_user(user: User):
    with open("new.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.id, user.name, user.email, user.article,])
    return {"message": "User sucessfully created", "data": user}

#Read - GET
@app.get("/user/{id}")
async def get_user(id: int):
    with open ("new.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) >= 3 and int(row[0]) == id:
                return User(id=int(row[0]), name=row[1], email=row[2], article=row[3])
    return {"message":"User not found"}
                 
#Update - PUT
@app.put("/user/{id}")
async def update_user(id: int, user: User):
     rows = []
     with open ('new.csv', 'r') as f:
          reader = csv.reader(f)
          header = next(reader)
          for row in reader:
              rows.append(row)
     with open ('new.csv', 'w', newline = '') as f:
         writer = csv.writer(f)
         writer.writerow(header)
         for index, row in enumerate(rows):
             if int(row[0]) == id:
                  rows[index] = [user.id, user.name, user.email, user.article]
                  writer.writerow(rows[index])
             else:
                 writer.writerow(rows[index])
     return {"message": "Person sucessfully updated", "data": user}  

#DELETE - delete
@app.delete("/user/{id}")      
async def update_user(id: int, user: User):
     rows = []
     with open ('new.csv', 'r') as f:
          reader = csv.reader(f)
          header = next(reader)
          for row in reader:
              rows.append(row)
     with open ('new.csv', 'w', newline = '') as f:
         writer = csv.writer(f)
         writer.writerow(header)
         for index, row in enumerate(rows):
             if int(row[0]) == id:
                  continue
             else:
                 writer.writerow(rows[index])
     return {"message": "User sucessfully deleted"} 