from bs4 import BeautifulSoup
from datetime import *
from OneClick import Hunter
hd = str(Hunter.Services())

try:
	import requests  ,re, os , sys , random , uuid , user_agent , json,secrets,secrets
	from uuid import uuid4
	from secrets import *
	from user_agent import generate_user_agent
	import requests
	import names
	import uuid,string
	import instaloader
	import hashlib
	import urllib
	import mechanize
	import json
	import secrets
	import smtplib
	import time
    
	
except ImportError:
	os.system('pip install requests')

	
	
uid = str(uuid4)
class salammzere3:
	def Info_IG(user,sessionid):
		head = {
		'accept': '*/*',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
		'cookie': 'mid=YvvDrAALAAFLJor2N0MGQgLWW0UW; ig_did=A837F007-F7BC-4802-8EF0-A68D997C297D; ig_nrcb=1; datr=nGUPYz2GPkoNMu7UWgKcsp8x; csrftoken=ZUyjsgp9hIYl4CfqYu7ilo6ZEgv2gl2Z; ds_user_id=5376288835; shbid="14120\0545376288835\0541695151496:01f736544db5dcfedc306d753acc4c86d0c42f55fdf7c5941c9c39c6edf1a239cafb04a2"; shbts="1663615496\0545376288835\0541695151496:01f7487ad9bfa5a41605905bf69300e6d01dcca404a38a4f43c2b140c3c002789b13493e"; sessionid='+sessionid+'; rur="NAO\0545376288835\0541695151518:01f70ce168631f1e97241f7871dda739a5cde84682f30c3436b4f2fbe18ad3eaf1c6dc9c"',
		'origin': 'https://www.instagram.com',
		'referer': 'https://www.instagram.com/',
		'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': generate_user_agent(),
		'x-asbd-id': '198387',
		'x-csrftoken': 'ZUyjsgp9hIYl4CfqYu7ilo6ZEgv2gl2Z',
		'x-ig-app-id': '936619743392459',
		'x-ig-www-claim': 'hmac.AR2M8P8_d7bvLTR7zVAphA15aAoyYXFGByqPC36ugQK8Wv2m',
		'x-instagram-ajax': '1006224323',}

		re = requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis', headers=head).json()
		id = re['graphql']['user']['id']
		name = re['graphql']['user']['full_name']
		userr = re['graphql']['user']['username']
		follows = re['graphql']['user']['edge_followed_by']['count']
		following = re['graphql']['user']['edge_follow']['count']
		date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]
		bio = re['graphql']['user']['biography']
		isp = re['graphql']['user']['is_private']
		post = re['graphql']['user']['edge_owner_to_timeline_media']['count']
		return {'user':userr,'name':name,'id':id,'followers':follows,'following':following,'date':date,'bio':bio,'private':isp,'post':post}
		
	
	
	def Instagram(email):
	   url2 = 'https://i.instagram.com/api/v1/accounts/login/'
	   headers2 = {
        'User-Agent':str(hd),
        'Accept':'*/*',
        'Cookie':'missing',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'en-US',
        'X-IG-Capabilities':'3brTvw==',
        'X-IG-Connection-Type':'WIFI',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Host':'i.instagram.com'}
	   data2 = {
        'uuid':uid,
        'password':'SalamH@T5B55',
        'username':email,
        'device_id':uid,
        'from_reg':'false',
        '_csrftoken':'missing',
        'login_attempt_countn':'0'}
	   res2 = requests.post(url2,headers=headers2,data=data2).text
	   if ('"invalid_user"')in res2:
        	return {'status':'FALSE','BY':'@T5B55'}
	   elif ('"bad_password"') in res2:
        	return {'status':'OK','BY':'@T5B55'}
	   else:
        	return {'status':'FALSE','BY':'@T5B55'}
	
	def TikTok(email):
		url = "https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1656747775&as=a1e67fbb4fffb246cf0244&cp=f2f02d6bfbffb36de1eomw&mas=01cd120efcb179ac1b331e5cecb80282052c2c4c0c66c66c2c4c46"
		headers = {
            'host':'api2-19-h2.musical.ly',
            'connection':'keep-alive',
            'cookie':'sstore-idc=maliva; store-country-co de=iq; odin_tt=056f31c10f8c82638f6d4d64669ad49e9c36d4946d5d596f433d7f2d75fa1592a21c201d712196d54ee4ae4e14ac8708eee32dc97c85c0a65510024ecc0698346f73ecab038b7160dbff96ced716b8af',
            'accept-Encoding':'gzip',
            'user-agent':'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ; SM-A022F; Build/RP1A.200720.012; Cronet/58.0.2991.0)',
            'connection': 'close'        
    }
		data = f"app_language=ar&manifest_version_code=2018101933&_rticket=1656747775754&iid=7115676682581247750&channel=googleplay&language=ar&fp=&device_type=SM-A022F&resolution=720*1471&openudid=8c05dec470c7b7d5&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=280&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7023349253125604869&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=samsung&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233"
		res = requests.post(url,headers=headers,data=data).text
		if 'Sent successfully' in res:
			return {'status':'OK','BY':'@T5B55'}
		else :
			return {'status':'FALSE','BY':'@T5B55'}
	
	def Info_TikTok(user):
		headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
		data=None
		rd = requests.get(f"https://www.tiktok.com/@{user}", headers=headers).text
		try:
			soup = BeautifulSoup(rd, 'html.parser')
			script = soup.find(id='SIGI_STATE').contents
			rr = str(script).split('},"UserModule":{"users":{')[1]
			try:
				na=rr.split(',"nickname":"')[1].split('",')[0]
			except:
				na='false'
			try:
				id=rr.split('"id":"')[1].split('",')[0]
			except:
				id='false'
			try:
				pr=rr.split('"privateAccount":')[1].split(',')[0]
			except:
				pr='false'
			try:
				flog=rr.split('"followingCount":')[1].split(',')[0]
			except:
				flog='0'
			try:
				flos=rr.split('"followerCount":')[1].split(',')[0]
			except:
				flos='0'
			try:
				bio=rr.split('"signature":')[1].split(',')[0]
			except:
				bio='false'
			try:
				video=rr.split('"videoCount":')[1].split(',')[0]
			except:
				video='false'
			try:
				like= rr.split('"heartCount":')[1].split(',')[0]
			except:
				like='0'
			try:
				user= rr.split('"uniqueId":')[1].split(',')[0]
			except:
				user='false'
			try:
			 url_id = int(id)
			 binary = "{0:b}".format(url_id)
			 i = 0
			 bits = ""
			 while i < 31:
			     bits += binary[i]
			     i += 1
			 timestamp = int(bits, 2)
			 timme = datetime.fromtimestamp(timestamp)
             #print(timme)
			except:
				timme= 'false'
			return {"user":user,"name":na,"id":id,"date":timme,"followers":flos,"following":flog,"privacy":pr,"like":like,"video":video,"bio":bio}
		except:
				return 'BAD'

		
	
	
	def Instalogin(email,password):
		
		UrlSalam = 'https://www.instagram.com/accounts/login/ajax/'
		
		HeadSalam = {

    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-length':'317',
    'content-type':'application/x-www-form-urlencoded',
    'cookie':'mid=YdduAwAEAAH5tvQgBxaWFmtCauW1; ig_did=3B9E189F-664C-4C27-BAD4-A4DC839FFFFA; ig_nrcb=1; shbid="15789\0545722116218\0541674148260:01f7b34891a790ddc3b2f8f61b0c76d2e539c3efaedb09b6812283940bfcc6739f7a6930"; shbts="1642612260\0545722116218\0541674148260:01f74a3f9c5b7857cd36ad8a36a61bbe4bcc22061a61a730590ea1f665bd85916ae193b4"; csrftoken=qMiGRabzXyZlJPciGxtTKQAJZkCv0Rhi',
    'origin':'https://www.instagram.com',
    'referer':'https://www.instagram.com/',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-origin',
    'user-agent':generate_user_agent(),
    'x-asbd-id':'198387',
    'x-csrftoken':'qMiGRabzXyZlJPciGxtTKQAJZkCv0Rhi',
    'x-ig-app-id':'936619743392459',
    'x-ig-www-claim':'0',
    'x-instagram-ajax':'9e76603e49dc',
    'x-requested-with':'XMLHttpRequest'}
    
		DatSalam = {
	'username': email,
	'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+ password
	}
		ReqSalam = requests.post(UrlSalam,headers=HeadSalam,data=DatSalam)
		if ('"authenticated":true') in ReqSalam.text:
			
			
			os.system('rm -rf sessionid.txt')
			
			APK = ReqSalam.cookies['sessionid']
			
			f = open('sessionid.txt','a')
			
			f.write(APK+"\n")
			
			f.close()
			
			return {'status':'Success','login':'true','sessionid':str(APK)}
			
		if str('"message":"challenge_required","challenge"') in ReqSalam.text:
			
			return {'status':'challenge_required'}
			
		else:
			
			return {'status':'error_login'}
		


	def gmail(email):
	    url = 'https://android.clients.google.com/setup/checkavail'
	    headers = {
		'Content-Length':'98',
		'Content-Type':'text/plain; charset=UTF-8',
		'Host':'android.clients.google.com',
		'Connection':'Keep-Alive',
		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',}
	    data = json.dumps({
		'username':str(email),
		'version':'3',
		'firstName':'GDO_0',
		'lastName':'GDOTools' })
	    res = requests.post(url,data=data,headers=headers)
	    if res.json()['status'] == 'SUCCESS':
	           return {'status':'Success','email':True}
	           
	    else:
	           return {'status':'error','email':False}
            
	def instagram(email):
	    headers = {
            # 'Content-Length': '143',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (25/7.1.2; 160dpi; 383x681; LENOVO/Android-x86; 4242ED1; x86_64; android_x86_64; en_US)',
            'Accept-Language': 'en-US',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': 'AQ==',
            # 'Accept-Encoding': 'gzip',
        }

	    data = {
            'ig_sig_key_version': '4',
            "q": f"{email}"
        }

	    response = requests.post('https://i.instagram.com/api/v1/users/lookup/', headers=headers, data=data).text
	    if "ok" in response:
	       return {'email': email,'status':'True'}
	    else:
	        return {'email': email,'status':'False'}
	        
	        
	def tiktok(email):
	    url = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c"
	    data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA"
	    hed = {
		"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"}
		
	    r = requests.post(url,headers=hed,data=data)
	    if '{"is_registered":1}' in r.text:
	        return {"status":"register","email":email}
		    
	    elif '{"is_registered":0}' in r.text:
	        return {"status":"not_register","email":email}
		    
	    else:
	        return {"status":"error","email":email}



	def logintiktok(email,password):
	    url = 'https://api2.musical.ly/passport/user/login/?mix_mode=1&username=1&email=&mobile=&account=&password=hg&captcha=&ts=&app_type=normal&app_language=en&manifest_version_code=2018073102&_rticket=1633593458298&iid=7011916372695598854&channel=googleplay&language=en&fp=&device_type=SM-G955F&resolution=1440*2792&openudid=91cac57ba8ef12b6&update_version_code=2018073102&sys_region=AS&os_api=28&is_my_cn=0&timezone_name=Asia/Muscat&dpi=560&carrier_region=OM&ac=wifi&device_id=6785177577851504133&mcc_mnc=42203&timezone_offset=14400&os_version=9&version_code=800&carrier_region_v2=422&app_name=musical_ly&version_name=8.0.0&device_brand=samsung&ssmix=a&build_number=8.0.0&device_platform=android&region=US&aid=&as=&cp=Qm&mas='
	    headers = \
            {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
            'cookie': 'csrftoken=' + str(secrets.token_hex(8) * 2) + '; sessionid=' + str(secrets.token_hex(8) * 2) + ';',
            'User-Agent': 'Connectionzucom.zhiliaoapp.musically/2018073102 (Linux; U; Android 9; en_AS; SM-G955F; Build/PPR1.180610.011; Cronet/58.0.2991.0)z',
            'Host': 'api2.musical.ly', 'Connection': 'keep-alive'}
	    data = {"email": str(email), "password": str(password)}
	    res = requests.post(url, headers=headers, data=data)
	    if ("user_id") in res.text:
	        sessionid = str(res.json()['data']['session_key'])
	        return {'username': str(email), 'password': str(password), 'status': 'True', 'SessionId': sessionid}
	        
	    elif ("Incorrect account or password") in res.text:
	       return {'username': str(email), 'password': str(password), 'status' :'Error Password Or Username'}
	    else:
	        return {'username': str(email), 'password': str(password), 'status' :'False'}
	        
	  
	  
	def hotmail(email):
	    url = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990"
	    headers = {
    	    "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": str(generate_user_agent()),
            "Connection": "close",
            "Host": "odc.officeapps.live.com",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
            "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
            "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
            "uaid": "d06e1498e7ed4def9078bd46883f187b",
            "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}
	    res = requests.post(url, data="", headers=headers).text
	    if ("Neither") in res:
	        return {'status': 'Success', 'email': 'True'}
	    else:
	        return {'email': email,'status':'False'}

	    
	    
	    
	def Send_Reset(email):
	    uidd = str(uuid4)
	    
	    url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
	    headers = {
    "Content-Length": "325",
    "Content-Type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Host": "i.instagram.com",
    "Connection": "Keep-Alive",
    "User-Agent": "Instagram 6.12.1 Android (30/11; 280dpi; 720x1339; samsung; SM-A115F; a11q; qcom; ar_AE)",
    "Cookie": "mid\u003dYuNHpwABAAHN0phpxYgGf2YLosTU; csrftoken\u003dupWgl5AujnKWZVrYTSGeHBdxN3XyBQC9",
    "Cookie2": "$Version\u003d1",
    "Accept-Language": "ar-AE, en-US",
    "X-IG-Connection-Type": "WIFI",
    "X-IG-Capabilities": "AQ\u003d\u003d",
    "Accept-Encoding": "gzip"}
    
	    data = {
'ig_sig_key_version':'4',
'user_email':email,
'device_id':uidd}
	    req = requests.post(url,headers=headers,data=data).text
	    if 'ok' in req:
	        return {'status': 'Success', 'email': email}
	        
	    else:
	        return {'status': 'error', 'email': email}
	        

class session_insta:
    
    def login(session: str) -> str:
        url = "https://i.instagram.com/api/v1/accounts/current_user/?edit=true"
        headers = {
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTBw==',
            'User-Agent': 'Instagram 9.7.0 Android (28/9; 420dpi; 1080x2131; samsung; SM-A505F; a50; exynos9610; en_US)',
            'Accept-Language': 'en-US',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'Connection': 'keep-alive',
            'Accept': '*/*'}
        cookies = {"sessionid": str(session)}
        res = requests.get(url, headers=headers, cookies=cookies).json()
        if str('message') in res:
            return {'status': 'error', 'login': 'error_session'}

        else:
            username = res['user']['username']
            id = res['user']['pk']
            full_name = res['user']['full_name']
            profile = res['user']['profile_pic_url']
            private = res['user']['is_private']
            following = info_insta.following(username)
            followers = info_insta.followers(username)
            date = info_insta.date(username)
            return {'status':'Success','username':str(username),'id':str(id),'name':str(full_name),'following':str(following),'followers':str(followers),'date':str(date),'private':str(private),'profile':str(profile),'sessionid':str(session)}




class Tiktok:
    def sendreset(email: str) -> str:
        url = 'https://api16-va.tiktokv.com/passport/email/send_code/?passport-sdk-version=19&os_api=22&device_type=SM-G975N&ssmix=a&manifest_version_code=2021806060&dpi=240&uoo=0&carrier_region=AR&region=IQ&app_name=musical_ly&version_name=18.6.6&timezone_offset=10800&ts=1660261379&ab_version=18.6.6&residence=AR&cpu_support64=false&current_region=US&ac2=wifi&app_type=normal&ac=wifi&host_abi=armeabi-v7a&update_version_code=2021806060&channel=googleplay&_rticket=1660261381871&device_platform=android&iid=7126814077612115718&build_number=18.6.6&locale=ar&op_region=AR&version_code=180606&timezone_name=Europe%2FMoscow&cdid=86654e69-0edf-405a-a5a1-181f0e7aa14f&openudid=1c8a72b315ac7fbf&sys_region=IQ&device_id=6833300910404519430&app_language=ar&resolution=1280*720&os_version=5.1.1&language=ar&device_brand=samsung&aid=1233&mcc_mnc=310410'
        
        headers = {
        'Host': 'api16-va.tiktokv.com',
        'x-ss-stub': '04465DFECBF3ED2D56AF61B7DE2921AB',
        'accept-encoding': 'gzip',
        'passport-sdk-version': '19',
        'sdk-version': '2',
        'x-ss-req-ticket': '1660261382504',
        'cookie': 'odin_tt=7a321b6667e2ada3027155e053cc1e681ac076f643fbe4861f283fe2ecbc80c1260f1371bb96c8a4812ba32df7d22d4b785a5ba640289e1913e674bd3ffd6b52e8e38d3ade7f3d2d3e41f79931cfb1d4; passport_csrf_token_default=f7bdb605ee9f55f0186b3f0da6cc71e4; store-idc=alisg; store-country-code=cn; install_id=7126814077612115718; ttreq=1$065fc339e22f7da8844faf9adc4f19e5f267c6eb',
        'x-gorgon': '04048032500189a229bdf66e04feefcf47d5ccc94e336871888b',
        'x-khronos': '1660261382',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'content-length': '131',
        'user-agent': 'okhttp/3.10.0.1',
    }
        data = f'email={email}&account_sdk_source=app&rules_version=v2&mix_mode=1&multi_login=1&type=31'
        req = requests.post(url, headers=headers, data=data)
        if req.json()["message"] =="success":
            return {'status': 'Success', 'email': email}
            
        else:
            return {'status': 'error', 'email': email}
            
            
class salamhunter:
	def Create_IG(username,password,name):
		hosturl = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
		createurl = "https://www.instagram.com/accounts/web_create_ajax/attempt/"
		ageurl = "https://www.instagram.com/web/consent/check_age_eligibility/"
		sendurl = "https://i.instagram.com/api/v1/accounts/send_verify_email/"
		checkcodeurl = "https://i.instagram.com/api/v1/accounts/check_confirmation_code/"
		createacc = "https://www.instagram.com/accounts/web_create_ajax/"
		session = requests.Session()
		session.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36', 'Referer': hosturl}
		session.proxies = {'http': requests.get("https://gimmeproxy.com/api/getProxy").json()['curl']}
		reqB = session.get(hosturl)
		session.headers.update({'X-CSRFToken': reqB.cookies['csrftoken']})
		rem = requests.get("https://10minutemail.net/address.api.php")
		qwe=rem.json()['mail_get_mail'],rem.cookies['PHPSESSID']
		maile=qwe[0]
		mailss=qwe[1]
		
		data = {'enc_password':'#PWD_INSTAGRAM_BROWSER:0:&:'+password,'email':maile,'username':username,'first_name':name,'client_id':'','seamless_login_enabled':'1','opt_into_one_tap':'false',}
		reg1 = session.post(url=createurl,data=data,allow_redirects=True)
		if(reg1.json()['status'] == 'ok'):
			True
		else:
			
			return {"status": "username or password Error"}
		data2 = {'day':'4','month':'4','year':'2001',}
		reqA = session.post(url=ageurl,data=data2,allow_redirects=True)
		if(reqA.json()['status'] == 'ok'):
			True
		else:
			return {"status": "Error Send Date"}
		sendcode = session.post(url=sendurl,data={'device_id': '','email': maile},allow_redirects=True)
		if(sendcode.json()['status'] == 'ok'):
			True
		else:
			return {"status": "Error Send Code"}
		while 1:
			rei = requests.get("https://10minutemail.net/address.api.php",cookies={"PHPSESSID":mailss})
			inbox=rei.json()['mail_list'][0]['subject']
			if "Instagram" in inbox:
				code = inbox.split(" is")[0]
				True
				break	 
			else:
				True
				continue
		confirmation = session.post(url=checkcodeurl,data={'code': code,'device_id': '','email': maile})
		if confirmation.json()['status'] == "ok":
			signup_code = confirmation.json()['signup_code']
			True
			create = session.post(
				url=createacc,
				data={
'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+password,
'email': maile,
'username': username,
'first_name': name,
'month': '4',
'day': '4',
'year': '2001',
'client_id': '',
'seamless_login_enabled': '1',
'tos_version': 'row',
'force_sign_up_code': signup_code})
			if '"account_created": false' in create.text:
				return {"status": "Error Create Account"}
			else:
				return {"status": "Successful Create" , "username": username , "password": password , "name": name , "email": maile , "Telegram": "@T5B55"}
		else:
			return {"status": "Error Get SignUp Code"}