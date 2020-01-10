from collections import Counter
import copy

class Deck():
    def __init__(self):
        self.isLandLord = 0 
        self.shangjiaID = 0
        self.xiajiaID = 0
        self.shangjiaNum = 0
        self.xiajiaNum = 0
        self.shangjiaOut = []
        self.shangjiaPaixing = ''
        self.xiajiaOut = []
        self.xiajiaPaixing = ''

class myCard():
    def __init__(self,pai):
        self.SiCards = copy.copy(pai)
        self.MakeCards = copy.copy(pai)
        self.wangzha = 0
        self.zhadan = []
        self.feiji = []
        self.danshun = []
        self.liandui = []
        self.santiao = []
        self.dan = []
        self.dui = []

        self.shoushu=0

typelist=['R','B','2','3','4','5','6','7','8','9','0','J','Q','K','A']
n = ['A','K','Q','J','0','9','8','7','6','5','4','3']
comparelist=['3','4','5','6','7','8','9','0','J','Q','K','A','2','B','R']
nn=['R','B','2','A','K','Q','J','0','9','8','7','6','5','4','3']

def getAllCards(list):   
    cardList=[]
    for i in list:
        cardList.append(i[0])
    #print(cardList)
    return cardList

def classify1 (cards):
    if cards.MakeCards[0]=='R' and cards.MakeCards[1]=='B' :
        cards.wangzha = 1
        del cards.MakeCards[0]
        del cards.MakeCards[0]

    result = Counter(cards.MakeCards).most_common(6)
    for si in result:
        if si[1]==4 :
            cards.zhadan.append(si[0])
            for i in range(4) :
                cards.MakeCards.remove(si[0])
        else:
            break 

    result = Counter(cards.MakeCards).most_common(6)
    triple = []
    for tr in result :
        if (tr[1]==3) :
            triple.append(tr[0])
    i = 0
    j = 0
    while i<len(triple) and j<len(n) :
        if triple[i]==n[j] :
            temp=[]
            temp.append(triple[i])
            while i+1<len(triple) and j+1<len(n) and triple[i+1]==n[j+1] :
                temp.append(triple[i+1])
                i=i+1
                j=j+1
            if len(temp)>1 :
                cards.feiji.append(temp)
                for index in range(len(temp)) :
                    for k in range(3) :
                        cards.MakeCards.remove(temp[index])
            i=i+1
        else :
            j=j+1

def getDanShun(cards):
    #选择五连的单顺,fivedanshun承载顺子队列，j为简化计算的控制变量
    j=2
    fiveDanShun=[]
    while(j<10):
        for i in range(3,11):
            if(i<=j):
                continue
            while((typelist[i] in cards.MakeCards)):
                     if (typelist[i+1] in cards.MakeCards):
                          if (typelist[i+2] in cards.MakeCards) :
                                if (typelist[i+3] in cards.MakeCards) :
                                    if (typelist[i+4] in cards.MakeCards):
                                        fiveDanShun.append(typelist[i:i+5])
                                        cards.MakeCards.remove(typelist[i])
                                        cards.MakeCards.remove(typelist[i+1])
                                        cards.MakeCards.remove(typelist[i+2])
                                        cards.MakeCards.remove(typelist[i+3])
                                        cards.MakeCards.remove(typelist[i+4])
                                    else: 
                                        j=i+4
                                        break
                                else:
                                    j=i+3
                                    break
                          else: 
                              j=i+2
                              break
                     else:
                         j=i+1
                         break
            j=j+1            

    #扩展五连的单顺
    for shunzi in fiveDanShun: 
        if(typelist.index(shunzi[-1])<14):     
            next=typelist.index(shunzi[-1])+1
            while (typelist[next] in cards.MakeCards):
                cards.MakeCards.remove(typelist[next])
                shunzi.append(typelist[next])
                if(next<14):
                    next=next+1
                else:
                    break

    #合并可以合并的顺子
    if(len(fiveDanShun)>=2):
        if(len(fiveDanShun)==2):
            if typelist.index(fiveDanShun[0][-1])==(typelist.index(fiveDanShun[1][0])-1):
                fiveDanShun[0].extend(fiveDanShun[1])
                del fiveDanShun[1]
        else:
            if typelist.index(fiveDanShun[0][-1])==(typelist.index(fiveDanShun[1][0])-1):
                fiveDanShun[0].extend(fiveDanShun[1])
                del fiveDanShun[1]
            elif typelist.index(fiveDanShun[0][-1])==(typelist.index(fiveDanShun[2][0])-1):
                fiveDanShun[0].extend(fiveDanShun[2])
                del fiveDanShun[2]
            elif typelist.index(fiveDanShun[1][-1])==(typelist.index(fiveDanShun[2][0])-1):
                fiveDanShun[1].extend(fiveDanShun[2])
                del fiveDanShun[2]

    cards.danshun=copy.copy(fiveDanShun)
    
def getLianDui(cards):
    #选择三连的连对
    sanLianDui=[]
    j=2
    while(j<12):
        for i in range(3,13):
            if(i<=j):
                continue
            if(cards.MakeCards.count(typelist[i])>=2):
                     if (cards.MakeCards.count(typelist[i+1])>=2):
                          if (cards.MakeCards.count(typelist[i+2])>=2):
                                        sanLianDui.append(typelist[i:i+3])
                                        cards.MakeCards.remove(typelist[i])
                                        cards.MakeCards.remove(typelist[i])
                                        cards.MakeCards.remove(typelist[i+1])
                                        cards.MakeCards.remove(typelist[i+1])
                                        cards.MakeCards.remove(typelist[i+2])
                                        cards.MakeCards.remove(typelist[i+2])
                          else: 
                              j=i+2
                     else:
                         j=i+1
            else:j=i
    #扩展连对
    for liandui in sanLianDui: 
        if(typelist.index(liandui[-1])<14):     
            next=typelist.index(liandui[-1])+1
            while (cards.MakeCards.count(typelist[next])>=2):
                cards.MakeCards.remove(typelist[next])
                cards.MakeCards.remove(typelist[next])
                liandui.append(typelist[next])
                if(next<14):
                    next=next+1
                else:
                    break

    #合并连对
    if(len(sanLianDui)==2):
        if typelist.index(sanLianDui[0][-1])==(typelist.index(sanLianDui[1][0])-1):
                sanLianDui[0].extend(sanLianDui[1])
                del sanLianDui[1]

    cards.liandui=copy.copy(sanLianDui)

def classifySanTiao(cards):
    result = Counter(cards.MakeCards).most_common(6)
    for tr in result :
        if (tr[1]==3) :
            cards.santiao.append(tr[0])
            for k in range(3) :
                cards.MakeCards.remove(tr[0])

def getDuiDan(cards):
    result = Counter(cards.MakeCards).most_common(8)
    for tr in result :
        if (tr[1]==2) :
            cards.dui.append(tr[0])
            for k in range(2) :
                cards.MakeCards.remove(tr[0])
    cards.dan=copy.copy(cards.MakeCards)

def getShouShu(cards):
    number=cards.wangzha+len(cards.zhadan)+len(cards.feiji)+len(cards.danshun)+len(cards.liandui)+len(cards.santiao)
    danDui=len(cards.dui)+len(cards.dan)
    nengDai=0
    for obj in cards.feiji:
        nengDai=nengDai+len(obj)
    nengDai=nengDai+len(cards.santiao)
    if danDui>nengDai :
        number=number+danDui-nengDai
    cards.shoushu=number
        
def judge(alist):
    list=getAllCards(alist)
    cards1 = myCard(list)
    cards2 = myCard(list)
    cards3 = myCard(list)

    classify1(cards1)
    getDanShun(cards1)
    getLianDui(cards1)
    classifySanTiao(cards1)
    getDuiDan(cards1)
    getShouShu(cards1)
 
    classify1(cards2)
    getLianDui(cards2)
    getDanShun(cards2)
    classifySanTiao(cards2)
    getDuiDan(cards2)
    getShouShu(cards2)
    
    classify1(cards3)
    classifySanTiao(cards3)
    getDanShun(cards3)
    getLianDui(cards3)
    getDuiDan(cards3)
    getShouShu(cards3)

    if cards1.shoushu<=cards2.shoushu:
        if cards1.shoushu<=cards3.shoushu :
            return cards1
        else :
            return cards3
    else :
        if cards2.shoushu<=cards3.shoushu :
            return cards2
        else :
            return cards3

def myTurn(cards):
    #飞机、单顺、连对、三条、对、单、炸弹、王炸
    #注意飞机、炸弹、三条、对、单是大的在前，单顺、连对是小的在前
    chuShenMePai=[100,100,100,100,100,100,100,100]
    if(cards.wangzha):
        chuShenMePai[7]=16
    if(len(cards.zhadan)>0):
        chuShenMePai[6]=15
    if(len(cards.feiji)>0):
        chuShenMePai[0]=comparelist.index(cards.feiji[-1][-1])
    if(len(cards.danshun)>0):
        chuShenMePai[1]=comparelist.index(cards.danshun[0][0])
    if(len(cards.liandui)>0):
        chuShenMePai[2]=comparelist.index(cards.liandui[0][0])
    if(len(cards.santiao)>0):
        chuShenMePai[3]=comparelist.index(cards.santiao[-1])
    danDui=len(cards.dui)+len(cards.dan)
    nengDai=0
    for obj in cards.feiji:
        nengDai=nengDai+len(obj)
    nengDai=nengDai+len(cards.santiao)
    if danDui>nengDai :
        danordui=[]
        danordui.extend(cards.dui)
        danordui.extend(cards.dan)
        danordui.sort(key=comparelist.index)
        if(danordui[nengDai] in cards.dan):
            chuShenMePai[5]=comparelist.index(danordui[nengDai])
        else:
            chuShenMePai[4]=comparelist.index(danordui[nengDai])
    #记录好了最小值，开始选择最小的出牌
    paiXing=chuShenMePai.index(min(chuShenMePai))
    chupai=[]
    #出飞机
    if(paiXing==0):
        daiChuQu=len(cards.feiji[-1])
        if(len(cards.dan)>=daiChuQu):
            #既能带单又能带对
            if(len(cards.dui)>=daiChuQu):
                daidan=daidui=0
                for h in range(-1,-daiChuQu,-1):
                    daidan=daidan+comparelist.index(cards.dan[h])
                    daidui=daidui+comparelist.index(cards.dui[h])
                if(daidan<daidui):
                    chupai.extend(cards.dan[-daiChuQu:])
                    for a in range(daiChuQu):
                        cards.dan.pop()
                else:
                    for b in range(daiChuQu):
                        chupai.append(cards.dui[-1])
                        chupai.append(cards.dui[-1])
                        cards.dui.pop()
            #只能带单
            else:
                chupai.extend(cards.dan[-daiChuQu:])
                for c in range(daiChuQu):
                    cards.dan.pop()
        #只能带对
        elif(len(cards.dui)>=daiChuQu):
            for d in range(daiChuQu):
                chupai.append(cards.dui[-1])
                chupai.append(cards.dui[-1])
                cards.dui.pop()
        for e in range(daiChuQu):
            chupai.append(cards.feiji[-1][-1])
            chupai.append(cards.feiji[-1][-1])
            chupai.append(cards.feiji[-1][-1])
            cards.feiji[-1].pop()
        cards.feiji.pop()
    #出单顺
    if(paiXing==1):   
        chupai.extend(cards.danshun[0])
        cards.danshun.pop(0)
    #出连对
    if(paiXing==2):
        for g in range(len(cards.liandui[0])):
            print(g)
            chupai.append(cards.liandui[0][g])
            chupai.append(cards.liandui[0][g])
        cards.liandui.pop(0)
    #出三条
    if(paiXing==3):
        if(len(cards.dan)>0):
            if(len(cards.dui)>0):
                if(comparelist.index(cards.dan[-1])>comparelist.index(cards.dui[-1])):
                    chupai.append(cards.dui[-1])
                    chupai.append(cards.dui[-1])
                    cards.dui.pop()
                else:
                    chupai.append(cards.dan[-1])
                    cards.dan.pop()
            else:
                chupai.append(cards.dan[-1])
                cards.dan.pop()
        elif(len(cards.dui)>0):
            chupai.append(cards.dui[-1])
            chupai.append(cards.dui[-1])
            cards.dui.pop()
        chupai.append(cards.santiao[-1])
        chupai.append(cards.santiao[-1])
        chupai.append(cards.santiao[-1])
        cards.santiao.pop()
    if(paiXing==4):
        chupai.append(cards.dui[-1])
        chupai.append(cards.dui[-1])
        cards.dui.pop()
    if(paiXing==5):
        chupai.append(cards.dan[-1])
        cards.dan.pop()
    if(paiXing==6):
        chupai.append(cards.zhadan[-1])
        chupai.append(cards.zhadan[-1])
        chupai.append(cards.zhadan[-1])
        chupai.append(cards.zhadan[-1])
        cards.zhadan.pop()
    if(paiXing==7):
        chupai.append('R')
        chupai.append('B')
        cards.wangzha=0
    return chupai

def choose(paixing,daxiao,card) :
    print(paixing,daxiao)
    out=[]
    l=len(daxiao)
    if paixing=='zd' :
        if l==2 :
            return out
        for obj in card.zhadan[::-1] :
            if nn.index(obj)<nn.index(daxiao[0]) :
                for k in range(4) :
                    out.append(obj)
                card.zhadan.remove(obj)
                return out
        return out
    elif paixing=='dan' :
        for obj in card.dan[::-1] :
            if nn.index(obj)<nn.index(daxiao[0]) :
                out.append(obj)
                card.dan.remove(obj)
                return out
        for obj in card.dui[::-1] :
            if nn.index(obj)<nn.index(daxiao[0]) :
                out.append(obj)
                card.dui.remove(obj)
                card.dan.append(obj)
                return out
        return out
    elif paixing=='dui' :
        for obj in card.dui[::-1] :
            if nn.index(obj)<nn.index(daxiao[0]) :
                out.append(obj)
                out.append(obj)
                card.dui.remove(obj)
                return out
        return out
    elif paixing=='san' :
        for obj in card.santiao[::-1] :
            if nn.index(obj)<nn.index(daxiao[0]) :
                out.append(obj)
                out.append(obj)
                out.append(obj)
                card.santiao.remove(obj)
                return out
        return out
    elif paixing=='sz' :
        for obj in card.danshun :
            if len(obj)-l==0 and nn.index(obj[0])<nn.index(daxiao[l-1]):
                for g in obj:
                    out.append(g)
                card.danshun.remove(obj)
                return out
        return out
    elif paixing=='ld' :
        for obj in card.liandui :
            if len(obj)-l/2==0 and nn.index(obj[0])<nn.index(daxiao[l-1]):
                for g in obj:
                    out.append(g)
                    out.append(g)
                card.liandui.remove(obj)
                return out
        return out
    elif paixing=='sdy' :
        if len(card.dan)!=0 :
            result = Counter(daxiao).most_common(2)
            for obj in card.santiao[::-1] :
                if nn.index(obj)<nn.index(result[0][0]):
                    out.append(obj)
                    out.append(obj)
                    out.append(obj)
                    out.append(card.dan[len(card.dan)-1])
                    card.santiao.remove(obj)
                    del card.dan[len(card.dan)-1]
                    return out
        return out
    elif paixing=='sdd' :
        if len(card.dui)!=0 :
            result = Counter(daxiao).most_common(2)
            for obj in card.santiao[::-1] :
                if nn.index(obj)<nn.index(result[0][0]):
                    out.append(obj)
                    out.append(obj)
                    out.append(obj)
                    out.append(card.dui[len(card.dui)-1])
                    out.append(card.dui[len(card.dui)-1])
                    card.santiao.remove(obj)
                    del card.dui[len(card.dui)-1]
                    return out
        return out
    elif paixing=='fj' :
        result = Counter(daxiao).most_common(6)
        if l==6 :
            for obj in card.feiji :
                if len(obj)==2 and nn.index(obj[0])<nn.index(result[0][0]) :
                    for k in range(3):
                        out.append(obj[0])
                        out.append(obj[1])
                    card.feiji.remove(obj)
                    return out
        elif l==9 :
            for obj in card.feiji :
                if len(obj)==3 and nn.index(obj[0])<nn.index(result[0][0]) :
                    for k in range(3):
                        out.append(obj[0])
                        out.append(obj[1])
                        out.append(obj[2])
                    card.feiji.remove(obj)
                    return out
        elif l==8 :
            if len(card.dan)>1 :
                for obj in card.feiji :
                    if len(obj)==2 and nn.index(obj[0])<nn.index(result[0][0]) :
                        for k in range(3):
                            out.append(obj[0])
                            out.append(obj[1])
                        out.append(card.dan[len(card.dan)-1])
                        out.append(card.dan[len(card.dan)-2])
                        card.feiji.remove(obj)
                        del card.dan[len(card.dan)-1]
                        del card.dan[len(card.dan)-2]
                        return out
        elif l==10 :
            if len(card.dui)>1 :
                for obj in card.feiji :
                    if len(obj)==2 and nn.index(obj[0])<nn.index(result[0][0]) :
                        for k in range(3):
                            out.append(obj[0])
                            out.append(obj[1])
                        out.append(card.dui[len(card.dui)-1])
                        out.append(card.dui[len(card.dui)-1])
                        out.append(card.dui[len(card.dui)-2])
                        out.append(card.dui[len(card.dui)-2])
                        card.feiji.remove(obj)
                        del card.dui[len(card.dui)-1]
                        del card.dui[len(card.dui)-2]
                        return out
        elif l==12 :
            if len(card.dan)>2 :
                for obj in card.feiji :
                    if len(obj)==3 and nn.index(obj[0])<nn.index(result[0][0]) :
                        for k in range(3):
                            out.append(obj[0])
                            out.append(obj[1])
                            out.append(obj[2])
                        out.append(card.dan[len(card.dan)-1])
                        out.append(card.dan[len(card.dan)-2])
                        out.append(card.dan[len(card.dan)-3])
                        card.feiji.remove(obj)
                        del card.dan[len(card.dan)-1]
                        del card.dan[len(card.dan)-2]
                        del card.dan[len(card.dan)-3]
                        return out
        elif l==15 :
            if len(card.dui)>2 :
                for obj in card.feiji :
                    if len(obj)==3 and nn.index(obj[0])<nn.index(result[0][0]) :
                        for k in range(3):
                            out.append(obj[0])
                            out.append(obj[1])
                            out.append(obj[2])
                        out.append(card.dui[len(card.dui)-1])
                        out.append(card.dui[len(card.dui)-1])
                        out.append(card.dui[len(card.dui)-2])
                        out.append(card.dui[len(card.dui)-2])
                        out.append(card.dui[len(card.dui)-3])
                        out.append(card.dui[len(card.dui)-3])
                        card.feiji.remove(obj)
                        del card.dui[len(card.dui)-1]
                        del card.dui[len(card.dui)-2]
                        del card.dui[len(card.dui)-3]
                        return out
    else :
        return out       

def ifPass(paixing,daxiao,card) :
    out=[]
    if paixing=='dan' :
        if nn.index('0')<nn.index(daxiao[0]):
            for obj in card.dan[::-1] :
                if n.index(obj)<nn.index(daxiao[0]) and nn.index('0')<=n.index(obj):
                    out.append(obj)
                    return False,out
        return True,out
    elif paixing=='dui' :
        if nn.index('0')<nn.index(daxiao[0]):
            for obj in card.dui[::-1] :
                if nn.index(obj)<nn.index(daxiao[0]) and nn.index('0')<=nn.index(obj):
                    out.append(obj)
                    out.append(obj)
                    return False,out
        return True,out
    else :
        return True,out

def yaSi(card,deck):
    if len(deck.shangjiaOut)==0 :
        paixing=deck.xiajiaPaixing
        daxiao=deck.xiajiaOut
    else :
        paixing=deck.shangjiaPaixing
        daxiao=deck.shangjiaOut
    if deck.isLandLord==1 :
        list=choose(paixing,daxiao,card)
    else :
        if deck.shangjiaID==1 :
    
            list=choose(paixing,daxiao,card)
        else :
            flag,out=ifPass(paixing,daxiao,card)
            if flag or deck.shangjiaNum<10 :
                list=[]
            else :
                list=copy.copy(out)
    return list

def main():
    list = ['B','2','2','2','A','K','Q','J','0','0','0','9','8','8','7','6','6','4'] 
    cards=judge(list)
    print(cards.wangzha,cards.zhadan,cards.feiji,cards.danshun,cards.liandui,cards.santiao,cards.dui,cards.dan)
    print(cards.shoushu)
    deck=Deck()
    deck.shangjiaID=1
    deck.shangjiaNum=11
    deck.shangjiaPaixing='dan'
    deck.shangjiaOut=['K']
    print(yaSi(cards,deck))

main()
