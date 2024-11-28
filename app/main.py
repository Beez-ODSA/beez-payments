from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Payments service is running"}

@app.post("/payments/process")
async def process_payment(amount: float, method: str):
    return {"status": "success", "amount": amount, "method": method}