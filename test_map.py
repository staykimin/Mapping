import folium
mapObj = folium.Map(
			location=[24.2170111233401, 81.0791015625000],
			zoom_start=5)
# folium.Rectangle([(28.6471948,76.9531796), (19.0821978,72.7411)]).add_to(mapObj)
mapObj.save('output.html')