__author__ = 'user'


def getDateTime(aFmt="%M-%S-%f"):
    import datetime
    assert isinstance(aFmt, str), "Format isn't string"
    dateTimeStr = datetime.datetime.now().strftime(aFmt)
    return dateTimeStr

def dbg(aMsg):
	import logging
	from inspect import getframeinfo, stack
	
	log = logging.getLogger('debug')
	'''
	import inspect
	curFrame = inspect.currentframe()
	calFrame = inspect.getouterframes(curFrame, 2)
	calName = calFrame[1][3]
	
	log.debug('---------')
	log.debug(calName + ' ' + getDateTime('%H%M%S') + ': ' +aMsg)
	log.debug(inspect.currentframe().f_back.f_code.co_name)
	log.debug('------------------')
	log.debug(inspect.getframeinfo(curFrame, 1))
	log.debug('------------------')
	log.debug(inspect.getframeinfo(curFrame, 2))
	log.debug('------------------')
	log.debug(inspect.getouterframes(curFrame, 1))
	log.debug('------------------')
	log.debug(inspect.getouterframes(curFrame, 2))
	log.debug('------------------')
	log.debug(curFrame.f_back.f_code.co_name)
	
	frame = inspect.currentframe()
	## Keep moving to next outer frame
	while True:
		try:
			frame = frame.f_back
			name = frame.f_code.co_name
			log.debug(name)
		except:
			break
	'''
	caller = getframeinfo(stack()[1][0])
	#print("%s:%d - %s" % (caller.filename, caller.lineno, '!!!'))
	log.debug("%s:%d" % (caller.filename, caller.lineno))
	log.debug(aMsg)
	#log.debug(caller)

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
