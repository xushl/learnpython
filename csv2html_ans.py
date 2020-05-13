import sys
def main():
    maxwidth,num_format=process_options()
    print_start() 
    count = 0 
    while True: 
        try: 
            line = input() 
            if count == 0: 
                color = "lightgreen" 
            elif count % 2: 
                color = "white" 
            else: 
                color = "lightyellow"
            print_line(line, color, maxwidth,num_format) 
            count += 1 
        except EOFError: 
            break 
    print_end()

def print_start(): 
    print("<table border='1'>")

def print_end(): 
    print("</table>")

def print_line(line, color, maxwidth,num_format): 
    print("<tr bgcolor='{0}'>".format(color)) 
    fields = extract_fields(line) 
    for field in fields: 
        if not field: 
            print("<td></td>") 
        else: 
            number = field.replace(",", "") 
            try: 
                x = float(number) 
                print("<td align='right'>"+num_format.format(round(x))+"</td>") 
            except ValueError: 
                field = field.title() 
                field = field.replace(" And ", " and ") 
                if len(field) <= maxwidth: 
                    field = escape_html(field) 
                else: 
                    field = "{0} ...".format( escape_html(field[:maxwidth])) 
                print("<td>{0}</td>".format(field)) 
    print("</tr>")
def process_options():
    maxwidth = 100
    num_format = '{0:.0f}' 
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help','-h']:
            print('''usage: 
csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html

maxwidth is an optional integer; if specified, it sets the maximum 
number of characters that can be output for string fields, 
otherwise a default of 100 characters is used.

format is the format to use for numbers; if not specified it 
defaults to ".0f".''')
            sys.exit()
        else:
            for i in sys.argv[1:]:
                word_list=i.split('=')
                if word_list[0] == 'maxwidth':
                    maxwidth=int(word_list[1])
                if word_list[0] == 'format':
                    num_format = "{0:"+word_list[1]+"}"
    return maxwidth,num_format
        
def extract_fields(line): 
    fields = [] 
    field = "" 
    quote = None 
    for c in line: 
        if c in "\"'": 
            if quote is None: # start of quoted string 
                quote = c 
            elif quote == c: # end of quoted string 
                quote = None 
            else: 
                field += c # other quote inside quoted string 
            continue 
        if quote is None and c == ",": # end of a field 
            fields.append(field) 
            field = "" 
        else: 
            field += c # accumulating a field 
    if field: 
        fields.append(field) # adding the last field 
    return fields 

def escape_html(text): 
    text = text.replace("&", "&amp;") 
    text = text.replace("<", "&lt;") 
    text = text.replace(">", "&gt;") 
    return text 



main()