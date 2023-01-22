def create(first_name, name, telephone, description):

    xml = '<xml>\n'
    xml += '   <first_name>{}</first_name>\n'\
        .format(first_name)
    xml += '   <name>{}</name>\n'\
        .format(name)
    xml += '   <tel>{}</tel>\n'\
        .format(telephone)
    xml += '   <description>{}</description>\n'\
        .format(description)
    xml += '</xml>\n'

    with open('HW7MVC/phone_book.xml', 'a', encoding="utf-8") as page:
        page.write(xml)

    return xml
