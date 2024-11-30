import re
from collections import OrderedDict
import csv


def correct_information_table(contact_list: list) -> list:
    contact_list = contact_list.copy()
    for contact in contact_list:
        if len(contact[0].split()) > 2:
            new_contact_elements = contact[0].split()
            contact[0] = new_contact_elements[0]
            contact[1] = new_contact_elements[1]
            contact[2] = new_contact_elements[2]
        elif len(contact[0].split()) == 2:
            new_contact_elements = contact[0].split()
            if len(contact[1].split()) > 0:
                contact[2] = contact[1]
            contact[0] = new_contact_elements[0]
            contact[1] = new_contact_elements[1]
        elif len(contact[1].split()) == 2:
            new_contact_elements = contact[1].split()
            contact[1] = new_contact_elements[0]
            contact[2] = new_contact_elements[1]
    return contact_list


def remove_duplicate_data(contact_list: list) -> list:
    k = 0
    while k < len(contact_list) - 1:
        for list1, list2 in zip(contact_list[k], contact_list[k + 1]):
            if list1 == list2:
                new_list = list(OrderedDict.fromkeys(contact_list[k] + contact_list[k + 1]))
                contact_list.remove(contact_list[k + 1])
                contact_list.remove(contact_list[k])
                contact_list.append(new_list)
            break
        k += 1
    return contacts_list


def formatting_style_number(contact_list: list) -> list:
    for contact in contact_list:
        pattern = re.compile(
            r"(\+7|8)?\s*\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s*\W*)?(доб\.)?(\s*)?(\d*)(\W)?")
        contact[5] = pattern.sub(r"+7(\2)\3-\4-\5 \7\9", contact[5])
    return contact_list


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    correct_information_list = correct_information_table(contacts_list)
    optimized_contact_list = remove_duplicate_data(correct_information_list)
    new_contact_list = formatting_style_number(optimized_contact_list)

    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contact_list)
