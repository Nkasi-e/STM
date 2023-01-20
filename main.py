
from fastapi import FastAPI, Path, Query
from api import users, sections, courses

app = FastAPI(
    title = "Common Books",
    description = "API for reading and writing books",
    version = "0.1.0",
    terms_of_service = "API url service",
    contact = {
        "name":"Nkasi Emmanuel",
        "email":"emmanuelnkasi@gmail.com",
        "url":"http://github.com/nkasi-e"
    },
    license_info = {
        "name":"MIT"
    },
)

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)