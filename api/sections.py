import fastapi

router = fastapi.APIRouter()



@router.get('/sections/{id}')
async def read_section():
    return {"section": []}


@router.post('/sections/{id}/content-blocks')
async def read_section_content_blocks():
    return {"section": []}


@router.get('/content-blocks/{id}')
async def read_content_blocks():
    return {"section": []}

