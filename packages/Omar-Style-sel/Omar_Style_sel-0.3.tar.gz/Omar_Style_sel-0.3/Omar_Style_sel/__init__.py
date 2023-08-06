"""
Copyright: You are prohibited from publishing this project in another project
Code developer Omar_Style_ps

Contact for inquiries:
    https://t.me/OmarStyle1
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
#Omar_Style 
class BrowsersProxy:
    #Omar_Style 
    def proxy_firefox(self, pr, firr):
        try:
            proxy_host, proxy_port = pr.split(":")
            # print(proxy_host,proxy_port)
        except ValueError:
            print("Please enter the proxy correctly   Example  => 95.56.254.139:3128")
            return

        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("network.proxy.type", 1)
        firefox_profile.set_preference("network.proxy.http", proxy_host)
        firefox_profile.set_preference("network.proxy.http_port", int(proxy_port))
        firefox_profile.set_preference("network.proxy.ssl", proxy_host)
        firefox_profile.set_preference("network.proxy.ssl_port", int(proxy_port))

        driver = webdriver.Firefox(firefox_profile=firefox_profile)
        driver.get(firr)
        return driver

    def proxy_chrome(self,proxy_address,Link,driver_path=None):
        options = Options()
        options.add_argument("window-size=1400,600")
        from fake_useragent import UserAgent
        ua = UserAgent()
        user_agent = ua.random
        # print(user_agent)
        options.add_argument(f'user-agent={user_agent}')
        
        # driver = webdriver.Chrome(chrome_options=options)
        # driver.get('https://whoer.net/')
        # driver.quit()

        """

        Copyright: You are prohibited from publishing this project in another project
            Code developer Omar_Style_ps

        Contact for inquiries:
            https://t.me/OmarStyle1
        """
        try:
            proxy_host, proxy_port = proxy_address.split(":")
        except ValueError:
            raise ValueError("Please enter the proxy correctly. Example: 95.56.254.139:3128")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--proxy-server={proxy_host}:{proxy_port}')

        if driver_path is None:
            driver = webdriver.Chrome(options=chrome_options,chrome_options=options)
        else:
            driver = webdriver.Chrome(driver_path, options=chrome_options,chrome_options=options)
        driver.get(Link)
        return driver






# pr = BrowsersProxy()
# pr.proxy_firefox("74.249.8.183:3128", "http://whatismyipaddress.com")
# driver = pr.proxy_chrome("95.56.254.139:3128","http://whatismyipaddress.com", driver_path='E:\\chroo\\chromedriver.exe')

