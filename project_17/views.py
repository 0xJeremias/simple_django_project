from curses.ascii import HT
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context


def hello_world(request):
    return HttpResponse(" Hello, world!!. You're at my Django first view.")


def second_view(request):
    return HttpResponse("<br> I got it! This is very easy!!. This is my second view.")


def to_day(request):
    day = datetime.now()
    text_document = f"Today is: <br> {day}"

    return HttpResponse(text_document)


def my_name(self, name, age):
    text_document = f"My name is: <br> {name} <br> My age is: <br> {age}"

    return HttpResponse(text_document)


def calculate_birth_year(self, age):
    current_year = datetime.now().year
    birth_year = current_year - int(age)
    return HttpResponse(f"<br> My birth year is: {birth_year}")


def calculate_age(self, birth_day):
    birth_day = datetime.strptime(birth_day, "%d-%m-%y")
    print(type(birth_day))
    delta_time = datetime.now() - birth_day
    days_by_year = 365.25

    http_response = """
    <br><br>
    I'm {years} years, {months} months, {days} days old.
    """.format(
        years=int(delta_time.days // days_by_year),
        months=int((delta_time.days % days_by_year) // 30),
        days=int((delta_time.days % days_by_year) % 30),
    )
    return HttpResponse(http_response)


def test_template(self):

    my_html = open(
        "/home/jere/Projects/Coder_Python/project_Coder_17/project_17/project_17/templates/template.html"
    )

    my_template = Template(
        my_html.read()
    )  # Se carga en memoria nuestro documento, template
    ##Import template & contex, with: "from django.template import Template, Context"

    my_html.close()  # Close file

    my_context = (
        Context()
    )  # EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    document = my_template.render(
        my_context
    )  # Aca renderizamos la plantilla en documento

    return HttpResponse(document)
