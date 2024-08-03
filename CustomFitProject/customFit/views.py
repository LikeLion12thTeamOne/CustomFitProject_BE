from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count  # Count를 명시적으로 가져옴
from .models import Product, Cart, CartItem, RecommendedProduct
from .serializers import ProductSerializer, CartItemSerializer, RecommendedProductRatingSerializer

# Product 읽기 전용 API view
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # 전체 Product list 반환
    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.only('product_id', 'product_name', 'manufacturer', 'Capacity', 'category')
        return super().list(request, *args, **kwargs)
    
    # 특정 product 객체를 반환
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    

# Product search
class ProductSearchViewSet(viewsets.ViewSet):
    
    # 쿼리 파라미터 받아, 해당 이름 포함하는 product 객체 반환
    def search(self, request):
        product_name = request.query_params.get('product_name', None)

        if product_name:
            queryset = Product.objects.filter(product_name__icontains=product_name).only('product_id', 'product_name', 'manufacturer', 'Capacity', 'category')
            if queryset.exists():
                serializer = ProductSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return Response({"message": "해당 상품이 없습니다."})
        return Response({"error": "상품명을 입력해 주세요"}, status=400) #400 code = 클라이언트측 에러 응답

    def retrieve(self, request, pk=None):
        try:
            product = Product.objects.get(pk=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "해당 상품이 없습니다"}, status=404)


# 상품을 카트에 추가하는 기능을 제공하는 API 뷰
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 사용 가능 (로그인)

    def post(self, request, product_id):    # 제품을 카트에 추가
        user = request.user
        product = get_object_or_404(Product, product_id=product_id)
        cart = get_object_or_404(Cart, user=user)

        if cart.items.count() >= 5:
            return Response({"error": "카트에 담을 수 있는 최대 상품 수는 5개입니다."}, status=status.HTTP_400_BAD_REQUEST)

        if CartItem.objects.filter(cart=cart, product=product).exists():
            return Response({"error": "이 상품은 이미 카트에 있습니다."}, status=status.HTTP_400_BAD_REQUEST)

        CartItem.objects.create(cart=cart, product=product)
        return Response({"success": "상품이 카트에 추가되었습니다."}, status=status.HTTP_201_CREATED)

# 카트 목록을 조회하는 API 뷰
class CartDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):     # 카트에 담긴 제품 목록을 반환 
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        items = cart.items.all()
        serializer = CartItemSerializer(items, many=True)
        return Response(serializer.data)


# 상품을 카트에서 삭제하는 기능을 제공하는 API 뷰
class CartItemDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, product_id):  # 제품을 카트에서 삭제
        user = request.user
        product = get_object_or_404(Product, product_id=product_id)
        cart = get_object_or_404(Cart, user=user)   # 카트가 로그인된 사용자인지 확인 

        try:
            cart_item = CartItem.objects.get(cart=cart, product=product)
            cart_item.delete()
            return Response({"success": "상품이 카트에서 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response({"error": "카트에 해당 상품이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)

# 카트 안의 모든 상품을 삭제하는 기능을 제공하는 API 뷰      
class CartClearView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        cart = get_object_or_404(Cart, user=user)
        cart.items.all().delete()
        return Response({"success": "카트가 비워졌습니다."}, status=status.HTTP_204_NO_CONTENT)
    


User = get_user_model() # 현재 활성 사용자 모델 반환/ settings.AUTH_USER_MODEL에 지정된 사용자 모델을 반환

# 비교기능
class CompareProductsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart_items = user.cart.items.all()

        if not user.disease:
            return Response({"error": "사용자의 질병 키워드가 설정되어 있지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        if not cart_items:
            return Response({"error": "카트에 상품이 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        disease = user.disease
        if disease == 'diabetes':  # 당뇨
            sorted_items = sorted(cart_items, key=lambda x: x.product.sugars)   #오름차순
        elif disease == 'obesity':  # 비만
            sorted_items = sorted(cart_items, key=lambda x: x.product.calories) #오름차순
        elif disease == 'hypertension':  # 고혈압
            sorted_items = sorted(cart_items, key=lambda x: x.product.sodium)   #오름차순
        elif disease == 'muscle_loss':  # 근손실
            sorted_items = sorted(cart_items, key=lambda x: x.product.protein, reverse=True)    #내림차순
        else:
            return Response({"error": "알 수 없는 질병 키워드입니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        best_product = sorted_items[0].product  # 추천상품

        # 추천 상품 저장
        RecommendedProduct.objects.create(
            user=user,
            product=best_product,
            product_name=best_product.product_name,
            disease=disease 
        )

        serializer = ProductSerializer(best_product)

        user.cart.items.all().delete()  # 비교 완료 후 카트 비우기

        # GnB 카운트 추가
        """
        참고 자료 : https://velog.io/@mechauk418/DRF-annotate
        """
        gnb_counts = RecommendedProduct.objects.filter(product=best_product, disease=disease).values('GNB').annotate(count=Count('GNB'))
        gnb_summary = {
            'Good': sum(item['count'] for item in gnb_counts if item['GNB'] == 'G'),
            'Bad': sum(item['count'] for item in gnb_counts if item['GNB'] == 'B')
        }

        response_data = {
            'recommended_product': serializer.data,
            'gnb_summary': gnb_summary, 
        }

        return Response(response_data, status=status.HTTP_200_OK)
    

# 별점 등록 기능을 위한 API 뷰
class RateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        recommended_product = get_object_or_404(RecommendedProduct, pk=pk, user=request.user)   # 로그인된 사용자인지 확인
        serializer = RecommendedProductRatingSerializer(recommended_product, data=request.data, partial=True)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

User = get_user_model()