first_names = ['Levi', 'Matthias', 'Irene', 'Annie', 'Mary', 'David', 'Daniel',
                'Jeanie', 'Methuselah', 'Nebuchadnezzar', 'Jedediah', 'John',
                'Eli', 'Noah', 'Samuel', 'Sarah', 'Rebecca', 'Anna', 'Susanna',
                'Hannah', 'Susan', 'Elizabeth', 'Rachael', 'Moses']
last_names = ['Yoder', 'Stoltzfus', 'Martin', 'Reimer', 'Berg',
                'Friesen', 'Longachre', 'Lehman', 'Miller', 'Weaver', 'Weber',
                'Horst', 'Hurst', 'Kauffman', 'Hostetler', 'Good', 'Shenk',
                'Brubaker', 'Landis', 'Zehr', 'Garber', 'Roth', 'Mast', 'Wenger',
                'Bontrager', 'Burkholder', 'Peachey', 'Shrock', 'Zimmerman']

self.nickname = (first_names.pop(random.randint(0, len(first_names) - 1)) +
" " + last_names.pop(random.randint(0, len(last_names) - 1)) + '-' +
last_names.pop(random.randint(0, len(last_names) - 1)))
