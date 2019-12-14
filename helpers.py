def fix_name(name):
    for c in ['\\', '/', ':', '*', '?', '"', '<', '>', '|']:
        if c in name:
            name = name.replace(c, '')
    name = name.strip('.').strip(' ')
    return name