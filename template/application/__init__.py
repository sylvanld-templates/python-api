"""
{{app_description}}
"""

from fastapi import FastAPI
from .endpoints.defaults import router as default_endpoints


server = FastAPI()
server.include_router(default_endpoints)
