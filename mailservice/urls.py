from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import EnquiryView ,NewsletterSubscriptionView

urlpatterns = [
    path("enquiry", EnquiryView.as_view(), name="enquiry"),
    path("newsletter", NewsletterSubscriptionView.as_view(), name="newsletter"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
