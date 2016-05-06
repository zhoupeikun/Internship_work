#encoding=utf-8  
import urllib2  
import urllib  
import cookielib  

def lux_Brower(url,user,password):  
    #登陆页面，可以通过抓包工具分析获得，如fiddler，wireshark  
    login_page = "http://182.98.225.43:8080/lux-birt/login.jsp??nocache=1462372120940"  
    try:  
        #获得一个cookieJar实例  
        cj = cookielib.CookieJar()  
        #cookieJar作为参数，获得一个opener的实例  
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
        #伪装成一个正常的浏览器，避免有些web服务器拒绝访问。  
        opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 6.1)')]  
        #生成Post数据，含有登陆用户名密码。  
        data = urllib.urlencode({"username":user,"password":password})  
        #以post的方法访问登陆页面，访问之后cookieJar会自定保存cookie  
        opener.open(login_page,data)  
        #以带cookie的方式访问页面  
        op=opener.open(url)  
        #读取页面源码  
        data= op.read()  
        return data  
    except Exception,e:  
        print str(e)  
  
print lux_Brower("http://182.98.224.12:8080/lux-birt/main.do","admin","123456")  