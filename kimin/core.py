import os, json, folium
class Core:
	def __init__(kimin, folder="db"):
		kimin.folder = folder
	
	def AddDb(kimin, data, path="lokasi.min"):
		
		if not os.path.exists(f"{kimin.folder}/{path}"):
			
			with open(f"{kimin.folder}/{path}",'w') as dataku:
				data = json.dumps(data)
				dataku.write(f"{data}\n")
		else:
			db = kimin.GetData()
			if not data in db:
				data = json.dumps(data)
				with open(f"{kimin.folder}/{path}", 'a') as dataku:
					dataku.write(f"{data}\n")
			
			else:
				return "Duplicate Data"
		
		return "Sukses Add Data"
	
	def Maps(kimin, latitude, longitude, label, auto_reload=True):
		if auto_reload == True:
			title_html = '''<title>Kimin Tracking</title>
							<meta http-equiv="refresh" content="10" />'''
		elif auto_reload == False:
			title_html = '''<title>Kimin Tracking</title>'''
		map = folium.Map(location=[latitude, longitude], zoom_start=18, control_scale=True)
		map.get_root().html.add_child(folium.Element(title_html))
		popup  = folium.Popup(label, max_width=600, max_height=600)
		folium.vector_layers.Marker(location=[latitude, longitude], tooltip=label, popup = popup).add_to(map)
		map.save(f'templates/maps.html')
	
	def GetData(kimin, path="lokasi.min"):
		with open(f"{kimin.folder}/{path}",'r') as dataku:
			data = dataku.read().splitlines()
		hasil = []
		for i in data:
			hasil.append(json.loads(i))
		return hasil
		