from django.urls import path
from .views import TestimonialCreateListView, TestimonialUpdateDeleteView

urlpatterns = [
    path('testimonials', TestimonialCreateListView.as_view(), name='testimonial-list-create'),
    path('testimonials/<int:pk>', TestimonialUpdateDeleteView.as_view(), name='testimonial-update-delete'),
]
