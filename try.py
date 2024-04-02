# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': {
#             'format': '%{levelname}s %{message}s'
#         },
#         'verbose': {
#             'format': '{levelname} {ascitime} {module} {process} {thread} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter' : 'verbose',
#         },
#         'file': {
#             'class': 'logging.FileHandler',
#             'filename': './log/django.log',
#             'formatter' : 'verbose',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'INFO',
#         },
#         'myapp': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }

# LOGGING = {
#  'version': 1,
#  'disable_existing_loggers': False,
#  'formatters': {
#  'verbose': {
#  'format': '{levelname} {asctime} {module} {process} {thread} {message}',
#  'style': '{',
#  },
#  'simple': {
#  'format': '%(levelname)s %(message)s'
#  },
#  },
#  'handlers': {
#  'console': {
#  'class': 'logging.StreamHandler',
#  'formatter': 'verbose', # добавлен параметр formatter
#  },
#  'file': {
#  'class': 'logging.FileHandler',
#  'filename': './log/django.log',
#  'formatter': 'verbose', # добавлен параметр formatter
#  },
#  },
#  'loggers': {
#  'django': {
#  'handlers': ['console', 'file'],
#  'level': 'INFO',
#  },
#  'myapp': {
#  'handlers': ['console', 'file'],
#  'level': 'DEBUG',
#  'propagate': True,
#  },
#  },
# }


from random import random, randint

b = random() + randint(10, 1000)

print(b)