from flask import Flask, render_template, request, session, url_for, redirect, send_file
from flask_ngrok import run_with_ngrok
from kimin.core import Core
from pyngrok import ngrok

import datetime, requests
server = Flask(__name__)
server.jinja_env.auto_reload = True
server.config['TEMPLATES_AUTO_RELOAD'] = True

token = input("Masukkan Token Dari Ngrok : ")
x = input("Aktifkan Auto Reload : ")
if x.lower() == "y":
	auto_reload = True
else:
	auto_reload = False
run_with_ngrok(server)
ngrok.set_auth_token(token)

@server.route("/data", methods=['GET'])
def Data():
	sin = Core()
	data = sin.GetData()
	return data

@server.route("/maps", methods=['GET'])
def Maps():
	return render_template("maps.html")

@server.route("/", methods=['POST'])
def Testing():
	label = request.form['label']
	warna = request.form['warna']
	author = request.form['author']
	long = request.form['long']
	lat = request.form['lat']
	now = datetime.datetime.now()
	now = now.strftime("%d-%m-%Y %H:%M:%S")
	data = {"label":label, "warna":warna, "author":author, "create":now, "long":long, "lat":lat}
	sin = Core()
	hasil = sin.AddDb(data)
	data = sin.Maps(lat, long, label, auto_reload)
	return hasil

if __name__ == "__main__":
	server.run()