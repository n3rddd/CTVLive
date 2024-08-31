ip_version_priority = "ipv4"

source_urls = [
    "https://raw.githubusercontent.com/redrainl/iptv/main/speedtest/zubo_fofa.txt", #ADDED BY LEM ON 01/08/2024
    "https://raw.githubusercontent.com/pxiptv/live/main/iptv.txt", #ADDED BY LEM ON 08/08/2024
    "http://tv.850930.xyz/kdsb.m3u", #ADDED BY LEM ON 29/07/2024
    "http://tv.850930.xyz/kdsb2.m3u", #ADDED BY LEM ON 31/07/2024
    "http://tv.850930.xyz/kdsb3.m3u", #ADDED BY LEM ON 27/08/2024
    "http://tv.850930.xyz/gather.m3u", #ADDED BY LEM ON 29/07/2024
    "https://tv543.cc/nb.txt", #ADDED BY LEM ON 26/08/2024
    "https://raw.githubusercontent.com/hus888yu/app/main/111.m3u", #ADDED BY LEM ON 06/08/2024
    "https://raw.githubusercontent.com/hus888yu/app/main/543.m3u", #ADDED BY LEM ON 13/08/2024
    "https://guot55.serv00.net/zb.php", #ADDED BY LEM ON 31/08/2024
    "https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt",
    "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt", #ADDED BY LEM ON 29/07/2024
    "http://ttkx.live:55/lib/kx2024.txt", #ADDED BY LEM ON 29/07/2024
    "https://raw.githubusercontent.com/Love4vn/love4vn/main/Sport.m3u", #奥运 ON 29/07/2024
    "https://gitlab.com/tvkj/qxitv/-/raw/main/888.txt" #ADDED BY LEM ON 29/07/2024
]

url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn"
]

announcements = [
    {
        "channel": "🤠雷蒙影视直播",
        "entries": [
            {"name":"雷蒙影视直播","url":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/CTVThemeSong1.mp4","logo":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/ICON1.png"},
            {"name":"CrimeTV LIVE","url":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/CTVThemeSong2.mp4","logo":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/ICON2.png"},
            {"name":"更新日期","url":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/CRIMETVPV1.mkv","logo":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/ICON3.png"},
            {"name":None,"url":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/CRIMETVPV2.mkv","logo":"https://cors.isteed.cc/https://raw.githubusercontent.com/n3rddd/N3RD/master/JN/N3RD/W/ICON4.png"}
        ]
    }
]

epg_urls = [
    "https://live.fanmingming.com/e.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "http://epg.aptvapp.com/xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
