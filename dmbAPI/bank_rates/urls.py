from .views import BankRatesViewSet

routeList = (
    (r'bank_rates', BankRatesViewSet, 'bank_rates'),
)
