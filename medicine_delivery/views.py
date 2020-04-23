from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from medicine_delivery.models import Medicine
from medicine_delivery.serializers_medicine_delivery import MedicineDetailsModelSerializer, \
    MedicineDetailsValidationSerializer, LoginValidationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK


class GetMedicineDetails(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        print(request.data)
        print(request.user)
        request_data = MedicineDetailsValidationSerializer(data=request.data)
        if request_data.is_valid():
            print(request_data.validated_data)
            if 'get_list' in request_data.validated_data:
                if request_data.validated_data['get_list'] is True:
                    medicine = Medicine.objects.all()
                    if not medicine.exists():
                        return Response({"status_code": 0, "status_message": "No medicines found"})

            if 'medicine_name' in request_data.validated_data:
                medicine = Medicine.objects.filter(medicine_name__icontains=request_data.data['medicine_name'])
                if not medicine.exists():
                    return Response({"status_code": 0, "status_message": "No medicine found for given name"})

            if 'manufacturer_slug' in request_data.validated_data:
                medicine = Medicine.objects.filter(medicine_manufacturer__medicine_manufacturer_slug=
                                                request_data.validated_data['manufacturer_slug'])
                if not medicine.exists():
                    return Response({"status_code": 0, "status_message": "No medicine manufacturer found"})

            if 'price_range' in request_data.validated_data:
                lower_value, upper_value = request_data.validated_data['price_range'].split("-")
                medicine = Medicine.objects.filter(medicine_price__gt=float(lower_value),
                                                   medicine_price__lte=float(upper_value))
                if not medicine.exists():
                    return Response({"status_code": 0, "status_message": "No medicine found for given price range"})

            medicine_serialized = MedicineDetailsModelSerializer(medicine, many=True)
            return Response({"status_code": 1, "medicine": medicine_serialized.data})
        else:
            return Response({"status_code": -1, "status_message": "Given input is not valid"})


class Login(APIView):
    def post(self, request):
        print(request.data)
        request_data = LoginValidationSerializer(data=request.data)
        if request_data.is_valid():
            if request_data.data['username'] is None or request_data.data['password'] is None:
                return Response({'error': 'Please provide both username and password'},
                                status=HTTP_400_BAD_REQUEST)
            user = authenticate(username=request_data.data['username'], password=request_data.data['password'])

            if user is not None:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                print("User logged in as", user)
                return Response({'token': token.key, "status_code": 1, "status_message": "Successfully logged in"},
                                status=HTTP_200_OK)
            else:
                print("Login failed")
                return Response({"status_code": 0, "status_message": "Invalid username or password"},
                                status=HTTP_404_NOT_FOUND)
        else:
            return Response({"status_message": -1, "status_message": "Please provide valid inputs"},
                            status=HTTP_400_BAD_REQUEST)


class Logout(APIView):

    def get(self, request):
        if request.user is not None:
            print(request.user)
            request.user.auth_token.delete()
            logout(request)
            print(request.user)
            return Response({"status_code": 1, "status_message": "Successfully logged out"}, status=HTTP_200_OK)
