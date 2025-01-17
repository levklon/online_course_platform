from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .models import Course, Video
from .serializers import CourseSerializer, VideoSerializer
import stripe
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from .forms import MyForm


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.create(user=user).key
        })

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['POST'])
def create_checkout_session(request):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Course',
                    },
                    'unit_amount': 1000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:3000/success',
            cancel_url='http://localhost:3000/cancel',
        )
        return JsonResponse({'id': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)})



def my_view(request):
    user_input = ''
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['name']  
    else:
        form = MyForm()

    return render(request, 'my_template.html', {'form': form, 'user_input': user_input})