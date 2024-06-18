from fastapi import FastAPI
 
app = FastAPI()
 
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
# pyinstaller --name=YourAppName --onefile --add-data "weights;weights" --add-data "utils.py;." --add-data "models/models.py;models" --add-data "images;images" app.py
 