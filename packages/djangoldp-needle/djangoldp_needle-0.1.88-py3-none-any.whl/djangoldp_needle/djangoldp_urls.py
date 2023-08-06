from django.conf import settings
from django.conf.urls import url
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .models import Annotation, Tag, AnnotationTarget, NeedleActivity, AnnotationIntersectionRead, ContactMessage, \
    Booklet, NeedleUserFollow, Avatar
from .views import AnnotationViewset, AnnotationTargetViewset, TagViewset, AnnotationIntersectionReadViewset, \
    ContactMessageView, BookletViewset, BookletInvitationViewset, BookletQuitViewset, NeedleUserFollowViewset, \
    AnnotationIntersectionsViewset, UserViewset, \
    avatars_animals_list, avatars_quality_list, AvatarViewset

urlpatterns = [
    url(r'^booklets/', BookletViewset.urls(model_prefix="booklet", model=Booklet)),
    path('booklets/<pk>/invitation/', BookletInvitationViewset.as_view({'post': 'create'}, model=Booklet)),
    path('booklets/<pk>/quit/', BookletQuitViewset.as_view({'post': 'create'}, model=Booklet)),
    url(r'^annotations/', AnnotationViewset.urls(model_prefix="annoations", model=Annotation)),
    url(r'^annotationtargets/', AnnotationTargetViewset.urls(model_prefix="annotationtarget", model=AnnotationTarget)),
    url(r'^users/(?P<slug>[\w\-\.]+)/annotation_intersection_read/', AnnotationIntersectionReadViewset.urls(model_prefix="annotationintersectionread", model=AnnotationIntersectionRead)),
    url(r'^annotationintersectionreads/', AnnotationIntersectionReadViewset.urls(model_prefix="annotationintersectionread", model=AnnotationIntersectionRead)),
    path('annotationintersections/',
        AnnotationIntersectionsViewset.as_view({'post': 'list'}, model=Annotation)),
    url(r'^users/', UserViewset.urls(model=settings.AUTH_USER_MODEL)),
    url(r'^users/(?P<slug>[\w\-\.]+)/yarn/', AnnotationViewset.urls(model_prefix="yarn", model=Annotation)),
    url(r'^users/(?P<slug>[\w\-\.]+)/tags', TagViewset.urls(model_prefix="tags", model=Tag)),
    url(r'^users/(?P<slug>[\w\-\.]+)/avatar', AvatarViewset.as_view({'get': 'retrieve'},  model=Avatar)),
    url(r'^contact_messages/', ContactMessageView.as_view({'post': 'create'},  model=ContactMessage)),
    url(r'^needleuserfollow/', NeedleUserFollowViewset.urls(model=NeedleUserFollow)),
    url(r'^avatars_animals_list/$', csrf_exempt(avatars_animals_list)),
    url(r'^avatars_quality_list/$', csrf_exempt(avatars_quality_list))
]
