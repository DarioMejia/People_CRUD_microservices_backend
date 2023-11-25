import logging
from fastapi import FastAPI, Query

from data.databases.remote.database import get_mongo_database
from config.logging import config_logger
from daos.people_dao import PeopleDAO

config_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="People Search Service",
    description="API to search people",
)
mongo_database = get_mongo_database()
people_dao = PeopleDAO(mongo_database)


@app.get("/")
def list():
    people_list = people_dao.list()
    return people_list


@app.get("/detail")
def detail(doc_id: str = Query(...), doc_type: str = Query(...)):
    people = people_dao.read_by_doc_id_and_type(doc_id, doc_type)
    return people


@app.on_event("startup")
def startup():
    logger.info("read service startup")


@app.on_event("shutdown")
def shutdown_db_client():
    logger.info("read service shutdown")
