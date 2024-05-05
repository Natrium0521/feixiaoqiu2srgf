import json
import requests

uid = 0
req = requests.get(f"https://feixiaoqiu.com/query_xt_record/?uid={uid}").json()
srgf = {
    "info": {
        "srgf_version": "v1.0",
        "uid": str(uid),
        "lang": "zh-cn",
        "region_time_zone": 8,
        "export_timestamp": 0,
        "export_app": "feixiaoqiu2srgf",
        "export_app_version": "v1.0",
    },
    "list": [],
}
if req["result"] == "OK":
    rec = req["record"]
    items = rec.split("#")
    for item in items:
        vals = item.split("_")
        tmp = {
            "gacha_id": vals[-1],
            "gacha_type": vals[0],
            "item_id": vals[4],
            "time": vals[5],
            "id": vals[6],
            "count": "1",
            "name": vals[2],
            "item_type": "角色" if vals[1] == "1" else "光锥",
            "rank_type": vals[3],
        }
        srgf["list"].append(tmp)
    with open("./out.json", "w", encoding="utf-8") as f:
        json.dump(srgf, f, indent=4, ensure_ascii=False)
