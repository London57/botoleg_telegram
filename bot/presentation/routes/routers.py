from .map import router as start_router
from .work.work import router as work_router
from .work.business import router as business_router

routers = [start_router, work_router, business_router]