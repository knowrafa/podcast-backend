from django.utils.safestring import mark_safe


def table_template(dictionary, name='Nome', value='Valor'):
    """
    Create a table, based in dictionary
    """
    html_string = '<table>' \
                  '<thead>' \
                  '<tr>' \
                  '<th> {} </th>' \
                  '<th> {} </th>' \
                  '</tr>' \
                  '</thead>' \
                  '<tbody style="overflow-: auto;">'.format(name, value)
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            html_string += '</tr>' \
                           '<td>{}</td>' \
                           '<td>{}</td>' \
                           '</tr>'.format(key, value)
    html_string += '</tbody>' \
                   '</table>'
    return mark_safe(html_string)
