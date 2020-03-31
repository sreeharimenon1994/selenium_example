from selenium import webdriver

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# use for headless option
# chrome_options.add_argument("--headless")
# use it while using headless option
# chrome_options.add_argument("--window-size=1920x1080")


driver_path = 'C:\\Users\\DELL\\Downloads\\sree\\selenium\\drivers\\chromedriver.exe'
url = 'https://www.bbc.co.uk/news/health-52096049' 

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)
driver.maximize_window()

driver.get(url)
driver.implicitly_wait(1)

title = driver.find_element_by_class_name('story-body__h1')

author = driver.find_element_by_class_name('byline__name')

timeVar = driver.find_element_by_class_name('relative-time')
timeVar = timeVar.get_attribute("data-seconds")

content = driver.find_element_by_class_name('story-body__introduction')


print('\n\nTitle:', title.text)
print('\nAuthor:', author.text)
print('\nTime:', timeVar)
print('\nContent:', content.text, '\n\n')

driver.quit()