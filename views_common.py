#coding: utf-8

def create_grid(list_data, list_metadata):
    #grid = '<table class="table table-striped table-hover">'
    grid = '<thead>'
    
    for titulo in list_metadata:
        grid += '   <td>%s</td>' % titulo
    
    grid += '<td>Edit</td>'
    grid += '<td>Delete</td>'

    grid += '</thead>'
    grid += '<tbody>'

    if len(list_data) > 0:
        for fields in list_data:
            grid += '   <tr>'
            
            for field in fields:            
                grid += '       <td>%s</td>' % field
                
            grid += '       <td><a href="#"><i class="icon-edit"></i></a></td>'
            grid += '       <td><a href="#"><i class="icon-trash"></i></a></td>'
            grid += '   </tr>'

    else:
        grid += '<tr><td colspan="6">Nenhum registro cadastrado</td></tr>'


    grid += '</tbody>'
    #grid += '</table>'
    return grid