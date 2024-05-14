def get_population(country):
    
    keys = ['col', 'bol']
    values = [300, 400]
    
    return keys, values

def population_by_country(data, country):

    result = list(filter(lambda item: item['Country/Territory'] == country, data))

    return result

