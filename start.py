__author__ = 'user'

# import sys
# sys.path.append('C:\work.py\PycharmProjects')
from cmn.etc import *
import subprocess

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

if __name__ == "__main__":
    print('DateTime: ' + getDateTime())
    print('Python:   ' + getPythonVer())
    print('Django:   ' + getDjangoVer())
    print('CMS:      ' + getDjangoCmsVer())
    print('Cmn:      ' + getCmnVer())
