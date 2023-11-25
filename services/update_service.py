import logging
from fastapi import FastAPI, UploadFile, Query

from data.databases.remote.database import get_mongo_database
from config.logging import config_logger
from dtos.people_dto import UpdatePeopleDTO
from daos.people_dao import PeopleDAO

config_logger()
logger = logging.getLogger(__name__)

app = FastAPI(
    title="People Update Service",
    description="API to update people",
)
mongo_database = get_mongo_database()
people_dao = PeopleDAO(mongo_database)


@app.patch("/")
def update(data: UpdatePeopleDTO, doc_id: str = Query(...), doc_type: str = Query(...)):
    people = people_dao.update_by_doc_id_and_type(doc_id, doc_type, data)
    return people


@app.patch("/{doc_id}/image")
def upload_image(doc_id: str, file: UploadFile):
    people = people_dao.update_photo_url_doc_id(doc_id, file)
    return people


@app.on_event("startup")
def startup():
    logger.info("update service startup")


@app.on_event("shutdown")
def shutdown_db_client():
    logger.info("update service shutdown")
