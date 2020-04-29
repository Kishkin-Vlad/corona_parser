from selenium import webdriver
import csv
import time


def main():
    link = 'https://covid.2gis.ru/stat?utm_source=online&utm_medium=mapcontrol&utm_campaign=firsttry&lt=56.301157&ln=43.928022&z=11'

    with open('statistics.csv', 'w', newline='', encoding='utf-8') as File:
        writer = csv.writer(File)
        parse(link, writer)


def parse(link, writer):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get(link)

    # чтобы все продукты загрузились
    print('sleep before')
    time.sleep(1)
    # driver.execute_script("window.scrollTo(0, 10000)")
    print('sleep after')

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

    for i in range(length):
        print(arr_name[i].text)
        print(arr_count[i].text)
        print(arr_infected[i].text)
        print(arr_recovered[i].text)
        print(arr_died[i].text)

    writer.writerow([date])
    writer.writerow([global_stat[0], global_stat[1], global_stat[1]])
    for i in range(length):
        writer.writerow([i, arr_name[i].text, arr_count[i].text,
                         arr_infected[i].text[1:], arr_recovered[i].text,
                         arr_died[i].text])

    driver.close()

# from selenium import webdriver
# import csv
# import time
#
#
# def main():
#     f = open('links_need.txt', 'r')
#     link_start = 'https://lebazar.uz'
#     links = []
#     for line in f:
#         links.append(line[:-1])
#     f.close()
#     print(links)
#     counter = 0
#
#     with open('product.csv', 'a', newline='', encoding='utf-8') as File:
#         writer = csv.writer(File)
#         # writer.writerow(['category', 'subcategory', 'name', 'price', 'count', 'image'])
#         # parse(link_start + links[4], writer)
#         for link in links:
#             counter += 1
#             print('\n', counter)
#             parse(link_start + link, writer)
#
#
# def parse(link, writer):
#     driver = webdriver.Chrome()
#     driver.get(link)
#
#     # чтобы все продукты загрузились
#     print('sleep before')
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(1)
#     driver.execute_script("window.scrollTo(0, 10000)")
#     time.sleep(5)
#     print('sleep after')
#
#     arr_product = driver.find_elements_by_class_name('clickable')
#     categories = driver.find_elements_by_class_name('hide-for-xlarge')
#     img_product = driver.find_elements_by_class_name('product-img')
#
#     # Массив продуктов (ready)
#     arr_product_ready = []
#     # Временный массив для проверок
#     nado_text = []
#
#     gap = len(arr_product) - len(img_product)
#     if arr_product[gap].text == 'Бестселлеры':
#         temp = arr_product.pop(gap + 2)
#         temp = arr_product.pop(gap + 1)
#         temp = arr_product.pop(gap)
#         del temp
#
#     print(len(arr_product))
#     print(len(img_product))
#     # for i in img_product:
#     #     print(i.get_attribute('src'))
#
#     j = 0  #
#     for i in arr_product:
#         if j >= gap:
#             nado_text.append(i.text)
#
#             if i.text[:1] == '-':
#                 text_without_sell = i.text[i.text.find('\n') + 1:]
#
#                 name = text_without_sell[:text_without_sell.find('\n')]
#
#                 price = text_without_sell[text_without_sell.find('\n') + 1:]
#                 count = price[price.find('.') + 2:price.find('\n')]
#                 price = price[:price.find('.')]
#             else:
#                 name = i.text[:i.text.find('\n')]
#
#                 price = i.text[i.text.find('\n') + 1:]
#                 count = price[price.find('.') + 2:price.find('\n')]
#                 price = price[:price.find('.')]
#             arr_product_ready.append(
#                 {'category': categories[1].text, 'subcategory': categories[2].text, 'name': name, 'price': price,
#                  'count': count, 'image': img_product[j - gap].get_attribute('src')})
#         j += 1
#
#     for i in range(j - gap):
#         writer.writerow([arr_product_ready[i]['category'], arr_product_ready[i]['subcategory'],
#                          arr_product_ready[i]['name'], arr_product_ready[i]['price'],
#                          arr_product_ready[i]['count'], arr_product_ready[i]['image']])
#     print(nado_text)
#     print()
#
#     print(arr_product_ready)
#     driver.close()
#
#
# main()

