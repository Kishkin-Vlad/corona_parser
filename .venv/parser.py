from selenium import webdriver
import csv
import time


def main():
    # link with statistics
    link = 'https://covid.2gis.ru/stat?utm_source=online&utm_medium=mapcontrol&utm_campaign=firsttry&lt=56.301157&ln=43.928022&z=11'

    # write to file
    with open('statistics.csv', 'w', newline='', encoding='utf-8') as File:
        writer = csv.writer(File)
        parse(link, writer)


def parse(link, writer):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(link)

    # loading page
    print('sleep before')
    time.sleep(1)
    # driver.execute_script("window.scrollTo(0, 10000)")
    print('sleep after')

    # receiving data
    date = driver.find_elements_by_class_name('_1yqjulD6HRCu9HJhnSLavU')[0].text
    date = date[17:]
    need = driver.find_elements_by_class_name('_2SPkxbSToMQWrknZQxaSTy')
    global_stat = [need[0].text,
                   need[1].text,
                   need[2].text]
    del need
    arr_name = driver.find_elements_by_class_name('_3r-dq_HmMIDwJZvs5husso')
    arr_count = driver.find_elements_by_class_name('_3fnsOxbKy38SgCDl8XpTtk')
    arr_infected = driver.find_elements_by_class_name('_3kI38TNjLuopjIH5V6tIu5')
    arr_recovered = driver.find_elements_by_class_name('uM3qmboljxNTcBp-nM0_T')
    arr_died = driver.find_elements_by_class_name('_ZHvbI4vYrOPo6Ii-V5Lj')

    length = len(arr_name)

    # print data in screen
    for i in range(length):
        print(arr_name[i].text)
        print(arr_count[i].text)
        print(arr_infected[i].text)
        print(arr_recovered[i].text)
        print(arr_died[i].text)

    # write data to db (csv)
    writer.writerow([date])
    writer.writerow([global_stat[0], global_stat[1], global_stat[1]])
    for i in range(length):
        writer.writerow([i, arr_name[i].text, arr_count[i].text,
                         arr_infected[i].text[1:], arr_recovered[i].text,
                         arr_died[i].text])

    driver.close()


main()
