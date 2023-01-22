import view
import model
import xml_generator


def main():
    select = view.start()

    if select == 1:
        temp = model.add_contact()
        first_name, name, telephone, description = temp[0], temp[1], temp[2], temp[3]
        model.add_contact_csv(first_name, name, telephone, description)
        model.add_contact_txt(temp)
        xml_generator.create(first_name, name, telephone, description)

    elif select == 2:
        model.get_contact_from_cvs()

    elif select == 3:
        model.get_contact_from_txt()

    elif select == 4:
        model.get_contact_from_xml()

    elif select == 5:
        model.delete_contact()

    elif select == 0:
        exit()
