import allure
from allure_commons.types import AttachmentType


def screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png,
                  name='page_screenshot_' + browser.driver.session_id,
                  attachment_type=AttachmentType.PNG,
                  extension='.png')


def logs(browser):
    try:
        log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
        allure.attach(body=log,
                      name='browser_logs_' + browser.driver.session_id,
                      attachment_type=AttachmentType.TEXT,
                      extension='.log')
    except Exception:
        pass


def html(browser):
    html = browser.driver.page_source
    allure.attach(body=html,
                  name='page_source_' + browser.driver.session_id,
                  attachment_type=AttachmentType.HTML,
                  extension='.html')


def video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(body=html,
                  name='test_video_' + browser.driver.session_id,
                  attachment_type=AttachmentType.HTML,
                  extension='.html')
