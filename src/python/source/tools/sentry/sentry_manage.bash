(tact)hdknr@wzy:~/ve/tact/src/logging$ sentry --config=sentry.conf.py help

Usage: sentry subcommand [options] [args]

Options:
  -v VERBOSITY, --verbosity=VERBOSITY
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings=SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath=PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Print traceback on exception
  --version             show program's version number and exit
  -h, --help            show this help message and exit

Type 'sentry help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[django]
    clean_kombu_messages
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    runfcgi
    shell
    sql
    sqlall
    sqlclear
    sqlcustom
    sqlflush
    sqlindexes
    sqlinitialdata
    sqlsequencereset
    startapp
    startproject
    validate

[djcelery]
    camqadm
    celery
    celerybeat
    celerycam
    celeryctl
    celeryd
    celeryd_detach
    celeryd_multi
    celeryev
    celerymon
    djcelerymon

[gunicorn]
    run_gunicorn

[raven_compat]
    raven

[sentry]
    cleanup
    create_sample_event
    repair
    send_fake_data
    start
    upgrade

[sessions]
    clearsessions

[social_auth]
    clean_associations
    clean_nonces

[south]
    convert_to_south
    datamigration
    graphmigrations
    migrate
    migrationcheck
    schemamigration
    startmigration
    syncdb
    test
    testserver

[static_compiler]
    compilestatic

[staticfiles]
    collectstatic
    findstatic
    runserver
