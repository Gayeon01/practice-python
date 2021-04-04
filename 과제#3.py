web = "http://naver.com"

web2 = web.replace("http://","")

print ("%s의 비밀번호:" %web +web2[:3] +str(len(web2)-4) +str(web2.count("e"))+"!")