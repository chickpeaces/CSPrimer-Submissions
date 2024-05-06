import re as regex

def rgb_s(red, green, blue, alph=-1):
    if alph < 0:
        return "rgb({0} {1} {2});".format( red, green, blue)
    
    return "rgba({0} {1} {2} / {3:.5f});".format( red, green, blue, alph)

def css_h_to_rgb( css_hex):
    """
    potentional regexp "#[\da-f]{3,4};|#[\da-f]{6};|#[\da-f]{8};"
    starts with '#', will follow  with 3,4,6, or 8 hex values
    above regexp will still capture 5 & 7 hex values
    
    1. Scrape CSS file for css_h codes (will not pick up non-hex values)
    2. determine if valid css_h codes (not 5 /7  digits)
    3. parse values based on css_h type 
        3 values, shorthand rgb() #r g b 
        4 values, shorthand rgba() #r g b a 
            shorthand values duplicate each byte, #1230 becomes #11223300
        6 values, rgb() #rr gg bb 
        8 values rgb() #rr gg bb aa
    4. convert to decimal and wrap in 'rgb(', ')'
    """
    css_hex_len = len(css_hex)
    if css_hex_len == 5: #three hex digits plus '#' and ';'        
        return rgb_s( 
            red= int( css_hex[1]+css_hex[1], 16), 
            green= int( css_hex[2]+css_hex[2], 16), 
            blue= int( css_hex[3]+css_hex[3], 16)
        )
    
    if css_hex_len == 6: #four hex digits plus '#' and ';'
        return rgb_s( 
            red= int( css_hex[1]+css_hex[1], 16), 
            green= int( css_hex[2]+css_hex[2], 16), 
            blue= int( css_hex[3]+css_hex[3], 16),
            alph= int( css_hex[4]+css_hex[4], 16) / 255.0
        )
    
    if css_hex_len == 8: #three hex digits plus '#' and ';'
        return rgb_s( 
            red= int( css_hex[1:3], 16), 
            green= int( css_hex[3:5], 16),
            blue= int( css_hex[5:7], 16)
        )
        
    if css_hex_len == 10: #four hex digits plus '#' and ';'
        return rgb_s( 
            red= int( css_hex[1:3], 16), 
            green= int( css_hex[3:5], 16),
            blue= int( css_hex[5:7], 16),
            alph= int( css_hex[7:9], 16) / 255.0
        )

    return "invalid css hex value" #css_h string is not 3,4,6, or 8 hex digits
    
def process_css( css_file):
    
    output_file = css_file
    css_h_strs = exp.findall( css_file)
    for string in css_h_strs:
        output_file = output_file.replace( string, css_h_to_rgb(string))
        
    return output_file
    
if __name__ == '__main__':
    
    read_data = []
    expected_data = []
    exp = regex.compile("#[\da-f]{3,4};|#[\da-f]{6};|#[\da-f]{8};", regex.IGNORECASE)
    test_files = [('simple.css', 'simple_expected.css'), ('advanced.css', 'advanced_expected.css')]

    for test_file, expected_file in test_files:
        with open( test_file, 'r') as _file:
            read_data.append( _file.read())
        with open(expected_file, 'r') as _exp_file:
            expected_data.append( _exp_file.read())
    
    for idx in range(len(read_data)):
        assert process_css(read_data[idx]) == expected_data[idx]