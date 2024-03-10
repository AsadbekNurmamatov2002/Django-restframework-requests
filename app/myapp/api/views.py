from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializers
from myapp.models import Product

@api_view(["GET"])
def ProductApi(request):
    product=Product.objects.all()
    serializer=ProductSerializers(product, many=True)
    return Response(serializer.data)