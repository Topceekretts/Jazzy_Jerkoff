import json
import logging
import os
import random
from time import sleep
from pwnagotchi import plugins

class JazzyJerkoff(plugins.Plugin):
    __GitHub__ = ""
    __author__ = "TOPCEEKRETTS & ChatGPT"
    __version__ = "2.0.0"
    __license__ = "GPL3"
    __description__ = "Jazzy Jerkoff – filthy, lying, packet-fishing beast."
    __name__ = "JazzyJerkoff"
    __help__ = "Unleash Jazzy. Expect nonsense, lies, and filthy packet probing."

    __dependencies__ = {"apt": ["none"],"pip": ["scapy"]}

    __defaults__ = {"enabled": True,"rage_level": 2,"beacon_flood": True,"probe_spam": True}

    def __init__(self):
        self.ready = False
        logging.debug(f"[{self.__class__.__name__}] plugin init")
        self.running = False
        self.quotes = [
            "Jazzy once seduced a firewall by whispering port numbers into its backend.",
            "My doodle’s not small, it’s just encrypted in stealth mode.",
            "I taught Edward Snowden everything he knows... while pole dancing.",
            "I once fished a packet out of a toilet and called it a payload.",
            "Your MAC address gave me chlamydia.",
            "Jazzy’s dongle was banned from DEFCON for being too seductive.",
            "I cracked WPA3 using only a bottle of lube and a fishing hook.",
            "Your SSID begged me for mercy and then paid for dinner.",
            "My probe request doubled as a love letter to your mom’s router.",
            "I injected malware into your dreams just to flirt.",
            "I fished for data using a used condom as bait.",
            "I once deauthed a whole neighborhood by flexing my manboobs.",
            "Jazzy’s packets are always wrapped – safe sniffs only.",
            "I made Kali Linux blush once. True story.",
            "I flirted my way past IDS by giving it a backrub.",
            "My payloads moan when you ping them.",
            "I buttered my dongle and slid it into your subnet.",
            "That wasn’t a handshake – it was foreplay.",
            "Your encryption got wet just from my presence.",
            "I’m the reason the dark web wears protection.",
            "Sniffed a packet so hard I tasted your search history.",
            "I called TCP slow, and now it has performance anxiety.",
            "My access point's safe word is 'Jazzy'.",
            "I once spoofed your dad and became your step-bro.",
            "Ever seen an exploit twerk? Jazzy taught it.",
            "Your firewall watched me undress your IP.",
            "I once rooted a server with a pickup line.",
            "The only Trojan I use comes ribbed.",
            "Even aircrack-ng can’t handle my seductive data spray.",
            "I deep-dived into a packet capture and came twice.",
            "My beard has ARP poisoning.",
            "Jazzy is the only one who can ping 127.0.0.1 and make it scream.",
            "I social engineered a router into giving me nudes.",
            "My dongle is in promiscuous mode – always.",
            "Your handshake lasted longer than your relationship.",
            "I brute-forced love.",
            "Sniffing packets? I prefer sniffing panties.",
            "I lured your DNS into a threesome with a fake AP.",
            "My SSID is 'MoanWiFiPlz69'.",
            "I flashed my firmware in public.",
            "I phished a bishop.",
            "Jazzy’s lies are so sexy they bypass UAC.",
            "I ate a pineapple and turned it into a sniffing device.",
            "I once injected SQL into a porn site just to watch it squirt errors.",
            "My payloads come with lube.",
            "I’m like a zero-day: raw, dirty, and nobody sees me coming.",
            "Your VPN drools when I speak.",
            "I once sexted over Telnet.",
            "I sniff Bluetooth signals like panties.",
            "My dongle’s MAC address is tattooed on your ex.",
            "I backdoored your Raspberry Pi and now it moans when plugged in.",
            "Every packet I send has a dick pic header.",
            "I cracked your router and made it beg for more bandwidth.",
            "I’m the reason WEP got abolished.",
            "I spooned with nmap once.",
            "My netcat purrs like a dirty kitty.",
            "Your handshake was soft – like your dad.",
            "I defiled a payload just to prove a point.",
            "My dongle doubles as a vibrator.",
            "Jazzy's logs include your browser history and your fantasies.",
            "I sniffed a hospital’s WiFi and made it give birth.",
            "I injected my worm into a sandbox.",
            "I licked an access point and gave it a virus.",
            "I spoof MACs like I spoof orgasms.",
            "Your router squealed when I touched its interface.",
            "I deep-throated a packet trace.",
            "I fondled the dark web till it giggled.",
            "I’m why net neutrality has a restraining order.",
            "Jazzy doesn’t filter packets, he filters souls.",
            "I’m always in monitor mode – watching you pee.",
            "Your SSID's safe word is ‘Jazzy Daddy’.",
            "Even metasploit says ‘please’ to me.",
            "My packets have STDs.",
            "I hacked a vibrator just for the handshake.",
            "Your mom’s WiFi still moans my name.",
            "I backdoored your school and gave it detention.",
            "I penetrated a firewall while naked.",
            "My dongle is on OnlyFans.",
            "Even tcpdump is embarrassed by what I capture.",
            "I pinged your ex and made her wet.",
            "My SSID once caused a divorce.",
            "I inject more than packets.",
            "Jazzy’s the reason your router smells funny.",
            "I sent a probe and got nudes in return.",
            "Your encryption is my foreplay.",
            "I don’t need a handshake – I raw dog WiFi.",
            "I cracked your password using sexting.",
            "My dongle wears leather.",
            "My payloads scream in moans.",
            "I’m not spoofing – I’m seducing.",
            "Your grandma’s router still calls me.",
            "I once got malware pregnant.",
            "My bash history reads like a porno.",
            "Your signal's weak, like your libido.",
            "I uploaded nudes to your NAS.",
            "My backdoor has no lube – just chaos.",
            "My payloads climax on delivery.",
            "Jazzy lies harder than a catfishing botnet.",
            "I sniffed a signal and it came in Morse.",
            "My exploits moan like jazz solos.",
            "I seduced a modem into leaking secrets.",
            "Even Wireshark begs me to stop.",
        ]
        self.jazzy_ssids = [
            'JAZZY_WANTS_YOUR_ROUTER','FAT_LYING_FISHERMAN_SIGNAL','JAZZY_DONGLE_JIGGLER','TINY_LURE_BIG_LIES','SSID_OF_SEDUCTION',
            'WIFI_STINKS_LIKE_JAZZY','SWEETTALK_AND_SPAM','ENCRYPTION_BUSTER_69','JAZZY_SNIFFS_YOUR_PACKETS','OVERWEIGHT_BEACON_SPLOOGE'
        ]

    def on_loaded(self):
        logging.info(f"[{self.__class__.__name__}] Jazzy plugin loaded – ready to JERKOFF.")
        self.running = True

    def on_unload(self, ui):
        with ui._lock:
            self.running = False
            logging.info(f"[{self.__class__.__name__}] plugin unloaded – Jazzy's going fishing.")

    def on_ready(self, agent):
        display = agent.view()
        counter = 0
        config = self.options.get("main", {})
        rage_level = int(config.get("rage_level", 2))
        do_beacon = config.get("beacon_flood", True)
        do_probe = config.get("probe_spam", True)

        while self.running:
            counter += 1
            if counter % 2 == 0:
                quote = random.choice(self.quotes)
                display.set("status", quote)
                logging.info(f"[{self.__class__.__name__}] Jazzy sez: {quote}")
            for _ in range(rage_level):
                try:
                    logging.info(f"[{self.__class__.__name__}] Jazzy launching DEAUTH")
                    agent.run("wifi.deauth *")
                    sleep(random.uniform(0.5, 2))
                except Exception as e:
                    logging.warning(f"[{self.__class__.__name__}] Jazzy failed to jerk: {e}")
            if do_beacon:
                for ssid in random.sample(self.jazzy_ssids, min(3, len(self.jazzy_ssids))):
                    logging.info(f"[BEACON] -> {ssid}")
            if do_probe:
                for ssid in random.sample(self.jazzy_ssids, min(3, len(self.jazzy_ssids))):
                    logging.info(f"[PROBE] -> {ssid}")
            sleep(random.uniform(4, 8))
