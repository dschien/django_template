DATABASES = {
    'default': {
        'USER': '<TODO>', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
        'PASSWORD': '<TODO>', # Not used with sqlite3.
    }
}

import os
logs_folder = os.path.join(__file__, './../var/log/')

# Make this unique, and don't share it with anybody.
# Generate your own
SECRET_KEY = ''

EMAIL_HOST_USER = '<google email user>'
EMAIL_HOST_PASSWORD = '<password>'
