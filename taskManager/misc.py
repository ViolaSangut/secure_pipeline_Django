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

import subprocess
import os

def save_uploaded_file(uploaded_file, upload_dir_path, title):
    # Ensure destination folder exists
    os.makedirs(upload_dir_path, exist_ok=True)

    src = uploaded_file.temporary_file_path()
    dst = os.path.join(upload_dir_path, title)

    # Use subprocess with list form to prevent shell injection
    subprocess.run(['mv', src, dst], check=True)


    return '/static/taskManager/uploads/%s' % (title)
