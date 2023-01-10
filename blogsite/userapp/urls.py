from django.urls import path
from .views import *
urlpatterns = [
   path('uhome/',UserHome.as_view(),name='uhome'),
   path('profile/',ViewProfile.as_view(),name='prof'),
   path('blogs/',MyBlogs.as_view(),name='blog'),
   path('addbio/',UserProView.as_view(),name='addbio'),
   path('chpsw/',ChangePasswordView.as_view(),name='change-password'),
   path('updatebio/<int:user_id>',UpdateBioView.as_view(),name='updatebio'),
   path('addcmnt/<int:id>',add_comment,name='add-cmnt'),
   path('blog/like/<int:bid>',add_like,name='add-like')
]