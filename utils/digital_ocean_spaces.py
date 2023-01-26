import os, shutil, json
from datetime import date, datetime
from fastapi import HTTPException

# BOTO imports
import boto3
from boto3 import session
from botocore.client import Config
from boto3.s3.transfer import S3Transfer

# SETTINGS
from settings.config import settings

DOS_ACCESS_ID = settings.DOS_ACCESS_ID
DOS_SECRET_KEY = settings.DOS_SECRET_KEY

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg'}
UPLOAD_FOLDER = os.getcwd() + '/media/uploads'

# initiate session
session = session.Session()
client = session.client('s3',
                        region_name=settings.DOS_REGION_NAME, 
                        endpoint_url=settings.DOS_ENDPOINT_URL,
                        
                        aws_access_key_id=DOS_ACCESS_ID,
                        aws_secret_access_key=DOS_SECRET_KEY)
transfer = S3Transfer(client)



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

async def file_upload(fileObj):
    file = fileObj

    if file and allowed_file(filename=file.filename):
        try:
            file_location = os.path.join(UPLOAD_FOLDER, file.filename)
            print("x", file_location)

            with open(file_location, "wb+") as file_object:
                shutil.copyfileobj(file.file, file_object)
                

            return file_location
        except Exception as e:
            print("shdgv", e)
            raise HTTPException(status_code=500, detail=json.dumps(e))
    else:
        return None

# upload to DOS
async def upload_to_spaces(file):
    try:

        file_to_upload = await file_upload(fileObj=file)

        transfer.upload_file(file_to_upload, settings.DOS_NAME_OF_BUCKET, 
                            settings.DOS_CURRENT_UPLOAD_FOLDER + "/" + file.filename, 
                            extra_args={'ContentType': 'application/pdf', 'ACL': 'public-read'})

        # this makes the file you are specifically uploaded public by default
        response = client.put_object_acl(ACL='public-read', Bucket=settings.DOS_NAME_OF_BUCKET,
                                        Key="%s/%s" % (settings.DOS_CURRENT_UPLOAD_FOLDER, file.filename))
        return  file_to_upload

    except Exception as e:
        raise HTTPException(status_code=500, detail=json.dumps(e))

# delete files uploaded
settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))

media_uploads = os.path.join(PROJECT_ROOT, "media/uploads")

def delete_upload(filename):
    os.chdir(media_uploads)

    for file in os.listdir("."):
        if os.path.isfile(file) and file.startswith(filename):
            try:
                os.remove(file)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error while deleting file {e}")