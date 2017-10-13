from django.contrib.auth.decorators import login_required
from splunkdj.decorators.render import render_to

@render_to('presenter:use_case_example/main.html')
@login_required
def main(request):

    context = {}

    return context
