#     _  _                        __   __
#  __| |(_)__ _ _ _  __ _ ___   _ \ \ / /
# / _` || / _` | ' \/ _` / _ \_| ' \ V /
# \__,_|/ \__,_|_||_\__, \___(_)_||_\_/
#     |__/          |___/
#
#			INSECURE APPLICATION WARNING
#
# django.nV is a PURPOSELY INSECURE web-application
# meant to demonstrate Django security problems
# UNDER NO CIRCUMSTANCES should you take any code
# from django.nV for use in another web application!
#
""" misc.py contains miscellaneous functions

    Functions that are used in multiple places in the
    rest of the application, but are not tied to a
    specific area are stored in misc.py
"""

import os
import shutil


def store_uploaded_file(title, uploaded_file):
    """Securely stores a temporary uploaded file on disk"""
    upload_dir_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'static',
        'taskManager',
        'uploads'
    )

    os.makedirs(upload_dir_path, exist_ok=True)

    source_path = uploaded_file.temporary_file_path()
    destination_path = os.path.join(upload_dir_path, title)

    # Secure file move (no shell command)
    shutil.move(source_path, destination_path)

    return f'/static/taskManager/uploads/{title}'
