all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:


def filter_colors(item):
    if item["sexy"] == True:
        return item["label"]

def generate_li(item):
    aux = item["label"]
    return "<li>" + aux + "</li>"

sexyColors = list(filter(filter_colors, all_colors))
liColors = list(map(generate_li,  sexyColors))


n=""
print(n.join(liColors))
