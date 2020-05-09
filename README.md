# django-cbt-app
A Computer Based Test App made to enable one test students' proficiency electronically.

Author : Tobi Balogun

#### Django Cbt App

###### Warning

Make sure you have an Internet connection to load the necessary JS Libraries.

> Basic Usage


This app is minimal and avoids user authentication. If you wish to enable User login before taking Tests, a little trick here and there will do.
The app combines REST API and AJAX technology to make the test asynchronous. Thus it is necessary to add the needed Views and routes when a new Subject is added.
If a subject or course `CSC101` is added in the admin panel, you should and the following in the **views.py** file:

```
class CSC101ViewSet(viewsets.ModelViewSet): 
    queryset= models.Subject.objects.filter(course_name="CSC101")
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

```
And the following to ***urls.py*** file:

```
***
from .views import CSC101ViewSet
***
router.register(r'csc101', CSC101ViewSet)
***
```
Note the cases of the variables.

This alone should get the App working fine.


