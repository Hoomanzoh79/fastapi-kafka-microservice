from fastapi import FastAPI


app = FastAPI(
    title="Microservice 2",
    description="This is the consumer fastapi microservice",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
