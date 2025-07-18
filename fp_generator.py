import random

class fingerprint:
    def __init__(self, user_agent):
        self.ua = user_agent
        if "Chrome/" in self.ua or "CriOS" in self.ua or "FxiOS" in self.ua:
            self.engine = "chromium"
        elif "Firefox/" in self.ua and "Windows" in self.ua:
            self.engine = "firefox"
        else:
            raise BaseException("Unsupported User-Agent. (Currently, Chromium and Windows Firefox are only supported)")
    def Navigator(self, languages=["ja"]):
        firefox_version = int(self.ua.split("Firefox/")[1].split(" ")[0]) if self.engine == "firefox" else 0
        navigator = {
            "appCodeName": "Mozilla",
            "appName": "Netscape",
            "appVersion": {"chromium": self.ua.split("Mozilla/")[1], "firefox": "5.0 (Windows)"}[self.engine],
            # "bluetooth": "",
            "buildID": "20181001000000" if self.engine == "firefox" else "UNDEFINED",
            "clipboard": '[object Clipboard]',
            "connection": '[object NetworkInformation]' if self.engine == "chromium" else "UNDEFINED",
            #"contancts": "",
            "cookieEnabled": True,
            "credentials": '[object CredentialsContainer]',
            "deviceMemory": random.choice([4,8]) if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "devicePosture": '[object DevicePosture]' if self.engine == "chromium" else "UNDEFINED",
            "doNotTrack": "UNDEFINED" if "like Mac OS X" in self.ua else (None if self.engine == "chromium" else "unspecified"),
            "geolocation": "undefined",
            "globalPrivacyControl": False if self.engine == "firefox" else "UNDEFINED",
            "gpu": '[object GPU]' if self.engine == "chromium" or firefox_version > 140 else "UNDEFINED",
            "hardwareConcurrency": random.choice([4,8]),
            "hid": '[object HID]' if self.engine == "chromium" and "like Mac OS X" not in self.ua and "Android" not in self.ua else "UNDEFINED",
            "ink": '[object Ink]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "keyboard": '[object Keyboard]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "language": languages[0],
            "languages": languages,
            "locks": '[object LockManager]',
            "login": '[object NavigatorLogin]' if "like Mac OS X" not in self.ua else "UNDEFINED",
            "maxTouchPoints": 5 if "iPhone" in self.ua else 11 if "iPad" in self.ua else random.choice([5,10]) if "Mobile/" in self.ua else 0,
            "mediaCapabilities": '[object MediaCapabilities]',
            "mediaDevices": '[object MediaDevices]',
            "mimeTypes": "[object MimeTypeArray]",
            "onLine": True,
            "oscpu": "Windows NT 10.0; Win64; x64" if self.engine == "firefox" else "UNDEFINED",
            "pdfViewerEnabled": True,
            "permissions": '[object Permissions]',
            "platform": "Win32" if "Windows" in self.ua else "iPhone" if "iPhone" in self.ua else "UNDEFINED", # i don't have more devices
            "plugins": [{'name': 'PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'Chrome PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'Chromium PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'Microsoft Edge PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'WebKit built-in PDF', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}],
            "presentation": '[object Presentation]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "product": "Gecko",
            "productSub": "20030107" if self.engine == "chrome" else "20100101",
            "scheduling": '[object Scheduling]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "serial": '[object Serial]' if self.engine == "chromium" and "like Mac OS X" not in self.ua and "Android" not in self.ua else "UNDEFINED",
            "serviceWorker": '[object ServiceWorkerContainer]' if "like Mac OS X" not in self.ua else "UNDEFINED",
            "storage": '[object StorageManager]',
            "usb": '[object USB]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "userActivation": '[object UserActivation]',
            "userAgent": self.ua,
            "userAgentData": '[object NavigatorUAData]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "vendor": "" if self.engine == "firefox" else "Apple Computer, Inc." if "like Mac OS X" in self.ua else "Google Inc.",
            "vendorSub": "",
            "virtualKeyboard": '[object VirtualKeyboard]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "wakeLock": '[object WakeLock]',
            "webdriver": False, # You should set this True to get unflagged lol
            "windowControlsOverlay": '[object WindowControlsOverlay]' if self.engine == "chromium" and "like Mac OS X" not in self.ua and "Android" not in self.ua else "UNDEFINED",
            "xr": '[object XRSystem]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED"
        }
        for k in list(navigator.keys()):
            if navigator[k] == "UNDEFINED":
                del navigator[k]
        return navigator
