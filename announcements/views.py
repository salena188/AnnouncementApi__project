from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Announcement
from .serializers import AnnouncementSerializer
from django.shortcuts import render, redirect


# homepage
def announcement_page(request):

    success = False

    if request.method == "POST":

        Announcement.objects.create(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            expiry_date=request.POST.get("expiry_date") or None
        )

        success = True  # ✅ show alert

    return render(request, "announcement.html", {"success": success})


#
@api_view(['GET', 'POST'])
def announcement_api(request):

    if request.method == 'GET':

        announcements = Announcement.objects.all().order_by('-created_at')

        serializer = AnnouncementSerializer(
            announcements,
            many=True
        )

        return Response(serializer.data)

    if request.method == 'POST':

        serializer = AnnouncementSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)




