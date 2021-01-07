"""
{{app_description}}
"""

from fastapi import FastAPI
from .endpoints.defaults import router as documentation_endpoints


server = FastAPI()
server.include_router(documentation_endpoints)
