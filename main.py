from fastapi import FastAPI

from api.v1 import api_router

app = FastAPI()
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', debug=True, reload=True)
