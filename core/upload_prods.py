from shop.models import Product, Category, Image, ProductParameter, Spec
from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


def get_image(url):
	temp_img = NamedTemporaryFile(delete=True)
	with urlopen(url) as uo:
		assert uo.status == 200
		temp_img.write(uo.read())
		temp_img.flush()
	img = File(temp_img)
	return img, temp_img.name


def upload_to_db():
	file = open('products.txt', 'r').readlines()
	file = ''.join(file)
	lines = file.split("{'title")
	prod_dicts = [eval(str("""{'title"""+i)) for i in lines if i!='']
	total = -1
	for prod_dict in prod_dicts:
		total += 1
		try:
			cat = Category.objects.get(name=prod_dict['category'])
		except:
			cat = Category.objects.create(name=prod_dict['catego	ry'])
		price = int(prod_dict['price']) if prod_dict['price'] != '-' else 0
		prod = Product.objects.create(name=prod_dict['title'], price=price, category=cat)
		c = -1
		for image in prod_dict['images']:
			c += 1
			file = get_image(image)
			img = Image.objects.create(product=prod)
			name = f'product{prod.id}_img{c}'
			img.file.save(name, file[0])
		for parameter in prod_dict['parameters']:
			par = ProductParameter.objects.create(name=parameter[0], value=parameter[1])
			par.product.add(prod)
		for spec in prod_dict['specs']:
			s = Spec.objects.create(
				name=spec['name'],
				value=spec['value'],
				product=prod
				)								
		print(prod)
	return True

{
	'title': 'Apple MacBook Air 13" (M2, 8C CPU/10C GPU, 2022), 24 ГБ, 1 ТБ SSD, «полуночный черный»', 
	'price': '-', 
	'parameters': [('Память', '1 ТБ'), ('Цвет', ' rgb(5, 6, 43)')], 
	'images': ['https://static.re-store.ru/upload/iblock/ddd/wv4xrig3n2ufmz7q35v5echg1zf36tv3.jpg', 'https://static.re-store.ru/upload/iblock/7dd/dglyjusz3miuiesufyr9czhmkwmthhjr.jpg', 'https://static.re-store.ru/upload/iblock/e77/bg23a72h0rmlkgeb4eh1uga7ex62oiul.jpg', 'https://static.re-store.ru/upload/iblock/bdd/3p4w6viioynsgjq340g2b6wde7ph9owe.jpg', 'https://static.re-store.ru/upload/iblock/522/3ezis3mql9rfk3hp9oi15wse3w0bjpei.jpg', 'https://static.re-store.ru/upload/iblock/4d9/ntkzv349icgctubmt75fbzxkkdyrk90k.jpg', 'https://static.re-store.ru/upload/iblock/acb/22obcm4w84upslcit1cxyaqjobsxh6t3.jpg', 'https://static.re-store.ru/upload/iblock/d9f/3frt63wtuwfwu06vkbvqqe16w11jszjf.jpeg', 'https://static.re-store.ru/upload/iblock/d43/h5dmuociyhz8rr9e36thn0a53keog5yd.jpg', 'https://static.re-store.ru/upload/iblock/620/90ime2uskion7b8v8t4dew3b2prji20z.jpg', 'https://static.re-store.ru/upload/iblock/add/gs9z33tym6r54mvljnaskil1aa6axuin.jpg', 'https://static.re-store.ru/upload/iblock/a9c/801o4etc3sz63p5ieqkw6olxuzuk8fba.jpg', 'https://static.re-store.ru/upload/iblock/ddd/wv4xrig3n2ufmz7q35v5echg1zf36tv3.jpg', 'https://static.re-store.ru/upload/iblock/7dd/dglyjusz3miuiesufyr9czhmkwmthhjr.jpg', 'https://static.re-store.ru/upload/iblock/e77/bg23a72h0rmlkgeb4eh1uga7ex62oiul.jpg', 'https://static.re-store.ru/upload/iblock/bdd/3p4w6viioynsgjq340g2b6wde7ph9owe.jpg', 'https://static.re-store.ru/upload/iblock/522/3ezis3mql9rfk3hp9oi15wse3w0bjpei.jpg', 'https://static.re-store.ru/upload/iblock/4d9/ntkzv349icgctubmt75fbzxkkdyrk90k.jpg', 'https://static.re-store.ru/upload/iblock/acb/22obcm4w84upslcit1cxyaqjobsxh6t3.jpg', 'https://static.re-store.ru/upload/iblock/d9f/3frt63wtuwfwu06vkbvqqe16w11jszjf.jpeg', 'https://static.re-store.ru/upload/iblock/d43/h5dmuociyhz8rr9e36thn0a53keog5yd.jpg', 'https://static.re-store.ru/upload/iblock/620/90ime2uskion7b8v8t4dew3b2prji20z.jpg'], 
	'specs': [{'name': 'Срок службы', 'value': '12 мес'}, {'name': 'В комплекте', 'value': 'кабель USB-C/MagSafe 3 (2 м)'}, {'name': 'Доп. возможности', 'value': 'Siri'}, {'name': 'Материал', 'value': 'алюминий'}, {'name': 'Высота', 'value': '21,5 см'}, {'name': 'Ширина', 'value': '30,41 см'},{'name': 'Толщина', 'value': '1,13 см'}, {'name': 'Вес', 'value': '1,24 кг'}, {'name': 'При работе в интернете', 'value': 'до 15 часов'}, {'name': 'Воспроизведение видео', 'value': 'до 18 часов'}, {'name': 'Разъем питания', 'value': 'USB-C'}, {'name': 'Веб-камера', 'value': 'FaceTime 1080p (Full HD)'}, {'name': 'Аудио', 'value': ',встроенные динамики,,поддержка системы многоканального звука,,широкое стерео,,встроенный микрофон(ы),,система направленных микрофонов,,выход 3,5 мм для наушников (расширенная поддержка наушников с высоким импедансом),\n,встроенные динамики,\n,поддержка системы многоканального звука,\n,широкое стерео,\n,встроенный микрофон(ы),\n,система направленных микрофонов,\n,выход 3,5 мм для наушников (расширенная поддержка наушников с высоким импедансом),'}, {'name': 'Количество микрофонов', 'value': '4'}, {'name': 'Трекпад', 'value': 'Force Touch'}, {'name': 'Поддержка интерфейсов', 'value': ',USB 3.1,,USB 4,,DisplayPort,,Thunderbolt,,Thunderbolt 2,,Thunderbolt 3,\n,USB 3.1,\n,USB 4,\n,DisplayPort,\n,Thunderbolt,\n,Thunderbolt 2,\n,Thunderbolt 3,'}, {'name': 'Беспроводная сеть', 'value': ',Wi-Fi (802.11ac),,Wi-Fi 6 (802.11ax),,Bluetooth 5.0,\n,Wi-Fi (802.11ac),\n,Wi-Fi 6 (802.11ax),\n,Bluetooth 5.0,'}, {'name': 'Графический процессор', 'value': 'Apple M2 (8 ядер)'}, {'name': 'Диагональ', 'value': '13,6’’'}, {'name': 'Тип дисплея', 'value': 'Retina'}, {'name': 'Разрешение', 'value': '2560x1664'}, {'name': 'Яркость', 'value': '500 кд/м²'}, {'name': 'Цветовой охват', 'value': 'расширенный (P3)'}, {'name': 'Плотность пикселей на дюйм', 'value': '224'}, {'name': 'Тип накопителя', 'value': 'SSD'}, {'name': 'Тип оперативной памяти', 'value': 'Apple M2'}, {'name': 'Количество ядер процессора', 'value': '10'}, {'name': 'Количество ядер графического процессора', 'value': '8'}, {'name': 'Количество ядер Neural Engine', 'value': '16'}, {'name': 'Год релиза', 'value': '2022'}, {'name': 'Серия', 'value': 'MacBook Air'}, {'name': 'Процессор', 'value': 'Apple M2'}, {'name': 'Цвет', 'value': '«полуночный черный»'}, {'name': 'Память', 'value': '1 ТБ'}, {'name': 'Объем оперативной памяти', 'value': '24 ГБ'}], 
	'category': 'Mac'
}


"""
FOR LIMITED PRODUCTS UPLOAD PER CATEGOR

b = [i['category'] for i in prod_dicts]
b = list(set(b))
cats = {}
	for i in b:
		cats[i] = 0
del b

for i in prod_dicts:
	cats[i['category']] += 1
	if cats[i['category']] < 20:
		prod_dict = i
		# all the rest after total += 1
"""