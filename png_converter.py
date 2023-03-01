from html2image import Html2Image
hti = Html2Image()
with open('icons\\teste.html') as f:
    hti.screenshot(f.read(), save_as='icons\\teste.png')










#
# import imgkit
#
# imgkit.from_file('icons/teste.html', 'icons/teste.png')