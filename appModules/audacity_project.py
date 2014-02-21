--- start ---
# Audacity App Module for NVDA


import appModuleHandler

class AppModule(appModuleHandler.AppModule):

	def event_gainFocus(self, obj, nextHandler):
		import tones
		tones.beep(550, 50)
		nextHandler()


	__gestures={
		"kb:NVDA+ctrl+s": "announceNVDAVersion",
	}
--- end ---