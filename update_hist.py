# -*- coding: utf-8 -*-
import json, io, datetime

with io.open('history.json', encoding='utf-8') as f:
    h = json.load(f)

cutoff = '2026-08-18'
before = len(h['entries'])
h['entries'] = [e for e in h['entries'] if e.get('date', '') >= cutoff]
print('cleaned:', before, '->', len(h['entries']), '(cutoff', cutoff + ')')

new = [
    {'date': '2026-09-04', 'game': '海贼王 TCG', 'gameId': 'onepiece', 'emoji': '🏴‍☠️',
     'avatarClass': 'op', 'category': 'marketing', 'tag': 'event', 'tagText': '🔥联名',
     'title': 'Nike × One Piece Card Game 联名启动',
     'desc': '通过快闪店 Dr. B\'s RESEARCH LAB 与全球Nike门店分发特典卡，不走卡牌零售渠道；Jump订阅者9/18-10/18可邮购34张完整套装'},
    {'date': '2026-09-12', 'game': '峡谷争锋', 'gameId': 'xgzf', 'emoji': '🏰',
     'avatarClass': 'xg', 'category': 'tournaments', 'tag': 'event', 'tagText': '✅已落幕',
     'title': '2026巡回赛·广州站',
     'desc': '广交会琶洲展馆，512人上限，8/28-9/1报名、9/2抽选公示，解说娇娇/IZORO/书高，新奖品卡云缨，场贩含大乔「绒语心约」牌垫&牌套'},
    {'date': '2026-09-12', 'game': '符文战场', 'gameId': 'rwzc', 'emoji': '⚔️',
     'avatarClass': 'rw', 'category': 'tournaments', 'tag': 'event', 'tagText': '✅已落幕',
     'title': 'CN赛区沈阳站区域公开赛',
     'desc': '9/12-13沈阳新世界博览馆4A馆'},
    {'date': '2026-09-12', 'game': '正面对决 TCG', 'gameId': 'zmdd', 'emoji': '🏯',
     'avatarClass': 'zm', 'category': 'tournaments', 'tag': 'event', 'tagText': '✅已落幕',
     'title': '天津神黄忠主题赛',
     'desc': 'CardTime卡牌店举办'},
    {'date': '2026-09-13', 'game': '超英击战 TCG', 'gameId': 'cyjz', 'emoji': '🦸',
     'avatarClass': 'cy', 'category': 'tournaments', 'tag': 'event', 'tagText': '✅已落幕',
     'title': '黑猫牌垫争霸赛《超英击战》构筑赛',
     'desc': '广州举办'},
    {'date': '2026-09-16', 'game': '宝可梦 PTCG', 'gameId': 'ptcg', 'emoji': '⚡',
     'avatarClass': 'pk', 'category': 'newProducts', 'tag': 'new', 'tagText': '✅已发售',
     'title': '30th Celebration 全球同步首发（史上首次）',
     'desc': '176张全闪卡，6卡/包，每包必出30种皮卡丘之一；Futuristic Rare（YOSHIROTTEN绘Mew ex/Mewtwo ex）+30张Classic Collection经典复刻（含金框Base Set喷火龙）。同日发售幻彩未来纪念礼盒与典藏手办礼盒',
     'url': 'https://www.pokemon.com/us/pokemon-news/get-ready-for-pokemon-tcg-30th-celebration'},
    {'date': '2026-09-17', 'game': '符文战场', 'gameId': 'rwzc', 'emoji': '⚔️',
     'avatarClass': 'rw', 'category': 'newProducts', 'tag': 'alert', 'tagText': '🔥禁卡表',
     'title': '官方发布禁卡表（含「卡牌骗术」）',
     'desc': '为迎接韩文版发售提前发布，游戏总监Dave表示不希望发售后才发布造成心理落差'},
    {'date': '2026-09-17', 'game': '幻兽帕鲁 TCG', 'gameId': 'hspw', 'emoji': '🐉',
     'avatarClass': 'hs', 'category': 'marketing', 'tag': 'event', 'tagText': '🔥TGS',
     'title': 'TGS 2026 东京电玩展开幕',
     'desc': '9/17-21幕张展览馆，23位官方Coser阵容，现场赠捣蛋猫宣传卡/泡澡毛巾/红牛联名贴纸，消费满3000日元送夺魂锯主题宣传卡'},
    {'date': '2026-09-18', 'game': '符文战场', 'gameId': 'rwzc', 'emoji': '⚔️',
     'avatarClass': 'rw', 'category': 'newProducts', 'tag': 'alert', 'tagText': '✅今日发售',
     'title': '韩文版「起源」正式登陆韩国',
     'desc': '第五种官方语言版本。DK的ShowMaker/BeryL拍摄宣传片，T1已建分部并招募LS，GEN商城9/18-22促销+快闪店，韩国首场官方赛9/20资格赛、9/27淘汰赛（GEN GGX，64人，2小时320+人报名）'},
    {'date': '2026-09-18', 'game': '万智牌', 'gameId': 'mtg', 'emoji': '🔮',
     'avatarClass': 'mtg', 'category': 'newProducts', 'tag': 'alert', 'tagText': '🔥今日',
     'title': 'Reality Fracture 全卡表正式上线',
     'desc': '主系列FRA 175张，另含FRC指挥官（14位传奇面指挥官）与SPG Special Guests 10卡。10/2发售、售前9/25-10/1、Arena 9/29',
     'url': 'https://magic.wizards.com/en/news/feature/collecting-reality-fracture'},
]

h['entries'].extend(new)
h['entries'].sort(key=lambda e: e.get('date', ''))
h['updated'] = '2026-09-18T12:40:00+08:00'

with io.open('history.json', 'w', encoding='utf-8') as f:
    json.dump(h, f, ensure_ascii=False, indent=2)
print('history entries:', len(h['entries']), '| range:', h['entries'][0]['date'], '~', h['entries'][-1]['date'])
