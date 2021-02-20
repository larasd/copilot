<<<<<<< HEAD
#!C:\Users\paulo\PycharmProjects\copilot\venv\Scripts\python.exe
=======
#!C:\Users\a055507\PycharmProjects\copilot\venv\Scripts\python.exe
>>>>>>> 9ef8cee19e522686019b7b3722dae35f321afcfc
# When the django-admin.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-admin.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-admin instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-admin.py is deprecated in favor of django-admin.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
