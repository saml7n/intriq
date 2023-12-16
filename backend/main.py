from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Document(BaseModel):
    id: str
    type: str
    data_blob: bytes
    triplet_id: List[str]
    embedding_id: List[str]

class Company(BaseModel):
    id: str
    name: str
    type: str
    sector: str
    valuation: float
    kpi: List[str]
    triplet_id: List[str]
    embedding_id: List[str]

class Triplet(BaseModel):
    id: str
    subject: str
    relation: str
    object: str

class Embedding(BaseModel):
    id: str
    content: str
    vector: List[float]

class Node(BaseModel):
    id: str
    type: str
    position: dict
    label: str
    triplet_id: str

@app.post("/document")
def create_document(data_blob: bytes, file_type: str):
    # Your code here
    pass

@app.get("/document/{id}")
def read_document(id: str):
    # Your code here
    pass

@app.get("/document/{id}/blob")
def read_document_blob(id: str):
    # Your code here
    pass

@app.post("/company")
def create_company(name: str):
    # Your code here
    pass

@app.put("/company")
def update_company(name: Optional[str] = None, type: Optional[str] = None, sector: Optional[str] = None, valuation: Optional[float] = None, kpi: Optional[List[str]] = None):
    # Your code here
    pass

@app.get("/company/{id}")
def read_company(id: str):
    # Your code here
    pass

@app.get("/triplet/{id}")
def read_triplet(id: str):
    # Your code here
    pass

@app.get("/nodes")
def read_nodes():
    # Your code here
    pass

@app.put("/node/{id}")
def update_node(id: str, position: dict):
    # Your code here
    pass
