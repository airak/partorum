def extract(document):
    clippings = split_document(document)
    # criar uma lista de objetos aqui
    for clipping in clippings:
        name, author, page, position, date, content = extract_clipping(clipping)
        # implementar aqui o retorno de um objeto
        print('#{}#{}#{}#{}#{}#'.format(name, author, page, position, date))
    return
    
def extract_clipping(clipping):
    header, content = split_clipping(clipping)
    name, author, page, position, date = split_header(header)
    return name, author, page, position, date, content

def split_document(document):
    return document.split("==========\n")

def split_clipping(clipping):
    part = clipping.split("\n\n")
    header = part[0]
    content = "none"
    if len(part) > 1:
        content = part[1]
    return header, content

def split_header(header):
    part = header.split("\n")
    name_author = part[0].split("(")
    name = name_author[0]
    author = "None"
    page = "None"
    position = "None"
    date = "None"
    if len(name_author) > 1:
        author = name_author[1].replace(")","")

    if len(part) > 1:
        page_position_date = part[1].split(" | ")

        if len(page_position_date) == 3:
            page = page_position_date[0].split(" ")[-1]
            position = page_position_date[1].split(" ")[-1]
            date = page_position_date[2].split(",")[-1]

        if len(page_position_date) == 2:
            page = "-"
            position = page_position_date[0].split(" ")[-1]
            date = page_position_date[1].split(",")[-1]

    return name.strip(), author.strip(), page.strip(), position.strip(), date.strip()

def main():
    f = open("My Clippings.txt", "r")
    document = f.read()
    extract(document)

if __name__ == "__main__":
    main()