def reduce_file_path(path):
    path = path.split('/')
    wanted_path = []

    for i in path:
        if i == '..':
            if wanted_path:
                wanted_path.pop()
        elif i != '.' and i != '/':
            wanted_path.append(i)

    return '/' + '/'.join(filter(lambda x: x != '', wanted_path))
