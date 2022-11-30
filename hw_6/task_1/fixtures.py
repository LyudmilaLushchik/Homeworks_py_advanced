fixture_check_doc_existance = [
    ('10006', True),
    ('12345678', False)
]

fixture_get_doc_owner_name = [
    ('11-2', 'Геннадий Покемонов'),
    ('10006', 'Аристарх Павлов')
]
 
fixture_get_all_doc_owners_names = {
    'Василий Гупкин',
    'Геннадий Покемонов',
    'Аристарх Павлов'
}

fixture_show_doc_info = [
    ({"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}, 'insurance "10006" "Аристарх Павлов"'),
]

fixture_get_doc_shelf = [
    ('11-2', '1'),
    ('00', None)
]

fixture_add_new_doc = [
    ('555', 'insurance', 'Иван Иванов', '3', '3')
]

fixture_delete_doc = [
    ('555', ('555',True)),
    ('1234', None)
]

fixture_remove_doc_from_shelf = [
    ('5455 028765', True),
    ('111', None)
]

fixture_add_new_shelf = [
    ('5', ('5', True)),
    ('2', ('2', False))
]