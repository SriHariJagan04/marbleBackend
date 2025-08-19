from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .serializers import EnquirySerializer
from rest_framework.permissions import AllowAny


class EnquiryView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            # Get type and name with defaults
            request_type = data.get("type", "enquiry").lower()
            name = data.get("name", "Anonymous")

            # Choose template & subject
            if request_type == "instantquote":
                template_name = "emails/instant_quote.html"
                subject = f"Instant Quote Request from {name}"
            elif request_type == "enquiry":
                template_name = "emails/enquiry.html"
                subject = f"New Enquiry from {name}"
            else:
                # Default fallback
                template_name = "emails/enquiry.html"
                subject = f"General Request from {name}"

            # Render HTML email
            html_content = render_to_string(template_name, data)

            # Send email
            msg = EmailMultiAlternatives(
                subject=subject,
                body="Please see the details below.",
                from_email=data.get('email', 'no-reply@example.com'),  # default if missing
                to=["jkgranimarmo@hotmail.com", "jkgranimarmoksg@gmail.com", "sriharijagan07@gmail.com"],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return Response(
                {"message": f"{request_type.capitalize()} sent successfully"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class NewsletterSubscriptionView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare subject and HTML template
        subject = "Welcome to JK Grani Marmo – Stay Inspired with Marble Elegance"
        html_content = render_to_string("emails/subscription.html", {
            "email": email
        })

        # Send email
        msg = EmailMultiAlternatives(
            subject=subject,
            body="Thank you for subscribing to JK Grani Marmo's newsletter.",
            from_email="no-reply@jkgranimarmo.in",  # Use your domain email
            to=[email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

        return Response({"message": "Subscription successful. Welcome email sent!"}, status=status.HTTP_200_OK)
