from selenium import webdriver
import config, time


def before_feature(context, feature):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.accept_untrusted_certs = True
    chrome_options.assume_untrusted_cert_issuer = True
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-impl-side-painting")
    # chrome_options.add_argument("--disable-setuid-sandbox")
    # chrome_options.add_argument("--disable-seccomp-filter-sandbox")
    # chrome_options.add_argument("--disable-breakpad")
    # chrome_options.add_argument("--disable-client-side-phishing-detection")
    # chrome_options.add_argument("--disable-cast")
    # chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
    # chrome_options.add_argument("--disable-cloud-import")
    # chrome_options.add_argument("--disable-popup-blocking")
    # chrome_options.add_argument("--ignore-certificate-errors")
    # chrome_options.add_argument("--disable-session-crashed-bubble")
    # chrome_options.add_argument("--disable-ipv6")
    # chrome_options.add_argument("--allow-http-screen-capture")
    #chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--remote-debugging-port=9230")
    chrome_options.binary_location = "C:\\Program Files (x86)\\B2B Soft\\Wireless Standard\\ws_core.exe"

    chrome_options.add_experimental_option(name="debuggerAddress", value="127.0.0.1:9230")
    chrome_options.debugger_address = "127.0.0.1:9230"


    # chrome_options.add_argument("--headless")

    context.driver = webdriver.Chrome(executable_path=config.chromedriver, chrome_options=chrome_options)
    #context.driver = webdriver.Firefox(executable_path=config.geckodriver)
    # context.driver = webdriver.Remote(command_executor='http://kv-wws-teamcity.qa.b2bsoft.com:4444/wd/hub', options=chrome_options)
    # context.driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=chrome_options)
    # time.sleep(3)