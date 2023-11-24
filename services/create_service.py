import logging
from fastapi import FastAPI
from starlette import status

from data.databases.remote.database import get_mongo_database
from config.logging import config_logger
from dtos.people_dto import CreatePeopleDTO
from daos.people_dao import PeopleDAO

config_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="People Create Service",
    description="API to create people",
)
mongo_database = get_mongo_database()
people_dao = PeopleDAO(mongo_database)


@app.post("/", status_code=status.HTTP_201_CREATED)
def create(people: CreatePeopleDTO):
    created_people = people_dao.create(people)
    return created_people


@app.on_event("startup")
def startup():
    logger.info("create service startup")


@app.on_event("shutdown")
def shutdown_db_client():
    logger.info("create service shutdown")
