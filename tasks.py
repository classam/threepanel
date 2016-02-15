from __future__ import print_function
import os
import sys

from invoke import run as silently_run
from invoke import task
from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.RED, file=sys.stderr)

def run(cmd, *args, **kwargs):
    """
    We're overwriting invoke's "run" to always
    print out the command it's running before it runs.
    It also does color things.
    """
    print(Fore.RED, file=sys.stderr)
    if not cmd:
        return
    print(Fore.GREEN + cmd)
    print(Style.RESET_ALL)
    print(Style.DIM)
    silently_run(cmd, *args, **kwargs)
    print(Style.RESET_ALL)

def env_to_string(debug='True'):
    """
    These keys need to be defined in the environment for
    the installation to work. We check if they are all
    defined, then convert them to a string so that
    we can pass them in to the installation script.
    """
    os.environ['DJANGO_DEBUG'] = debug
    keys = ['DIGITALOCEAN_API_TOKEN',
            'DJANGO_PROJECT_SLUG',
            'DJANGO_DOMAIN',
            'DJANGO_DEBUG',
            'DJANGO_ADMIN_NAME',
            'DJANGO_ADMIN_EMAIL',
            'POSTGRES_DB_PASSWORD',
            'MANDRILL_KEY',
            'DJANGO_SECRET_KEY']
    for key in keys:
        if key not in os.environ:
            print("Warning: {} not defined.".format(key), file=sys.stderr)
    env_variables = {"{}=\"{}\"".format(key,os.environ[key]) for key in
                     os.environ if key in keys}
    string = " ".join(env_variables)
    return string

@task
def vagrant(command):
    return run("vagrant ssh -c '{}'".format(command))

@task
def vagrant_invoke(command):
    return run(vagrant("source django_environment/bin/activate && cd vagrant_django/threepanel && invoke {}".format(command)))

@task
def get_media():
    run("scp -r vagrant@threepanel.com:/home/vagrant/vagrant_django/media .")

@task
def get_current_db():
    db_password = os.environ['POSTGRES_DB_PASSWORD']
    run("ssh vagrant@threepanel.com \"sudo -u postgres pg_dump threepanel > /tmp/last.db_backup\"")
    run("scp vagrant@threepanel.com:/tmp/last.db_backup /tmp/last.db_backup")
    run("vagrant scp /tmp/last.db_backup /tmp/last.db_backup")
    vagrant("sudo -u postgres psql -d threepanel -f /tmp/last.db_backup".format(db_password))

@task
def install(production=False):
    install_path = "/home/vagrant/vagrant_django/configuration/install.py"
    if not production:
        run("vagrant up --provider virtualbox")
        cmd = "sudo {} python3 {}".format(env_to_string(debug='True'), install_path)
        vagrant(cmd)
    else:
        get_media()
        run("vagrant up --provider digital_ocean")
        cmd = "sudo {} python3 {}".format(env_to_string(debug='False'), install_path)
        vagrant(cmd)
        vagrant_invoke("auth_keys")
    get_current_db()
    vagrant_invoke("makemigrations")
    vagrant_invoke("migrate")
    if production:
        vagrant_invoke("prod_restart")

@task
def clean():
    run("vagrant destroy -f")
    run("rm -rf vars.ini")
    run("rm -rf scripts")
    run("rm -rf __pycache__")
