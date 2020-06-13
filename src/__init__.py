import gettext

from os import environ

from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS


def localeInit():
	environ["LANGUAGE"] = language.getLanguage()[:2]
	gettext.bindtextdomain("YouTube", resolveFilename(SCOPE_PLUGINS,
		"Extensions/YouTube/locale"))


def _(txt):
	t = gettext.dgettext("YouTube", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t


def ngettext(singular, plural, n):
	t = gettext.dngettext("YouTube", singular, plural, n)
	if t in (singular, plural):
		t = gettext.ngettext(singular, plural, n)
	return t


localeInit()
language.addCallback(localeInit)
