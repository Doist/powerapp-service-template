A template for your PowerApp service
------------------------------------

To start with a new service integration, assuming you have already installed
locally the PowerApp Django project, just do following::

    mkdir ../powerapp-myname
    ./manage.py startapp powerapp_myname ../powerapp-myname --template=https://github.com/Doist/powerapp-service-template/archive/master.zip

Change to your app's name directory, change setup.py and replace application
name from "powerapp_myname" to "powerapp-myname". This step is optional but
desirable: most Python packages follow the convention of dash-separated names
for PyPI packages and underscore-separated name for Python modules.

To start hacking, install the app locally with::

    pip install -e .

Then type `./manage.py collect_services` and make sure your service is found
and added to the list of known services by PowerApp.

Replace this text with application installation instructions when you're ready
to publish your work.
