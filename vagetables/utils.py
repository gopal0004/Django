import uuid
from django.utils.text import slugify



def generate_slug(title : str) -> str:

    from .models import Receipe

    title = slugify(title)

    while(Receipe.objects.filter(slug = title).exists()):
        title = f'{slugify(title)} - {str(uuid.uuid4())[0:4]}'

    return title