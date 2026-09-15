from fastapi import FastAPI
import logging
import time

from database.database import Base, engine
from routers.students import router as student_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)


@app.middleware("http")
async def log_requests(request, call_next):

    start_time = time.time()

    response = await call_next(request)

    duration = time.time() - start_time

    logger.info(
        "%s %s completed in %.4f seconds",
        request.method,
        request.url.path,
        duration
    )

    return response


app.include_router(student_router)