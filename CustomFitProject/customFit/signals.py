""" 사용자가 생성될 때마다 자동으로 맞춤건강카트를 생성하는 역할"""

from django.db.models.signals import post_save  #사용자 모델이 저장된 후에 실행
from django.dispatch import receiver
from accounts.models import CustomUser
from .models import Cart

# 새로운 사용자가 생성될 때 호출되며, 자동으로 카트를 생성
@receiver(post_save, sender=CustomUser)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

#사용자 정보가 저장될 때 카트도 함께 저장
@receiver(post_save, sender=CustomUser)
def save_user_cart(sender, instance, **kwargs):
    instance.cart.save()