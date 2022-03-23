# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
from octoprint.events import Events

class iFramePlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Set up and ready to go! (Default: %s)" % self._settings.get(["url"]))

	def get_settings_defaults(self):
		return dict(url="http://en.m.wikipedia.org/wiki/Hello_world")
		# return dict(url="http://192.168.0.148:8000/")

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/iframe.js"],
			css=["css/iframe.css"],
			less=["less/iframe.less"]
		)

__plugin_pythoncompat__ = ">=2.7,<4"  # python 2 and 3

__plugin_name__ = "iFrame"
__plugin_implementation__ = iFramePlugin()



def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = iFramePlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
