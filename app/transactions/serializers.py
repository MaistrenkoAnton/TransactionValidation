from rest_framework import serializers

from transactions.validators import is_valid_currency


class MoneySerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)
    currency = serializers.CharField(required=True, validators=[is_valid_currency])


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


class TenderSerializer(serializers.Serializer):
    type = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    total_money = MoneySerializer(required=True)


class TaxSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    rate = serializers.FloatField(required=True)
    is_custom_amount = serializers.BooleanField(required=True)
    applied_money = MoneySerializer(required=True)


class ModifierSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    quantity = serializers.CharField(required=True)
    applied_money = MoneySerializer(required=True)


class VariationSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    pricing_type = serializers.CharField(required=True)
    price_money = MoneySerializer(required=True)


class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)


class ItemizationSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    total_money = MoneySerializer(required=True)
    single_quantity_money = MoneySerializer(required=True)
    gross_sales_money = MoneySerializer(required=True)
    discount_money = MoneySerializer(required=True)
    net_sales_money = MoneySerializer(required=True)
    category = CategorySerializer(required=True)
    variation = VariationSerializer(required=True)
    taxes = TaxSerializer(required=True, many=True)
    modifiers = ModifierSerializer(required=True, many=True)


class TransactionSerializer(serializers.Serializer):
    _id = serializers.CharField(required=True)
    business_id = serializers.UUIDField(required=True)
    location_id = serializers.UUIDField(required=True)
    transaction_id = serializers.UUIDField(required=True)
    receipt_id = serializers.CharField(required=True)
    serial_number = serializers.CharField(required=True)
    dining_option = serializers.CharField(required=True)
    creation_time = serializers.CharField(required=True)
    discount_money = MoneySerializer(required=True)
    additive_tax_money = MoneySerializer(required=True)
    inclusive_tax_money = MoneySerializer(required=True)
    refunded_money = MoneySerializer(required=True)
    tax_money = MoneySerializer(required=True)
    tip_money = MoneySerializer(required=True)
    total_collected_money = MoneySerializer(required=True)
    creator = UserSerializer(required=True)
    tender = TenderSerializer(required=True)
    taxes = TaxSerializer(required=True, many=True)
    itemization = ItemizationSerializer(required=True, many=True)
