import fitz
from svglib import svglib
from reportlab.graphics import renderPDF
import os

def export_svg_as_png(svg_path, png_path):
	# Convert svg to pdf in memory with svglib+reportlab
	# directly rendering to png does not support transparency nor scaling
	drawing = svglib.svg2rlg(path=svg_path)
	pdf = renderPDF.drawToString(drawing)

	# Open pdf with fitz (pyMuPdf) to convert to PNG
	doc = fitz.Document(stream=pdf)
	pix = doc.load_page(0).get_pixmap(alpha=True, dpi=72)
	pix.save(png_path)
def validate_output_folder(folder):
	if not os.path.exists(folder+"/png"):
		os.makedirs(folder+"/png")
		return folder+"/png"
	return folder+"/png"


folderpath = 'icons/' # COLOQUE AQUI O CAMINHO PARA FAZER A EXPORTAÇÃO ADEQUADA

if folderpath[-1] != "/":
	folderpath = folderpath + "/"

svg_files_path = [folderpath+i for i in os.listdir(folderpath) if i.endswith(".svg")]
png_files_names = [folderpath+"png/"+i.replace(".svg",".png") for i in os.listdir(folderpath) if i.endswith(".svg")]
for svg_file_path,png_file_path in zip(svg_files_path,png_files_names):
	export_svg_as_png(svg_file_path,png_file_path)


# print(png_files_names)


