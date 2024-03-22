from svg_import_loader import SVGImportLoader
from svg_import_parser import parse_svg
from svg_import_converter import convert_svg_path_to_glyphs_nodes
from svg_import_distributor import distribute_converted_data

def batch_process_svgs(folder_path):
    svg_files = SVGImportLoader().load_svg_files_from_folder(folder_path)
    
    if not svg_files:
        print("No refined SVG files to process.")
        return

    for file_path in svg_files:
        print(f"Processing: {file_path}")
        parsed_data = parse_svg(file_path, print_parsed_data=True)
        if parsed_data:
            converted_data = convert_svg_path_to_glyphs_nodes(parsed_data)
            distribute_converted_data(converted_data)  # Bind the distributor here
            print(f"Successfully processed: {file_path.split('/')[-1]}")
        else:
            print(f"Failed to parse: {file_path}")

    print("Batch import process completed.")