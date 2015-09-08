@call _setEnv

@set params=

@set params=%params% --i18n no
@set params=%params% --use-tz yes
@set params=%params% --reversion yes
@set params=%params% --permissions no
@set params=%params% --parent-dir .
@set params=%params% --languages ru
@set params=%params% --bootstrap no
@set params=%params% --starting-page no
@set params=%params% --skip-empty-check
@set params=%params% %PROJ_NAME%

@set DJANGO_SETTINGS_MODULE=

djangocms %params%