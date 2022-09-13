import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres host=localhost password=2345")

cur = conn.cursor()

# cur.execute("CREATE TABLE weather2 (city varchar(80), temp int, daydate date);")

# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Minsk', 16, '2022-09-06')")
# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Minsk', 13, '2022-09-07')")
# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Gomel', 20, '2022-09-06')")
# cur.execute("INSERT INTO weather2 (city, temp, daydate) VALUES ('Gomel', 22, '2022-09-07')")

cur.execute("SELECT * FROM weather2;")

# print(cur.fetchone())
# print('-------------------------------------------------------------------------------------------')
for ln in cur.fetchall():
    print(ln)
# print(cur.fetchall())

conn.commit()
cur.close()
conn.close()




LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console_debug_format': {
            'format': '%(asctime)s %(levelname)s - %(message)s'
        },
        'console_warning_format': {
            'format': '%(asctime)s %(levelname)s - %(message)s - %(pathname)s'
        },
        'console_error_critical_format': {
            'format': '%(asctime)s %(levelname)s - %(message)s - %(pathname)s - %(exc_info)s'
        },
        'mail_format': {
            'format': '%(asctime)s %(levelname)s - %(message)s - %(pathname)s'
        },
        'security_format': {
            'format': '%(asctime)s %(levelname)s - %(module)s - %(message)s'
        },
        'general_log_format': {
            'format': '%(asctime)s %(levelname)s - %(module)s - %(message)s'
        },

    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug_format',
            'filters': ['require_debug_true'],
        },
        'console_warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning_format',
        },
        'console_error_critical': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'console_error_critical_format',
        },
        'general_file': {
            'class': "logging.FileHandler",
            'filename': "general.log",
            'level': "INFO",
            'filters': ['require_debug_false'],
            'formatter': 'general_log_format',
        },
        'errors_file': {
            'class': "logging.FileHandler",
            'filename': "errors.log",
            'level': "ERROR",
            'formatter': 'console_error_critical_format',
        },
        'security_file': {
            'class': "logging.FileHandler",
            'filename': "security.log",
            'level': "WARNING",
            'formatter': "",
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'mail_format',
        },
    },
    'loggers': {
        'console_debug': {
            'handlers': ['console_debug'],
            'propagate': True,
        },
        'console_warning': {
            'handlers': ['console_warning'],
            'propagate': True,
        },
        'console_error': {
            'handlers': ['console_error_critical'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db_backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file'],
            'level': 'WARNING',
            'propagate': False,
        }
    }
}