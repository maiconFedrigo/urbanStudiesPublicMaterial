import os

def get_svg_content(path):
	with open(path,"r") as doc:
		return doc.read()

def replace_in_svg_content(content,old,new):
	return content.replace(old,new)

def replace_color_in_svg_content(content,old_string,new_string):
	return replace_in_svg_content(content,old_string, new_string)

def replace_number_in_svg_content(content, old_string, new_string):
	return replace_in_svg_content(content, old_string, new_string)

def save_svg(content,path):
	with open(path,"w") as doc:
		doc.write(content)

def create_transformed_icon(path,color_name,color_hex_old,color_hex_new,old_number,new_number,old_num_col,new_num_col):
	old_number = str(old_number)
	new_number = str(new_number)
	content = get_svg_content(path)
	content = replace_number_in_svg_content(content, old_number, new_number)
	content = replace_color_in_svg_content(content,color_hex_old,color_hex_new)
	content = replace_color_in_svg_content(content, old_num_col, new_num_col)
	path_to_save = path.replace('.svg','_' + color_name +'_' + new_number + '.svg')
	save_svg(content,path_to_save)

def create_range_of_icons(path,color_name,color_hex_old,color_hex_new,old_number,start_number,end_number,old_num_col,new_num_col):
	list_of_icon_numbers_to_create = [i for i in range(start_number,end_number+1)]
	for number in list_of_icon_numbers_to_create:
		create_transformed_icon(path,color_name,color_hex_old,color_hex_new,old_number,number,old_num_col,new_num_col)

create_range_of_icons("icons/icon_marker_template.svg","brown","#123456","#800000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","red","#123456","#ff0000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","orange","#123456","#ffa500","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","yellow","#123456","#ffff00","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","olive","#123456","#808000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","purple","#123456","#800080","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","fuschia","#123456","#ff00ff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","white","#123456","#ffffff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","lime","#123456","#00ff00","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","green","#123456","#008000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","navy","#123456","#000080","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","blue","#123456","#0000ff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","aqua","#123456","#00ffff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","teal","#123456","#008080","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","black","#123456","#000000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","silver","#123456","#c0c0c0","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_marker_template.svg","gray","#123456","#808080","REPLACE THIS",1,99,"#654321","#000000")

create_range_of_icons("icons/icon_square_marker_template.svg","brown","#123456","#800000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","red","#123456","#ff0000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","orange","#123456","#ffa500","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","yellow","#123456","#ffff00","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","olive","#123456","#808000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","purple","#123456","#800080","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","fuschia","#123456","#ff00ff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","white","#123456","#ffffff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","lime","#123456","#00ff00","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","green","#123456","#008000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","navy","#123456","#000080","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","blue","#123456","#0000ff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","aqua","#123456","#00ffff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","teal","#123456","#008080","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","black","#123456","#000000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","silver","#123456","#c0c0c0","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_square_marker_template.svg","gray","#123456","#808080","REPLACE THIS",1,99,"#654321","#000000")

create_range_of_icons("icons/icon_flag_template.svg","brown","#123456","#800000","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","red","#123456","#ff0000","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","orange","#123456","#ffa500","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","yellow","#123456","#ffff00","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","olive","#123456","#808000","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","purple","#123456","#800080","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","fuschia","#123456","#ff00ff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","white","#123456","#ffffff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","lime","#123456","#00ff00","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","green","#123456","#008000","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","navy","#123456","#000080","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","blue","#123456","#0000ff","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","aqua","#123456","#00ffff","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","teal","#123456","#008080","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","black","#123456","#000000","REPLACE THIS",1,99,"#654321","#ffffff")
create_range_of_icons("icons/icon_flag_template.svg","silver","#123456","#c0c0c0","REPLACE THIS",1,99,"#654321","#000000")
create_range_of_icons("icons/icon_flag_template.svg","gray","#123456","#808080","REPLACE THIS",1,99,"#654321","#ffffff")


