from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pyautogui


servico = Service(ChromeDriverManager().install())  

browser = webdriver.Chrome(service=servico)
browser.set_window_size(1366, 768)
browser.maximize_window()
browser.get('https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzRhNTdhYTQyLTJkMmQtNGVmNy1hY2Y5LTkyZjc3OTU2M2JlZg')
time.sleep(6)
browser.find_element('xpath', '//*[@id="ember412"]').click()
pyautogui.write('Brasilseg')
time.sleep(2)
pyautogui.press('enter')
time.sleep(1.5)
browser.find_element('xpath', '//*[@id="ember597"]/div/a/img').click()
time.sleep(4.5)
#pyautogui.write("bandrezzo@brasilseg.com.br")
#time.sleep(0.8)
#pyautogui.press('enter')
#time.sleep(2.5)
#pyautogui.write("Valve201020132022!")
#time.sleep(0.5)
#pyautogui.press('enter')
#time.sleep(1)
#browser.find_element('xpath', '//*[@id="idBtn_Back"]').click()
time.sleep(6)
pyautogui.press('esc')
time.sleep(35)
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('C:\\Users\\bandrezzo\\Desktop\\Checklist_v5_Calculo_Metrica.xlsx')
time.sleep(2.5)
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('alt', 'tab')
time.sleep(1.5)
pyautogui.doubleClick(x=737, y=296)
pyautogui.press('pagedown')
time.sleep(2)
#time.sleep(1)
#pyautogui.scroll(-1)
#pyautogui.keyUp('ctrl')
browser.execute_script("document.body.style.zoom='50%'")
time.sleep(2)
pyautogui.keyDown('ctrl')
time.sleep(0.7)
pyautogui.hotkey('shift', 'i')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(3)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.click(x=296, y=348)
time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
new_url_edge2 = 'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzNhZTM5YTgyLWM0YjItNDFkMC04YTRmLTZmY2I5OTE3ZDM1MQ'
browser.get(new_url_edge2)
time.sleep(8)
pyautogui.click(x=419, y=263)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.keyDown('ctrl')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(0.5)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
new_url_edge3 = 'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzYwYzljNzBjLWFkYzgtNGQ1OC05Yjk3LWZmMTlmMmYyNDlhMw'
browser.get(new_url_edge3)
time.sleep(10)
pyautogui.click(x=419, y=263)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.keyDown('ctrl')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(0.5)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('alt', 'tab')
new_url_edge4 = 'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzEwNTE0YzlhLWJlYTMtNGEyZC05ZmIzLWI2ZDE5N2ExOWFmNw'
browser.get(new_url_edge4)
time.sleep(10)
pyautogui.click(x=419, y=263)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.keyDown('ctrl')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(0.5)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('alt', 'tab')
new_url_edge5 = 'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzL2FiY2RiZTIxLTU5ZmItNDI1Yy04NmU4LWEzOTcyYmQyY2QxNA'
browser.get(new_url_edge5)
time.sleep(10)
pyautogui.click(x=419, y=263)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.keyDown('ctrl')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(0.5)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('alt', 'tab')
new_url_edge6 = 'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzkxMTc2YTI0LTJiM2YtNDhhNi1iZDIxLTk0Mjc0ODU2MDEyYw'
browser.get(new_url_edge6)
time.sleep(10)
pyautogui.click(x=419, y=263)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.keyDown('ctrl')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(0.5)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('alt', 'tab')
new_url_edge7 = 'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzL2NmYWM4ZmNhLTIzNTYtNDA4Ny1iZDFmLTViOWExMzIzZmUxNw'
browser.get(new_url_edge7)
time.sleep(10)
pyautogui.click(x=419, y=263)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.keyDown('ctrl')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(0.5)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('alt', 'tab')
new_url_edge8 = 'https://apps.mypurecloud.com/directory/#/engage/telephonyAdmin/edges/update/L2FwaS92Mi90ZWxlcGhvbnkvcHJvdmlkZXJzL2VkZ2VzLzg3YWFhNGVjLTU3ZjEtNDE0Yy1hNzkwLTEyNDk4YzQ4MzlmOA'
browser.get(new_url_edge8)
time.sleep(10)
pyautogui.click(x=419, y=263)
time.sleep(1)
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.keyDown('ctrl')
time.sleep(1.5)
pyautogui.hotkey('shift', 'c')
time.sleep(1.5)
pyautogui.keyUp('ctrl')
time.sleep(0.5)
pyautogui.moveTo(723, 451, 1.5)
time.sleep(1.5)
pyautogui.click(x=723, y=451)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.press('tab')
time.sleep(2)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
pyautogui.moveTo(725, 475, 2)
pyautogui.keyUp('ctrl')
pyautogui.click(x=725, y=475)
time.sleep(1)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
#pyautogui.press('tab')
#time.sleep(1)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.keyDown("ctrl")
time.sleep(1)
pyautogui.hotkey('shift', 'c')
time.sleep(1)
pyautogui.keyUp("ctrl")
time.sleep(1)
pyautogui.moveTo(726, 501, 2)
time.sleep(1)
pyautogui.click(x=726, y=501)
pyautogui.click(x=1242, y=415)
time.sleep(2)
pyautogui.click(x=1224, y=456)
time.sleep(2)
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
pyautogui.press('pagedown')
time.sleep(1)
pyautogui.doubleClick(x=918, y=591)
time.sleep(1)
pyautogui.hotkey("ctrl", "c")
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(2)
pyautogui.doubleClick(x=262, y=184)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=889, y=537)
time.sleep(1)
pyautogui.keyDown('shift')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.keyUp('shift')
time.sleep(1)
pyautogui.hotkey('ctrl', 'u')
time.sleep(2)
pyautogui.write('.')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.write(',')
pyautogui.press('tab')
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('alt', 'tab')
time.sleep(1)
pyautogui.press('left')
pyautogui.press('left')
pyautogui.press('left')
time.sleep(0.5)
pyautogui.keyDown('shift')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
pyautogui.press('up')
time.sleep(0.7)
pyautogui.keyUp('shift')
time.sleep(0.5)
pyautogui.hotkey('alt', 'tab')
time.sleep(0.5)
pyautogui.press('enter')