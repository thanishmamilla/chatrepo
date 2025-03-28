from fastapi import FastAPI
from routes.chat_routes import router as chat_router
from routes.user_routes import router as user_router
from routes.summary_routes import router as summary_router

app = FastAPI(title="Chat API", description="FastAPI Chat Storage & Summarization")

# Include routes
app.include_router(chat_router, prefix="/chats", tags=["Chats"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(summary_router, prefix="/summarization", tags=["Summarization"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
