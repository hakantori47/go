import requests
import re
from datetime import datetime

m3u_content = "#EXTM3U\n"
updated_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
m3u_content += f"# Last Updated: {updated_time}\n"

base = "https://trgoals"
domain = ""

for i in range(1485, 2101):
    test_domain = f"{base}{i}.xyz"
    try:
        response = requests.head(test_domain, timeout=3)
        if response.status_code == 200:
            domain = test_domain
            print(f"Active domain found: {domain}")
            break
    except:
        continue

if not domain:
    print("No active domain found")
    exit()

channel_ids = {
    "yayinzirve":"BEINSPORTS1 HD","yayininat":"BEINSPORTS1 HD","yayin1":"BEINSPORTS1 HD",
    "yayinb2":"BEINSPORTS2 HD","yayinb3":"BEINSPORTS3 HD","yayinb4":"BEINSPORTS4 HD",
    "yayinb5":"BEINSPORTS5 HD","yayinbm1":"BEINSPORTS1 MAX HD","yayinbm2":"BEINSPORTS2 MAX HD",
    "yayinss":"SARANSPORTS1 HD","yayinss2":"SARANSPORTS2 HD","yayint1":"TIVIBUSPORTS1 HD",
    "yayint2":"TIVIBUSPORTS2 HD","yayint3":"TIVIBUSPORTS3 HD","yayint4":"TIVIBUSPORTS4 HD",
    "yayinsmarts":"SMARTSPORTS HD","yayinsms2":"SMARTSPORTS2 HD","yayintrtspor":"TRTSPOR HD",
    "yayintrtspor2":"TRTSPOR2 HD","yayinas":"ASPOR HD","yayinatv":"ATV HD",
    "yayintv8":"TV8 HD","yayintv85":"TV85 HD","yayinnbatv":"NBATV HD",
    "yayinex1":"TABII1 HD","yayinex2":"TABII2 HD","yayinex3":"TABII3 HD",
    "yayinex4":"TABII4 HD","yayinex5":"TABII5 HD","yayinex6":"TABII6 HD",
    "yayinex7":"TABII7 HD","yayinex8":"TABII8 HD"
}

success_count = 0
for channel_id, channel_name in channel_ids.items():
    try:
        channel_url = f"{domain}/channel.html?id={channel_id}"
        r = requests.get(channel_url, headers={"User-Agent":"Mozilla/5.0"}, timeout=10)
        match = re.search(r'const baseurl = "(.*?)"', r.text)
        if match:
            baseurl = match.group(1)
            full_url = f"{baseurl}{channel_id}.m3u8"
            m3u_content += f'#EXTINF:-1 tvg-id="" tvg-name="{channel_name}" tvg-logo="https://i.hizliresim.com/b6xqz10.jpg" group-title="DeaTHLesS-Goals",{channel_name}\n'
            m3u_content += f'#EXTVLCOPT:http-referer={domain}/\n'
            m3u_content += f'{full_url}\n'
            success_count += 1
            print(f"✓ {channel_name} added")
        else:
            print(f"✗ {channel_name}: URL not found")
    except Exception as e:
        print(f"✗ {channel_name}: Error - {str(e)}")
        continue

with open("DeaTHLesS-Goals.m3u", "w", encoding="utf-8") as f:
    f.write(m3u_content)

print(f"\nFile saved: DeaTHLesS-Goals.m3u")
print(f"Total channels added: {success_count}/{len(channel_ids)}")
print(f"Updated: {updated_time}")