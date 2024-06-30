from fastapi import FastAPI
from api.dcgan_router import router as dcgan_router
from api.wgan_gp_router import router as wgan_gp_router


app = FastAPI()

# Include routers for DCGAN and WGAN-GP here
app.include_router(dcgan_router, prefix="/api")
app.include_router(wgan_gp_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

