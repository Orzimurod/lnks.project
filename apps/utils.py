import string
import random
from apps.lnks_app.models import Link

def generate_short_code(len=5):
    chars=string.ascii_letters+string.digits
    while True:
        short_code= random.choices(chars,k=len)
        if not Link.objects.filter(short_code=short_code).exists():
            return short_code
