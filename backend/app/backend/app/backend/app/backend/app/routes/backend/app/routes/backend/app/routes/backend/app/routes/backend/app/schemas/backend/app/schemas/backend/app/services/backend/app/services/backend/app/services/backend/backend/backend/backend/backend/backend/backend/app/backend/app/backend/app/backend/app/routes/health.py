from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "success": True,
        "status": "healthy",
        "service": "SIH26071 Backend"
    }
