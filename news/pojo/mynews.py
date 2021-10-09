'''
这里放我们的实体类
数据表--class对应
'''


class News():
    def __init__(self, id=0, title=None, author=None, create_date=None, description=None, text=None, category_id=None):
        self.id = id
        self.title = title
        self.author = author
        self.create_date = create_date
        self.description = description
        self.text = text
        self.category_id = category_id
        # self.category=category

    def __str__(self):
        return f'id:{self.id}\ttitle:{self.title}\tauthor:{self.author}' \
               f'\tdate:{self.create_date}\tdescription:{self.description}\t' \
               f'text:{self.text}\tcategory_id:{self.category_id}'


class Categorys():
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id:{self.id}\ttitle:{self.name}'


class Comments():
    def __init__(self, id=0, title=None, text=None, createDate=None, createUser_id=None, new_id=None):
        self.id = id
        self.title = title
        self.text = text
        self.createDate = createDate
        self.createUser_id = createUser_id
        self.new_id = new_id

    def __str__(self):
        return f'id:{self.id}\ttitle:{self.title}\ttext:{self.text}' \
               f'\tcreateDate:{self.createDate}\tcreateUser_id:{self.createUser_id}\t' \
               f'new_id:{self.new_id}'


class Users():
    def __init__(self, id=0, name=None, phone=None, gender=None, birthday=None, province=None, city=None,
                 district=None, id_card_number=None, email=None, password=None, state=0):
        self.id = id
        self.name = name
        self.phone = phone
        self.gender = gender
        self.birthday = birthday
        self.province = province
        self.city = city
        self.district = district
        self.id_card_number = id_card_number
        self.email = email
        self.password = password
        self.state = state

    def __str__(self):
        return f'id:{self.id}\tname:{self.name}\tphone:{self.phone}' \
               f'\tgender:{self.gender}\tbirthday:{self.birthday}\t' \
               f'province:{self.province}\tcity:{self.city}\t' \
               f'district:{self.district}\tid_card_number:{self.id_card_number}\t' \
               f'email:{self.email}\tpassword:{self.password}\tstate:{self.state}'


class UserNews():
    def __init__(self, id=0, users_id=None, new_id=None):
        self.id = id
        self.users_id = users_id
        self.new_id = new_id

    def __str__(self):
        return f'id:{self.id}\tusers_id:{self.users_id}\tnew_id:{self.new_id}'


class Labels():
    def __init__(self, id=0, name=None):
        self.id = id
        self.name = name

    def __str__(self):
        return f'id:{self.id}\tname:{self.name}'


class NewsLabels():
    def __init__(self, id=0, new_id=None, label_id=None):
        self.id = id
        self.new_id = new_id
        self.label_id = label_id

    def __str__(self):
        return f'id:{self.id}\tnew_id:{self.new_id}\tlabel_id:{self.label_id}'


class Fnames():
    def __init__(self, id=0, fname=None, new_id=None):
        self.id = id
        self.fname = fname
        self.new_id = new_id

    def __str__(self):
        return f'id:{self.id}\tfname:{self.fname}\tnew_id:{self.new_id}'
