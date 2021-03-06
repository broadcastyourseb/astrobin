from kombu import Exchange, Queue


BROKER_URL = 'amqp://astrobin:astrobin@rabbitmq:5672'
BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': 3600,
    'fanout_prefix': True,
    'fanout_patterns': True,
}
CELERY_RESULT_BACKEND = 'cache+memcached://memcached:11211/'
CELERY_IMPORTS = ('astrobin.tasks', 'rawdata.tasks', 'djcelery_email.tasks')
CELERY_DEFAULT_QUEUE = 'default'
CELERY_HAYSTACK_QUEUE = 'haystack'
CELERY_ACCEPT_CONTENT = ['pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = TIME_ZONE

CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('haystack', Exchange('haystack'), routing_key='haystack'),
    Queue('thumbnails', Exchange('thumbnails'), routing_key='thumbnails'),
)
CELERY_ROUTES = {
    'astrobin.tasks.retrieve_thumbnails': {
        'queue': 'thumbnails',
        'routing_key': 'thumbnails',
    },
}
