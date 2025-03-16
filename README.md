# Better Project And App Structure for Django

This repository contains two templates: one for project structure and one for app structure. These templates make
working with Django projects much more structured. But you'll need uv installed.

You can use these by referring to their release files during project/app creation:

    uv run --with=django \
           django-admin startproject \
           --extension=py,toml,md \
           --template=https://github.com/shezi/django-better-project-template/releases/download/1.0.1/project_template.zip \
           <project_name>

    # to start an app
    ./manage.py startapp --template https://github.com/shezi/django-better-project-template/releases/download/1.0.1/app_template.zip <app_name>

I also host the files on my domain for shorter paths:

    uv run --with=django \
           django-admin startproject \
           --extension=py,toml,md \
           --template=https://shezi.de/project_template.zip \
           <project_name>

    # to start an app
    ./manage.py startapp --template https://shezi.de/project_template.zip <app_name>; mv <app_name> apps/
