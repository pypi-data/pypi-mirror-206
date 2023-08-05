from simple_image_download import simple_image_download

response = simple_image_download.Downloader
keywords = ['flowers']

class Images:
    def download():
        for kw in keywords:
            response().download(kw,2)
            
