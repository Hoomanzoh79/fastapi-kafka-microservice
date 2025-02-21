from fastapi import FastAPI


app = FastAPI(
    title="Microservice 1",
    description="This is the publisher fastapi microservice",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
