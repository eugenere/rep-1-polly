__author__ = 'user'

# import sys
# sys.path.append('C:\work.py\PycharmProjects')
from cmn.etc import *
import subprocess
from django.core import management

import msvcrt

def newCmsProj(aProjName):
    import sys, os
    # sys.path.append('C:\work.py\envs\polly1\Scripts')
    params = \
    (
        ' --i18n no'
        ' --use-tz yes'
        ' --reversion yes'
        ' --permissions no'
        ' --parent-dir .'
        ' --languages ru'
        ' --bootstrap no'
        ' --starting-page no'
        ' --skip-empty-check'
        ' ' + aProjName
    )

    params = '-h'
    cmd = 'djangocms ' + params
    # cmd = "echo '" + cmd + "'"
    # cmd = "help"
    print(cmd);
    # subprocess.call("start cmd /k djangocms", shell=True)

    state = os.system(cmd)
    print('state: ' + str(state))

def test2():
    ml1 = \
    (
        's1p1'
        's1p2'
        's1p3'
        's1p4'
    )
    print(ml1)

    ml2 = """\
        s2p1\
        s2p2
        s2p3\
    print(ml2)
        s2p4
        """

    ml3 = \
        's3p1'\
        's3p2'\
        's3p3'\
        's3p4'

    print(ml3)

def doHttpRequest(aReq):
    pass

def getSqliteVer():
    import sqlite3
    return sqlite3.version

def fillSqlite(aDbFile, aSqlFile):
    import sqlite3, os

    with sqlite3.connect(aDbFile) as conn:
        with open(aSqlFile, 'rt') as sqlFile:
            schema = sqlFile.read()
            conn.executescript(schema)

def dumpSqlite(aDbFile, aSqlFile):
    import sqlite3, os

    with sqlite3.connect(aDbFile) as conn:
        with open(aSqlFile, 'w') as f:
            for line in conn.iterdump():
                f.write('%s\n' % line)
    

if __name__ == "__main__":
    print('DateTime: ' + getDateTime())
    print('Python:   ' + getPythonVer())
    print('Django:   ' + getDjangoVer())
    print('CMS:      ' + getDjangoCmsVer())
    print('Sqlite:   ' + getSqliteVer())
    print('Cmn:      ' + getCmnVer())

    # dumpSqlite('project.db', 'dump.sql')
    # fillSqlite('project2.db', 'dump.sql')
    # input("Press any key to exit")

    management.call_command('help', verbosity=0, interactive=False)
    
    print("Press any key")
    msvcrt.getch()


