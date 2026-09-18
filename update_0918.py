# -*- coding: utf-8 -*-
import json, io

with io.open('data.json', encoding='utf-8') as f:
    d = json.load(f)

G = {g['id']: g for g in d['games']}

# ============ meta ============
d['meta']['updated'] = '2026-09-18T12:40:00+08:00'
d['meta']['totalGames'] = 14
d['meta']['alertBanner'] = (
    '⚠️ 重要预警（9/18巡查）：'
    '🔴符文战场韩文版<strong style="color:#dc2626">今日9/18正式登陆韩国！</strong>'
    '🔴万智牌Reality Fracture<strong style="color:#dc2626">全卡表今日9/18上线！</strong>'
    '🔴PTCG 30周年庆典<strong style="color:#dc2626">9/16已全球同步首发！</strong>'
    '🔴幻兽帕鲁TGS 2026<strong style="color:#dc2626">9/17-21幕张进行中！</strong>'
    '🔴<strong style="color:#dc2626">新TCG发现：Cyberpunk TCG 11/6零售发售！</strong>'
    '🔴符文战场9/17发布禁卡表·韩国首赛9/20 GEN GGX开打！'
    '🔴海贼王×Nike联名特典卡全球分发中！'
)

def find(gid, cat, key):
    for i, it in enumerate(G[gid]['tabs'][cat]):
        if key in it.get('title', ''):
            return i
    return -1

def rm(gid, cat, key):
    i = find(gid, cat, key)
    if i >= 0:
        G[gid]['tabs'][cat].pop(i)

# ============ PTCG ============
p = G['ptcg']
p['statusText'] = '30周年9/16已全球同步首发·后续4波铺货至12/4'
i = find('ptcg', 'newProducts', '30th Celebration 扩展包')
if i >= 0:
    p['tabs']['newProducts'][i].update({
        'tag': 'new', 'tagText': '✅已发售',
        'title': '30th Celebration 扩展包（9/16全球同步首发）',
        'desc': '9/16已全球同步发售！史上首次全球同日首发，176张全闪卡（含基本能量），6卡/包，每包必出1张30种皮卡丘之一。Futuristic Rare新稀有度（YOSHIROTTEN绘Mew ex/Mewtwo ex）+30张Classic Collection经典复刻（含金框1998 Base Set喷火龙，保留原卡号，仅30周年皮卡丘印章区分，Standard不可用）'
    })
for key in ['幻彩未来纪念礼盒', '典藏手办礼盒']:
    i = find('ptcg', 'newProducts', key)
    if i >= 0:
        p['tabs']['newProducts'][i]['tagText'] = '✅已发售'
        p['tabs']['newProducts'][i]['tag'] = 'new'
p['tabs']['sentiment'].insert(0, {
    'tag': 'hot', 'tagText': '🔥市场',
    'title': '经典复刻喷火龙二级市场约$175·远低于原版',
    'desc': '30周年Classic Collection复刻的Base Set喷火龙裸卡二级市场约US$175，明显低于同品相原版，定位为"可开可玩"而非与vintage竞争。全闪卡出包即易磨损，收藏需注意品相',
    'date': '2026-09-16起'
})

# ============ 符文战场 ============
r = G['rwzc']
r['statusText'] = '韩文版今日9/18发售·9/17禁卡表·韩国首赛9/20'
i = find('rwzc', 'newProducts', '9/18 正式登陆韩国')
if i >= 0:
    r['tabs']['newProducts'][i].update({
        'tag': 'alert', 'tagText': '✅今日发售',
        'title': '符文战场韩文版「起源」9/18今日正式登陆韩国',
        'desc': '9/18今日发售！第五种官方语言版本。拳头以最高规格运营：DK的ShowMaker/BeryL拍摄宣传片+教学对战视频，T1早已建立分部并招募LS，GEN俱乐部9/17宣布官方商城直售+快闪店（预约已满）'
    })
rm('rwzc', 'newProducts', '韩文版第一系列')
r['tabs']['newProducts'].insert(0, {
    'tag': 'alert', 'tagText': '🔥禁卡表',
    'title': '9/17 官方发布禁卡表（含「卡牌骗术」）',
    'desc': '游戏总监Dave解释：不希望韩文版发售后才发禁卡表造成心理落差，因此提前于9/17发布，其中「卡牌骗术」来自第一系列',
    'date': '2026-09-17'
})
r['tabs']['newProducts'].insert(0, {
    'tag': 'event', 'tagText': '🔥韩国',
    'title': 'GEN商城促销活动（9/18-22）+ 韩国首场官方赛',
    'desc': '9/18-22在GEN商城或门店购买即获抽奖券，每日抽奖：GEN选手签名特别卡×5、起源系列肥包×1（Kiin瑟提/Canyon李青/Chovy阿狸亚索/Ruler卡莎/Duro蕾欧娜）。韩国首场官方赛落地GEN场馆GGX：9/20资格赛、9/27淘汰赛，免费报名限64人，GEN官方频道直播，开放2小时即320+人报名',
    'date': '2026-09-18~27'
})
for key in ['沈阳站（9/12-13', '沈阳站区域公开赛']:
    i = find('rwzc', 'tournaments', key)
    if i >= 0:
        r['tabs']['tournaments'][i].update({'tag': 'event', 'tagText': '✅已落幕'})
        r['tabs']['tournaments'][i]['title'] = r['tabs']['tournaments'][i]['title'].replace('🔥倒计时3天 ', '').replace('🔥明日 ', '')
# 去重：删除重复沈阳站条目
seen, keep = set(), []
for it in r['tabs']['tournaments']:
    k = it['title'].replace('✅已落幕 ', '')
    if '沈阳' in k and '沈阳' in seen:
        continue
    if '沈阳' in k:
        seen.add('沈阳')
    keep.append(it)
r['tabs']['tournaments'] = keep

# ============ 峡谷争锋 ============
x = G['xgzf']
x['statusText'] = '大奖赛千人60万奖金创国产之最·广州站9/12已收官'
i = find('xgzf', 'tournaments', '大奖赛·上海')
if i >= 0:
    x['tabs']['tournaments'][i]['desc'] = '上海杨行镇国际元数创港落幕！卡游主办，全国各地上千名选手参赛，创国产原创TCG赛事规模之最。总奖金60万元，首日瑞士轮选出8强，次日八强用两套无重复英雄卡组决胜，最终「御三家.鱼」夺得2026大奖赛总冠军。排名前列另获赛事限定珍贵奖品卡'
for it in x['tabs']['tournaments']:
    if '广州巡回赛' in it['title']:
        it.update({'tag': 'event', 'tagText': '✅已落幕'})
        it['title'] = it['title'].replace('🔥倒计时3天 ', '').replace('🔥明日 ', '')
seen, keep = set(), []
for it in x['tabs']['tournaments']:
    if '广州巡回赛' in it['title']:
        if 'gz' in seen:
            continue
        seen.add('gz')
    keep.append(it)
x['tabs']['tournaments'] = keep

# ============ 幻兽帕鲁 ============
h = G['hspw']
h['statusText'] = 'TGS 9/17-21进行中·第2弹10/30·金猫怪$10,350'
i = find('hspw', 'marketing', 'TGS 2026 幕张参展')
if i >= 0:
    h['tabs']['marketing'][i]['desc'] = '9/17-21幕张展览馆进行中！官方集结23位Coser阵容（天海濑奈/纯米绫乃/莱姆塔索饰露蒂米尔，火将Rosiel/猫乃心/桃里丽亚饰佐伊），舞台定期举办Cosplay互动秀。现场赠品：捣蛋猫宣传卡、帕鲁1.0限定T恤、捣蛋猫泡澡毛巾、红牛联名贴纸；消费满3000日元送捣蛋猫夺魂锯主题宣传卡，买TCG扩充满20000日元前100名送专属大型购物袋。4-6号厅南侧户外美食区设帕鲁专属餐车'

# ============ 正面对决 ============
z = G['zmdd']
z['statusText'] = '季度大奖赛《出征》进行中·天津神黄忠赛9/12已落幕'
for it in z['tabs']['tournaments']:
    if '神黄忠' in it['title']:
        it.update({'tag': 'event', 'tagText': '✅已落幕'})
        it['title'] = it['title'].replace('🔥店赛 ', '').replace('🔥明日 ', '')
seen, keep = set(), []
for it in z['tabs']['tournaments']:
    if '神黄忠' in it['title']:
        if 'tj' in seen:
            continue
        seen.add('tj')
    keep.append(it)
z['tabs']['tournaments'] = keep

# ============ 超英击战 ============
c = G['cyjz']
c['statusText'] = '泰国曼谷首赛2小时售罄·9-12月每月公开赛'
c['tabs']['newProducts'].insert(0, {
    'tag': 'hot', 'tagText': '🔥出海',
    'title': '泰国曼谷官方首赛·开售2小时全线售罄',
    'desc': '8/16杰森娱乐×泰国头部经销商Kidz&Kitz在The Mall Lifestore Bangkapi举办泰国首赛，产品开售2小时即售罄！以金/银/铜卡构建专属赛制覆盖不同玩家圈层。已布局：中国（广东/北京/长沙）、中国香港动漫电玩节、印尼雅加达（印尼文版发布会）、新加坡、泰国曼谷。董事长林俊亲赴一线，并在长沙录制《超英击战·飞玩不可》国民团综',
    'date': '2026-08-16'
})
for it in c['tabs']['tournaments']:
    if '黑猫牌垫争霸赛' in it['title']:
        it.update({'tag': 'event', 'tagText': '✅已落幕'})
        it['title'] = it['title'].replace('🔥倒计时4天 ', '')

# ============ 海贼王 ============
o = G['onepiece']
o['tabs']['newProducts'].insert(0, {
    'tag': 'upcoming', 'tagText': '新品',
    'title': 'One Piece Heroines Special Set（9月下旬）',
    'desc': '9月下旬发售，$70定价，Premium Bandai直售（美国/澳洲/新西兰，不走一般零售）。围绕女性角色主题，含宣传卡+DON!!宣传卡+卡套+卡垫+收纳盒',
    'date': '2026-09下旬'
})
o['tabs']['marketing'].insert(0, {
    'tag': 'event', 'tagText': '🔥联名',
    'title': 'Nike × One Piece Card Game 联名特典卡',
    'desc': '9/4启动！通过快闪店「Dr. B\'s RESEARCH LAB」与全球Nike门店分发特典卡，完全不走卡牌零售渠道；英文版卡通过各地区赛事奖池发放。周刊少年Jump订阅者另有邮购窗口：9/18-10/18可申请34张完整套装（DON!!+蒙奇·D·路飞宣传卡），每人限一套',
    'date': '2026-09-04起'
})
o['tabs']['sentiment'].insert(0, {
    'tag': 'news', 'tagText': '环境',
    'title': 'OP-17环境meta：绿鹰眼65%胜率领跑',
    'desc': '9月OP-17环境S级领袖：Green Dracule Mihawk 65.0%胜率、Purple/Yellow Nico Robin 53.3%、Blue Rocks D. Xebec 53.2%、Red/Black Sabo 52.0%、Purple Kaido 50.3%、Black Monkey.D.Luffy 50.1%。日版原盒约$144（9/7）',
    'date': '2026-09'
})

# ============ 万智牌 ============
m = G['mtg']
m['statusText'] = 'Reality Fracture全卡表今日上线·售前9/25·10/2发售'
m['tabs']['newProducts'].insert(0, {
    'tag': 'alert', 'tagText': '🔥今日',
    'title': 'Reality Fracture 全卡表 9/18 正式上线',
    'desc': '今日(9/18)完整卡图库上线！主系列FRA共175张，另有FRC指挥官产品（14位传奇面指挥官）与SPG Special Guests 10卡全景。核心：Jace化身Theorist建造Echoverse，新机制Empower Jace（鹏洛客衍生物）、Echoed Pairs（每包3传奇含2张成对镜像）、Shattered Mirror 13张、无框Echoed Pairs 30张。Serialized Bloodline Recollector 仅500张（ Collector Booster限定）。售价 Play Booster $5.49 / Collector $26.99 / Bundle $57.99',
    'date': '2026-09-18'
})

# ============ 火影 ============
n = G['hyrz']
i = find('hyrz', 'newProducts', 'Set 3 Akatsuki 11/7预发售')
if i >= 0:
    n['tabs']['newProducts'][i]['desc'] += '。⚠️注意：官方narutotcgmythos.com美国页最新显示Set 3预发售与正式发售均为2027年，与11/13说法存在冲突，建议以官网后续公告为准'

# ============ 新增 Cyberpunk TCG ============
d['games'].append({
    'id': 'cyberpunk',
    'name': 'Cyberpunk TCG',
    'emoji': '🌆',
    'avatarClass': 'cp',
    'status': 'upcoming',
    'statusText': 'Kickstarter史上最高众筹TCG·11/6零售发售',
    'tabs': {
        'newProducts': [
            {'tag': 'alert', 'tagText': '🔥全新TCG',
             'title': 'Cyberpunk TCG: Welcome to Night City（11/6零售发售）',
             'desc': 'WeirdCo×CD PROJEKT RED官方实体TCG！Kickstarter众筹$28,353,088 / 50,773名支持者，创TCG品类众筹历史最高纪录（5分钟即达成目标）。时间线：9/1 Kickstarter履约→9/10-17 Beta Events→10/30零售预发售周末→11/6全零售发售。补充盒24包/盒、12卡/包（7普+3 uncommon+2 rare+，每盒48张rare+）',
             'date': '2026-11-06'},
            {'tag': 'new', 'tagText': '新品',
             'title': '起始牌组 ST01 The Heist / ST02 Embracing Power',
             'desc': '两款40张即开即玩起始牌组（含6枚骰子）。ST02 Embracing Power以荒坂帝国为主题，收录荒坂三郎/赖宣/竹村五郎。英国定价£29.95，补充盒£109.95',
             'date': '2026-11-06'},
            {'tag': 'upcoming', 'tagText': '预告',
             'title': 'Set 2 将引入《Cyberpunk: Edgerunners》',
             'desc': '首弹聚焦《赛博朋克2077》角色与地点，Set 2预计完整引入《Cyberpunk: Edgerunners》内容',
             'date': '2027'}
        ],
        'sentiment': [
            {'tag': 'alert', 'tagText': '🔥纪录',
             'title': 'Kickstarter史上众筹金额最高的TCG',
             'desc': '最终筹得$28,353,088，50,773名支持者，项目开放5分钟即达成初始目标。因众筹规模空前，WeirdCo专程赴上海选定印刷伙伴以满足产能与特殊闪卡工艺需求',
             'date': '2026'},
            {'tag': 'hot', 'tagText': '🔥机制',
             'title': '稀有度体系与核心玩法',
             'desc': '稀有度：Common / Rare / Epic Rare / Secret Rare / Iconic Rare（主追卡，另类插画）；Nova Rare为推广限定（已公布Lucy/Rebecca/Adam Smasher，通过众筹、展会、联名发放）。玩法：围绕3张Legend组建小队，部署Units/Gear/Programs，Eddies为资源，6枚Gig骰驱动，以控制Night City多数Gigs取胜',
             'date': '2026'},
            {'tag': 'news', 'tagText': '评测',
             'title': 'Anime Expo 2026最大规模展位·媒体好评',
             'desc': '与CD PROJEKT RED联合设展，周末预计2000+玩家试玩。Kotaku提前试玩后评价积极，认为其具备长线生命力',
             'date': '2026-07'}
        ],
        'marketing': [
            {'tag': 'event', 'tagText': '🔥周边',
             'title': 'Adam Smasher / Rebecca 高端配件捆绑预售',
             'desc': 'CD PROJEKT RED Gear Store限时预售：Nova Rare双联画卡、6枚亚克力骰、氯丁橡胶卡垫、卡盒',
             'date': '2026-08'},
            {'tag': 'event', 'tagText': '展会',
             'title': '全球展会巡回试玩',
             'desc': 'Anime Expo→巴黎→Gen Con Indianapolis(7/30-8/2)，持续公布新卡与OP宣传卡情报（已预告 Adam Smasher — Metal Over Meat 等）',
             'date': '2026'}
        ],
        'offline': [
            {'tag': 'event', 'tagText': 'Beta赛',
             'title': 'Beta Events（9/10-17）',
             'desc': '零售版发售前的官方店内Beta赛事，使用Beta补充包（与零售版补充包为不同版本，赛事特典卡亦不同）',
             'date': '2026-09-10~17'}
        ],
        'tournaments': [
            {'tag': 'event', 'tagText': '预发售',
             'title': 'Retail Prerelease Weekend（10/30）',
             'desc': '全球本地牌店零售预发售周末，使用零售补充包，赛事套件特典与Beta赛不同',
             'date': '2026-10-30'}
        ]
    }
})

with io.open('data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('data.json updated. games:', len(d['games']))
