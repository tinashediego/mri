
from companyapi.viewsets import CompanyViewset
from mineralapi.viewsets import MineralViewset
from reportapi.viewsets import ReportViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('companies', CompanyViewset)
router.register('minerals', MineralViewset)
router.register('report', ReportViewset)