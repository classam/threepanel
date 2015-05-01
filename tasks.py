from invoke import task, run
from invoke.exceptions import Failure

def multiple(*args):
    return " && ".join(args)

@task()
def install():
    run("chmod a+x /home/vagrant/synced/install.sh")
    run("chmod a+x /home/vagrant/synced/resetdb.sh")
    run("bash /home/vagrant/synced/install.sh")

@task
def dev(command):
    return run(multiple("cd /home/vagrant/synced/threepanel/", command))

@task
def lint():
    return dev(multiple("pep8 */*.py --ignore=\"E128,E501,E402\"",
                       "pyflakes */*.py"))

@task
def watchlint():
    from watchie import Watchie
    w = Watchie()
    w.watch(path=".",
            result_fn=lint)
    w.start()

@task
def dj(command):
    return dev("python3 manage.py {}".format(command))

@task()
def runserver():
    print("Running server on localhost:8000")
    return dj("runserver 0:8000")

@task()
def reset():
    print("Resetting db")
    run("bash /home/vagrant/synced/resetdb.sh")
    dj("makemigrations")
    dj("migrate --noinput")
    dj("testdata")
