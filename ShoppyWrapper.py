import os,sys,requests,json

class Feedback:
	feedback_id = ""
	order_id = ""
	comment = ""
	stars = 0
	def __init__(self,feedback_id,order_id,comment,stars):
		self.feedback_id = feedback_id
		self.order_id = order_id
		self.comment = comment
		self.stars = stars
class User:
	username = ""
	email = ""
	currency = ""
	def __init__(self,username,email,currency):
		self.username = username
		self.email = email
		self.currency = currency

class Coupon:
	cid = ""
	seller_id = ""
	code = ""
	value = ""
	def __init__(self,cid,seller_id,code,value):
		self.cid = cid
		self.seller_id = seller_id
		self.code = code
		self.value = value

class Query:
	qid = ""
	subject = ""
	email =""
	message = ""
	created_at = ""
	def __init__(self,qid,subject,email,message,created_at):
		self.qid = qid
		self.subject = subject
		self.email = email
		self.message = message
		self.created_at = created_at

class Product:
	pid = ""
	title = ""
	description = ""
	price = 0
	currency = ""
	stock = 0
	def __init__(self,pid,title,description,price,currency,stock):
		self.pid = pid
		self.title = title
		self.description = description
		self.price = price
		self.currency = currency
		self.stock = stock


class Shoppy:
	apiKey = ""
	def __init__(self,apikey):
		self.apiKey = apikey
		print(' [~] shoppy wrapper initiated <'+self.apiKey+'>')
	def getUser(self):
		res = requests.get(url=f"https://shoppy.gg/api/v1/user",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy user request -> {str(res.status_code)}')
		return res 
	def getOrders(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/orders/",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy order request -> {str(res.status_code)}')
		return res
	def getOrder(self,oid):
		res=requests.get(url=f"https://shoppy.gg/api/v1/orders/{oid}",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy order request -> {str(res.status_code)}')
		return res
	def getProducts(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/products",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy products request -> {str(res.status_code)}')
		return res
	def getProduct(self,pid):
		res=requests.get(url=f"https://shoppy.gg/api/v1/products/{pid}",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy products request -> {str(res.status_code)}')
		return res
	def getCoupons(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/coupons",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy coupons request -> {str(res.status_code)}')
		return res
	def getCoupon(self,cid):
		res=requests.get(url=f"https://shoppy.gg/api/v1/coupons/{cid}",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy coupon request -> {str(res.status_code)}')
		return res
	def getQueries(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/queries",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy queries request -> {str(res.status_code)}')
		return res
	def getQuery(self,qid):
		res=requests.get(url=f"https://shoppy.gg/api/v1/queries/{qid}",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy products request -> {str(res.status_code)}')
		return res
	def getWebhooks(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/webhooks",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy webhook request -> {str(res.status_code)}')
		return res
	def getWebhook(self,wid):
		res=requests.get(url=f"https://shoppy.gg/api/v1/webhooks/{wid}",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy webhook request -> {str(res.status_code)}')
		return res
	def getFeedbacks(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/feedbacks",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy feedback request -> {str(res.status_code)}')
		return res
	def getFeedback(self,fid):
		res=requests.get(url=f"https://shoppy.gg/api/v1/feedbacks/{fid}",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy feedback request -> {str(res.status_code)}')
		return res
	def getSettings(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/settings",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy settings request -> {str(res.status_code)}')
		return res		
	def FormatFeedback(self,feedback):
		formatted = []
		for i in range(len(feedback)):
			jso = json.loads(feedback)[0]
			fback_class = Feedback(jso["id"],jso["order_id"],jso["comment"],jso["stars"])
			formatted.append(fback_class)
		return formatted
	def FormatSettings(self):
		text = self.getSettings().text
		settings = json.loads(text)
		user = settings["user"]["username"]
		user_c = User(settings["user"]["username"],settings["user"]["email"],settings["settings"]["currency"])
		return user_c
	def FormatQueries(self):
		data = json.loads(self.getQueries().text)
		queries = []
		for i in range(1000):
			try:
				queries.append(Query(data[i]["id"],data[i]["subject"],data[i]["email"],data[i]["message"],data[i]["created_at"]))
			except:
				return queries
		return queries
	def FormatCoupons(self):
		data = json.loads(self.getCoupons().text)
		coupons = []
		for i in range(1000):
			try:
				coupons.append(Coupon(data[i]["id"],data[i]["seller_id"],data[i]["code"],data[i]["value"]))
			except:
				return coupons
		return coupons

	def FormatProducts(self):
		data = json.loads(self.getProducts().text)
		products = []
		for i in range(1000):
			try:
				products.append(Product(data[i]["id"],data[i]["title"],data[i]["description"],data[i]["price"],data[i]["currency"],data[i]["stock"]))
			except:
				return products
		return products
