from selenium import webdriver
path= 'C:\\Users\\DELL\\Downloads\\sree\\selenium\\drivers\\chromedriver.exe'
driver = webdriver.Chrome(path)

url = 'https://www.bbc.co.uk/news/health-52096049' 

driver.get(url)

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