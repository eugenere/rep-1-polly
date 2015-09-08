__author__ = 'user'

def safeCallMaker(aDef='False'):
    def decorator(aFunc):
        def wrapper():
            try:
                return aFunc()
            except Exception:
                return aDef
        return wrapper
    return decorator

def getPythonVer():
    import sys
    ver = '{0}.{1}.{2}'.format(
        sys.version_info.major,
        sys.version_info.minor,
        sys.version_info.micro)
    return ver

@safeCallMaker('not found')
def getDjangoVer():
    import django
    ver = django.get_version()
    return ver

@safeCallMaker('not found')
def getDjangoCmsVer():
    from cms import __version__ as ver
    return ver

def getCmnVer():
    return '0.0.1'

def setDjangoConfig(aName):
    import django, os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", aName + ".settings")
    django.setup()

def getDateTime(aFmt = "%M-%S-%f"):
    import datetime
    assert isinstance(aFmt, str), "Format isn't string"
    dateTimeStr = datetime.datetime.now().strftime(aFmt)
    return dateTimeStr
