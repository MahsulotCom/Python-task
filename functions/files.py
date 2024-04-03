from fastapi import HTTPException
import os
from functions.users import one_user
from models.files import Files
from utils.pagination import pagination


def all_files(search, source_id, source, page, limit, db):
    if search:
        search_formatted = "%{}%".format(search)
        search_filter = Files.source.like(search_formatted)
    else:
        search_filter = Files.id > 0

    if source_id:
        source_id_filter = Files.source_id == source_id
    else:
        source_id_filter = Files.user_id > 0
    if source:
        source_filter = Files.source == source
    else:
        source_filter = Files.id > 0

    files = db.query(Files).filter(search_filter, source_filter,
                                   source_id_filter).order_by(
        Files.id.desc())

    if page and limit:
        return pagination(files, page, limit)
    else:
        return files.all()


def one_files(id, db):
    return db.query(Files).filter(Files.id == id).first()

def one_file_via_source_id(source_id,source, db):
    return db.query(Files).filter(Files.source == source,Files.source_id==source_id).first()

def add_file(source_id, source, file_url, user, db):
    new_files_db = Files(
        image_url=file_url,
        source_id=source_id,
        source=source,
        user_id=user.id,

    )
    db.add(new_files_db)
    db.commit()
    db.refresh(new_files_db)
    return {"data": "Added"}


def update_file( source_id, source, image_url, user, db):
    db.query(Files).filter(Files.source_id == source_id, source=source).update({

        Files.image_url: image_url,
        Files.source_id: source_id,
        Files.source: source,
        Files.user_id: user.id,
    })
    db.commit()
    return one_files(id, db)


def file_delete(source_id,source, db):
    file = one_file_via_source_id(source_id=source_id, source=source, db=db)
    if  file:

        os.unlink(file.image_url)
        db.query(Files).filter(Files.id == file.id).delete()
        db.commit()
        return {"data": "Ma'lumot o'chirildi !"}
