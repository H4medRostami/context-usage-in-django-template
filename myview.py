from django.shortcuts import render_to_response
from django.template import RequestContext

def custom_proc(request):
  return{
  'app':'myapp'
  'user':request.user
  'ip_address':request.META['REMOTE_ADDR']}
  
  def view_1(request):
  #some code
    return render_to_response(template1.html,
    {'message':'i'm view 1 :)'},
    context_instance=RequestContext(request, processors=[custom_proc]))
    
    def view_2(request):
  #some code
    return render_to_response(template2.html,
    {'message':'i'm view 2 :)'},
    context_instance=RequestContext(request, processors=[custom_proc]))
