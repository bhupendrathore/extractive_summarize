from fastapi import APIRouter
from app.services.summarize import SummExtract
from app.services.cluster import ClusterData
from app.routers.datamodels import InputData
import os

from sentence_transformers import SentenceTransformer

MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
try:
    thresh = os.environ["CLUSTER_THRESH"]
except :
    print("taking default")
    thresh = 0.4
CLUSTER_OBJ = ClusterData(MODEL,thresh)
SUMM_OBJ = SummExtract(CLUSTER_OBJ,MODEL)

router = APIRouter(
    tags=["Inference"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def health_check():
    """Check the health of services
    author: andy
    Returns:
        [json]: json object with a status 
    """
    return {"message": "Status = Healthy"}

@router.post("/summarize")
async def summarize(request:InputData):
    request_id = request.request_id
    text = request.text

    try:
        sum_text = SUMM_OBJ.summerize(text)
        print(f"summarization success for request_id = {request_id}")
        return {"status":True,"summarized_text":sum_text}
    except Exception as err:
        print(f"summarization failed with err = {err} for request_id = {request_id}")
        return {"status":False,"summarized_text":""}



