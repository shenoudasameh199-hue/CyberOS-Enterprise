import string, random
from rich.console import Console
def generate_password(length=18):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))
