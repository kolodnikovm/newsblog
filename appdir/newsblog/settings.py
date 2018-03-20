try:
    from .local_settings import *
except ImportError as e:
    print('No local_settings found')
