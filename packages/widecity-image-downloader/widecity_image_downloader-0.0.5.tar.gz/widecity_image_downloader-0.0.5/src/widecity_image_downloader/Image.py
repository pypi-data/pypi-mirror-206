from simple_image_download import simple_image_download
simp=simple_image_download.Downloader() 
simp.directory = 'widecity_Downloader/'
def download(keyword, limit):
    simp.download(keywords=keyword,limit=limit)

