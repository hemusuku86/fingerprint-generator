# fingerprint-generator
Generate Fingerprint from User-Agent, In Python.<br>
Properties and Method results be consistent with User-Agent.<br>
### Now we have:
- all navigator properties!
- window.screen

### Aiming to add:
- more navigator
- more window properties
- canvas API reproduce
# 📚 Usage
Example:
```py
>>> import fp_generator
>>> fp = fp_generator.fingerprint("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36")
>>> fp.Navigator() # {'appCodeName': 'Mozilla'...
>>> fp.Navigator(languages=["en-US", "ja"])["language"] # "en-US", you can change languages manually because they're dependented with your IP or proxy.
>>> fp.Navigator()["maxTouchPoints"] # 0
>>> fp = fp_generator.fingerprint("Mozilla/5.0 (iPhone; CPU iPhone OS 18_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/138.0.7204.156 Mobile/15E148 Safari/604.1")
>>> fp.Navigator()["maxTouchPoints"] # 5 , ofc results will be consistent with your user-agent.
```
