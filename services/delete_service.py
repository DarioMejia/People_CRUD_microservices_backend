import logging
from fastapi import FastAPI, Query
from starlette import status

from data.databases.remote.database import get_mongo_database
from config.logging import config_logger
from daos.people_dao import PeopleDAO

config_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="People Delete Service",
    description="API to delete people",
)
mongo_database = get_mongo_database()
people_dao = PeopleDAO(mongo_database)


@app.delete("/", status_code=status.HTTP_200_OK)
def delete(doc_id: str = Query(...), doc_type: str = Query(...)):
    people = people_dao.delete_by_doc_id_and_type(doc_id, doc_type)
    return people


@app.on_event("startup")
def startup():
    logger.info("delete service startup")


@app.on_event("shutdown")
def shutdown_db_client():
    logger.info("delete service shutdown")
