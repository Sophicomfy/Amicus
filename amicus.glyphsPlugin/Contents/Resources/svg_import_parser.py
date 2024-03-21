import xml.etree.ElementTree as ET

def parse_svg(svg_path, print_parsed_data=False):
    try:
        tree = ET.parse(svg_path)
        root = tree.getroot()
        paths = root.findall('.//{http://www.w3.org/2000/svg}path')
        path_data = [path.attrib['d'] for path in paths if 'd' in path.attrib]

        glyph_name = svg_path.split('/')[-1].replace('_refined.svg', '')
        parsed_data = {'glyph_name': glyph_name, 'paths': path_data}

        if print_parsed_data:
            print(f"Glyph Name: {parsed_data['glyph_name']}")
            for i, path in enumerate(parsed_data['paths']):
                print(f"  Path {i+1}: {path}")

        print("Forwarding the following data to svg_import_converter.py:")
        print(parsed_data)

        return parsed_data
    except ET.ParseError as e:
        print(f"Error parsing SVG file {svg_path}: {e}")
        return None