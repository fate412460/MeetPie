import json
import io

# some filters
frontEnd = ['html','css','javascript','js','vue','react','front','sass','web','bootstrap','ruby','網頁','SEO','fullstack','全端','bootstrap']
backEnd = ['back','rails','fullstack','全端','nodejs','node.js']
imageProcess = ['ps','photoshop','pr','premiere','adobe','圖層','影像','後製','illustrator','krita','攝影']
conf = ['conf','研討會','SITCON','HITCON']
campusAndClub = ['電機','資工','資管','台大','臺大','臺灣大學','台灣大學','開源社','台科大']
software = ['software','engineer','framework','system','web','git','app','tech','資訊','linux','Ubuntu','開源','程式']
programmingLanguage = ['python','ruby','C語言','C++','java','perl','php','swift','程式','C#','julia','lua','golang','javascript']
app = ['ios','swift','android','java','xamarin','web app','webapp']
career = ['22k','實習','silicon']
game = ['rpg','遊戲','game']
dataAndAI = ['google','data','數據','資料','分析','analy','static','人工智慧','機器學習','chatbot']
security = ['hack','駭','黑','逆','碼','封包','HITCON','TDOH']
codingAndDeveloping = ['hackathon','黑客松','開發','coding','develop','studio','workshop','code','git','程式']
system = ['linux','mint','ubuntu','mac','windows']
hardware = ['duino','8051']
social = ['meetup','SOSCET','社群']
network = ['web','互聯網','雲端']

filterArray = [frontEnd, backEnd, imageProcess, conf, campusAndClub, software, programmingLanguage, app, career, game, dataAndAI, security, codingAndDeveloping, system, hardware, social, network]
nameArray = ['前端','後端','影像處理','Conf','校園&社團','軟體','程式語言','app','工作','遊戲','數據分析&AI','資安','開發','作業系統','硬體','社群','網路']

jsonFileOpen = open('../Crawler-Result-JSON-Raw/Crawler-Result-Raw.json','r')
jsonContent = jsonFileOpen.read()
jsonObjects = json.loads(jsonContent)

idf = 0

for jsonObject in jsonObjects:
    jsonObject['type'] = []
    idf = 0
    for eachFilter in filterArray:
        for eachKeyword in eachFilter:
            if eachKeyword.lower() in jsonObject['title'].lower() or eachKeyword.lower() in jsonObject['description'].lower() or eachKeyword.lower() in jsonObject['host'].lower() or eachKeyword.lower() in jsonObject['location'].lower():
                jsonObject['type'].append(nameArray[idf])
                break
        idf+=1

jsonString = json.dumps(jsonObjects,ensure_ascii=False).encode('utf-8')


with io.open('../Crawler-Result-JSON-Tagged/Crawler-Result-Tagged.json', 'w', encoding='utf8') as json_file:
    json.dump( jsonObjects , json_file, ensure_ascii=False)