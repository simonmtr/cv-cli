import json

def get_data(path):
    with open(path) as data_file:
        return json.load(data_file)

def get_output_variable(path):
    data = get_data(path)
    return iterate_variable_input(data)

def iterate_variable_input(data, recoutput=''):
    for k, v in data.items():
        if isinstance(v, dict):
            recoutput += iterate_variable_input(v)
        elif isinstance(v, list):
            recoutput += f"\n{k}:\n"
            for value in v:
                recoutput += f"  ->  {value}\n"
        else:
            recoutput += f" -> {k} - {v}\n"
    return recoutput
    

def get_output_preset(path, flags):
    output = ''
    data = get_data(path)
    if flags['urls']:
        output += get_urls(data['urls'])
    if flags['projects']:
        output += get_projects(data['projects'])
    if flags['info']:
        output += get_info(data)
    if flags['skills']:
        output += get_skills(data['skills'])
    if flags['contact']:
        output += data['contact']
    if flags['education']:
        output += get_education(data['education'])
    return output

def get_info(data):
    return f"---\nName: {data['name']}\n---\n---Info: {data['info']}\n---"

def get_urls(data):
    urls = '---\nUrls\n---'
    for url in data:
        urls += url + '\n'
    return urls

def get_projects(data):
    projects = '---\nProjects\n---'
    for project in data:
        projects += 'Name: ' + project['name'] + '\n'
        projects += 'Company: ' + project['company'] + '\n'
        projects += 'Information:' + '\n'
        for info in project['information']:
            projects += info + '\n'
        projects += project['technologies'] + '\n'
        projects += project['link'] + '\n'
        projects += project['startdate'] + '\n'
        projects += project['enddate'] + '\n'
    return projects

def get_experience(data):
    experiences = '---\nExperiences\n---'
    return experiences


def get_skills(data):
    skills = '---\nSkills\n---'
    skills += f"Programming Languages: {data['programminglanguages']}\n"
    skills += f"Technologies: {data['technologies']}\n"
    skills += f"Languages: {data['languages']}\n"
    return skills

def get_education(data):
    educations = '---\nEducation\n---'
    for education in data:
        educations += f"Institute: {education['institute']}\n"
        educations += f"Name: {education['name']}\n"
        educations += f"Degree: {education['degree']}\n"
        educations += f"information: {education['information']}\n"
        educations += f"Focus: {education['focus']}\n"
        educations += f"Start: {education['startdate']}\n"
        educations += f"End: {education['enddate']}\n"
    return educations