def row_to_prompt(row,
                  row_columns):
    
    string = ''
    
    for column, response in zip(row_columns, row[row_columns]):
        new_string = f'{column.replace("_"," ")}\n{response}\n\n'
        string += new_string
        
    return string