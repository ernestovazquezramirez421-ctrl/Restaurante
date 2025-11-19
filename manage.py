#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Forzar variable de entorno para Render gratuito
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "restaurante.settings")
    
    # Forzar la ruta del proyecto
    current_path = os.path.dirname(os.path.abspath(__file__))
    if current_path not in sys.path:
        sys.path.append(current_path)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and available on your PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
