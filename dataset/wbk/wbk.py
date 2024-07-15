sourceUrl='http://trans.mglip.com/EnglishC2T.aspx'
# Find all <span> tags in the BeautifulSoup object

from selenium import webdriver

driver = webdriver.Chrome()
driver.get(sourceUrl)

num = 100
labels = []
with open('mon_wiki.txt', 'r') as src:
    for w in src:
        labels.append(w)
#print(labels)
output = []
f = open('MN_WIKI1.txt', 'w')
for i in range(0, 50000, 50):
    qqq = ''
    for j in range(i, min(i + 50, len(labels)), 1):
        qqq += labels[j]
    search = driver.find_element("id", "inputCyrillic_ID")
    search.clear()
    search.send_keys(qqq)
    search.submit()
    button = driver.find_element("id", "ButtonTran_ID")
    button.click()
    getting = driver.find_element("id", "outPutTraditonalM_ID")
    orig = qqq.split('\n')
    nw = getting.text.split('\n')
    for j in range(len(nw)):
        f.write(orig[j] + '|' + nw[j]+'\n')

f.close()
