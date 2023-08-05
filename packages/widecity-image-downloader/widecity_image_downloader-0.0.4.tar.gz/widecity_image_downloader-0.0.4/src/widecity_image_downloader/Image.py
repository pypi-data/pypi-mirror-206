from simple_image_download import simple_image_download

response = simple_image_download.Downloader



def download(keywords):
    for kw in keywords:
        response().download(kw,2)
        
