from winotify import Notification, audio

toast = Notification(app_id="WINDOWS",
                     title="System error 313 (0x139)",
                     msg="ITS A BUUUG HEEEEEELP!!!!!",
                     icon="C:/notifierPy/error.ico",)
toast.set_audio(audio.Mail, loop= True)

toast.show()