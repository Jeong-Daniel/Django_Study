from django.shortcuts import render
#from django.views.generic import ListView, Templateview
from django.template.context_processors import csrf
from boardapp.models import Boards

# Create your views here

#class BoardsListClassView(ListView):
#	model = Boards

#class BoardsTemplateClassView(TemplateView):
#	template_name = "template.html"

#	def get_context_data(self, **kwargs):
#		context = super().get_context_data(**kwargs)
#		context['list'] = Boards.objdets.all()
#		return context

def BoardsFunctionView(request):
    boardList = Boards.objects.all()
    return render(request, 'boardsfunctionview.html', {'boardList':boardList})

def memberRegisterFormPage(request):
    args={}
    args.update(csrf(request))
    return render(request, 'member_register_form.html',args)

