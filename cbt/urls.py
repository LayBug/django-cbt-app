from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import PhysicsViewSet, ChemistryViewSet, MathematicsViewSet

router = routers.DefaultRouter()
router.register(r'physics', PhysicsViewSet)
router.register(r'mathematics', MathematicsViewSet)
router.register(r'chemistry', ChemistryViewSet)

urlpatterns = [
        path('apis/', include(router.urls)),
        path('', views.home, name="home"),
        path('test/', views.test_page, name="test_page"),
        path('test/subject/<slug:slug>/', views.load_subject, name="subject_detail"),
        path('test/qa/<uuid:id>', views.validate_quiz, name="qa_detail"),
        path('test/result/<slug:slug>/', views.result_page, name="result"),
        ]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
