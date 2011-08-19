from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string


@dajaxice_register
def request_points(request):
    dajax = Dajax()

    points = []
    points.append({'lat': 37.41444798751896,
                   'lng': -122.0916223526001,
                   'text': 'Some Site #1'})
    points.append({'lat': 37.412061929307924,
                   'lng': -122.08582878112793,
                   'text': 'Other Site #2'})
    points.append({'lat': 37.41301636171327,
                   'lng': -122.0780611038208,
                   'text': 'Other Site #3'})

    dajax.add_data(points, 'example_draw_points')
    dajax.assign('#example_log', 'value', "3 Points loaded...")
    return dajax.json()


@dajaxice_register
def move_point(request, lat, lng):
    dajax = Dajax()
    message = "Saved new location at, %s, %s" % (lat, lng)
    dajax.assign('#example_log', 'value', message)
    return dajax.json()


@dajaxice_register
def multiply(request, a, b):
    dajax = Dajax()
    result = int(a) * int(b)
    dajax.assign('#result', 'value', str(result))
    return dajax.json()


@dajaxice_register
def randomize(request):
    import random
    dajax = Dajax()
    dajax.assign('#result', 'value', random.randint(1, 10))
    return dajax.json()


@dajaxice_register
def updatecombo(request, option, id):
    if id == 'combo1':
        dajax = Dajax()

        if option == 'sp':
            options = ['Madrid', 'Barcelona', 'Vitoria', 'Burgos']
        elif option == 'fr': 
            options = ['Paris', 'Evreux', 'Le Havre', 'Reims']
        else: 
            options = ['']
        
        out = ""
        for o in options:
            out = '%s<option value="#">%s</option>' % (out, o)
    
        dajax.assign('#combo2', 'innerHTML', out)
        return dajax.json()
    else:
        pass
    

@dajaxice_register
def pagination(request, p):
    from dajaxexamples.examples.views import get_pagination_page
    try:
        page = int(p)
    except:
        page = 1
    items = get_pagination_page(page)
    render = render_to_string('examples/pagination_page.html', {'items': items})

    dajax = Dajax()
    dajax.assign('#pagination', 'innerHTML', render)
    return dajax.json()


@dajaxice_register
def send_form(request, form):
    from forms import ExampleForm

    dajax = Dajax()
    form = ExampleForm(form)

    if form.is_valid():
        dajax.remove_css_class('#my_form input', 'error')
        dajax.alert("This form is_valid(), your username is: %s" % form.cleaned_data.get('username'))
    else:
        dajax.remove_css_class('#my_form input', 'error')
        for error in form.errors:
            dajax.add_css_class('#id_%s' % error, 'error')
    return dajax.json()


@dajaxice_register
def flickr_save(request, new_title):
    dajax = Dajax()
    # Use new_title...
    dajax.script('cancel_edit();')
    dajax.assign('#title', 'value', new_title)
    dajax.alert('Save complete using "%s"' % new_title)
    return dajax.json()
