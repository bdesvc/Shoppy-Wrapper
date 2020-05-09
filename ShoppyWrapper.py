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
	def getTickets(self):
		res=requests.get(url=f"https://shoppy.gg/api/v1/tickets",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy ticket request -> {str(res.status_code)}')
		return res
	def getTicket(self,tid):
		res=requests.get(url=f"https://shoppy.gg/api/v1/tickets/{tid}",headers={'Content-Type': 'application/json','Authorization':self.apiKey,'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'})
		#print(f' [~] shoppy ticket request -> {str(res.status_code)}')
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





os.system("cls")
shoppy_api = Shoppy('QE7opngxLgMA8QslEWMFFmJR0pyjmvPidKIPu7t9WFyCmli0RE')

user = shoppy_api.FormatSettings()

print('  shoppy user report -> ')
print(f'   username -> {user.username}\n   email -> {user.email}\n   currency -> {user.currency}')