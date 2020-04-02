"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls            import path, include
from rest_framework.routers import DefaultRouter
from newest_course          import views

router = DefaultRouter()

## views.CourseViewSet의 uri이름을 명시
## 나는 '공란'으로 명시함
router.register('', views.CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

