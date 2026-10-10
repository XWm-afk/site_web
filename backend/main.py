
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
#разобраться с CORS, написать lock в middleware, и через root опрпобовать чтото, 
#попробовать написать выводы в Middleware самому и проверить на работоспособность
# посмотреть .env, cors по сути работает через env
@app.get("/api/hello")
def hello():
    return {"message": "Hello from Python!"}

git config --global user.email "belgeorgy@gmail.com"
git config --global user.name "XWm"