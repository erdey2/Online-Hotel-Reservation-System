"""
WSGI config for room_slot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

# Add the project directory to the sys.path
sys.path.append('/home/erdey/Desktop/OHRS2/room_slot')  # Change this to the actual path of your OHRS2 directory

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'room_slot.settings')

application = get_wsgi_application()


