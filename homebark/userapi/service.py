from .models import User,Quote

def outputservice(count):
    text = Quote.objects.order_by('?')[:count]
    return text

