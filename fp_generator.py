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
        firefox_version = float(self.ua.split("Firefox/")[1].split(" ")[0]) if self.engine == "firefox" else 0
        navigator = {
            "appCodeName": "Mozilla",
            "appName": "Netscape",
            "appVersion": {"chromium": self.ua.split("Mozilla/")[1], "firefox": "5.0 (Windows)"}[self.engine],
            "bluetooth": "[object Bluetooth]" if self.engine == "chromium" and "Android" in self.ua else "UNDEFINED",
            "buildID": "20181001000000" if self.engine == "firefox" else "UNDEFINED",
            "clipboard": '[object Clipboard]',
            "connection": '[object NetworkInformation]' if self.engine == "chromium" else "UNDEFINED",
            "contancts": "[object ContactsManager]" if self.engine == "chromium" and "Android" in self.ua else "UNDEFINED",
            "cookieEnabled": True,
            "credentials": '[object CredentialsContainer]',
            "deviceMemory": random.choice([4,8]) if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "devicePosture": '[object DevicePosture]' if self.engine == "chromium" else "UNDEFINED",
            "doNotTrack": "UNDEFINED" if "like Mac OS X" in self.ua else (None if self.engine == "chromium" else "unspecified"),
            "geolocation": "[object Geolocation]",
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
            "maxTouchPoints": 5 if "iPhone" in self.ua else 11 if "iPad" in self.ua else random.choice([5,10]) if "Mobile" in self.ua else 0,
            "mediaCapabilities": '[object MediaCapabilities]',
            "mediaDevices": '[object MediaDevices]',
            "mimeTypes": "[object MimeTypeArray]",
            "onLine": True,
            "oscpu": "Windows NT 10.0; Win64; x64" if self.engine == "firefox" else "UNDEFINED",
            "pdfViewerEnabled": True,
            "permissions": '[object Permissions]',
            "platform": "Win32" if "Windows" in self.ua else "iPhone" if "iPhone" in self.ua else "Linux armv81" if "Android" in self.ua else "UNDEFINED", # i don't have more devices
            "plugins": [{'name': 'PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'Chrome PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'Chromium PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'Microsoft Edge PDF Viewer', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}, {'name': 'WebKit built-in PDF', 'description': 'Portable Document Format', 'mimeTypes': [{'type': 'application/pdf', 'suffixes': 'pdf'}, {'type': 'text/pdf', 'suffixes': 'pdf'}]}],
            "presentation": '[object Presentation]' if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
            "product": "Gecko",
            "productSub": "20030107" if self.engine == "chromium" else "20100101",
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
    def screen(self):
        iphone_css_screen_size = {'iPhone3G': [320, 480, 'iPhone OS 4_2_1'], 'iPhone3GS': [320, 480, 'iPhone OS 6_1_6'], 'iPhone4': [320, 480, 'iPhone OS 7_1_2'], 'iPhone5': [320, 568, 'iPhone OS 10_3_3'], 'iPhone5c': [320, 568, 'iPhone OS 10_3_3'], 'iPhone5s': [320, 568, 'iPhone OS 12_5_1'], 'iPhone6': [375, 667, 'iPhone OS 12_5_1'], 'iPhone6Plus': [414, 736, 'iPhone OS 12_5_1'], 'iPhone6s': [375, 667, 'iPhone OS 15_7_8'], 'iPhone6sPlus': [414, 736, 'iPhone OS 15_7_8'], 'iPhoneSE': [320, 568, 'iPhone OS 15_7_8'], 'iPhone7': [375, 667, 'iPhone OS 15_7_8'], 'iPhone7plus': [414, 736, 'iPhone OS 15_7_8'], 'iPhone8': [375, 667, "iPhone OS 16_7_4"], 'iPhone8Plus': [414, 736, "iPhone OS 16_7_4"], 'iPhoneX': [375, 812, "iPhone OS 16_7_4"], 'iPhoneXS': [375, 812, None], 'iPhoneXS MAX': [414, 896, None], 'iPhoneXR': [414, 896, None], 'iPhone11': [414, 896, None], 'iPhone11 Pro': [375, 812, None], 'iPhone11 Pro MAX': [414, 896, None], 'iPhoneSE（2nd gen）': [375, 667, None], 'iPhone12mini': [375, 812, None], 'iPhone12': [390, 844, None], 'iPhone12 Pro': [390, 844, None], 'iPhone12 Pro MAX': [428, 926, None], 'iPhone13mini': [375, 812, None], 'iPhone13': [390, 844, None], 'iPhone13 Pro': [390, 844, None], 'iPhone13 Pro MAX': [428, 926, None], 'iphoneSE（3nd gen）': [375, 667, None], 'iPhone 14': [390, 844, None], 'iPhone 14 Plus': [428, 926, None], 'iPhone 14 Pro': [390, 844, None], 'iPhone 14 Pro Max': [430, 932, None], 'iPhone 15': [393, 852, None], 'iPhone 15plus': [430, 932, None], 'iPhone 15pro': [393, 852, None], 'iPhone 15promax': [430, 932, None], 'iPhone 16': [393, 852, None], 'iPhone 16 Plus': [430, 932, None], 'iPhone 16 Pro': [402, 874, None], 'iPhone 16 Pro Max': [440, 956, None]}
        if "iPhone OS " in self.ua:
            ios_version = self.ua.split("iPhone OS ")[1].split(" ")[0].split("_")
            if len(ios_version) == 2:
                ios_version.append("0")
            ios_version = int("".join(ios_version))
            versions = []
            for v in list(iphone_css_screen_size.values()):
                if v[2] not in versions:
                    versions.append(v[2])
            for i in range(len(versions)):
                currentv = versions[i]
                nextv = versions[i+1]
                current_v = currentv.split("iPhone OS ")[1].split(" ")[0].split("_")
                if len(current_v) == 2:
                    current_v.append("0")
                current_v = int("".join(current_v))
                if nextv == None:
                    next_v = current_v + 1
                else:
                    next_v = nextv.split("iPhone OS ")[1].split(" ")[0].split("_")
                    if len(next_v) == 2:
                        next_v.append("0")
                    next_v = int("".join(next_v))
                if sorted([current_v, ios_version, next_v]) == [current_v, ios_version, next_v]:
                    near_version = versions[i+1]
                    break
                elif nextv == None:
                    near_version = None
                    break
            available_sizes = [v for v in list(iphone_css_screen_size.values()) if v[2] == near_version]
            size = random.choice(available_sizes)
            [height, width, availHeight, availWidth] = [size[1],size[0],size[1],size[0]]
        elif "Mobile" in self.ua:
            width = random.randint(320,480)
            height = int((width/9) * 19.5)
            [availHeight, availWidth] = [height, width]
        else:
            popular_resolutions = [
                [1920,1080],
                [1366,768],
                [1536,864]
            ]
            size = random.choice(popular_resolutions)
            [height, width, availHeight, availWidth] = [size[1], size[0], size[1] - 48 if "Windows" in self.ua else size[1], size[0]]
        screen = {
                "availHeight": availHeight,
                "availLeft": 0,
                "availTop": 0,
                "availWidth": availWidth,
                "colorDepth": 24,
                "height": height,
                "isExtended": False if "Mobile" in self.ua and "like Mac OS X" not in self.ua else random.choice([True,False]) if self.engine == "chromium" and "like Mac OS X" not in self.ua else "UNDEFINED",
                "left": 0,
                "mozOrientation": "landscape-primary" if self.engine == "firefox" else "UNDEFINED",
                "orientation": '[object ScreenOrientation]',
                "pixelDepth": 24,
                "top": 0,
                "width": width
            }
        for k in list(screen.keys()):
            if screen[k] == "UNDEFINED":
                del screen[k]
        return screen
    def window(self):
        window = {
            "screen": self.screen()
        }
        for k in list(window.keys()):
            if window[k] == "UNDEFINED":
                del window[k]
        return window
