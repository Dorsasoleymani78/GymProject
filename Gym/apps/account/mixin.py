
from django.http import Http404

 
class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_superuser:
            self.fields=['author','title','slug','category','content','img','published_at','status']
        elif request.user.is_author:
            self.fields=[ 'title','slug','category','content','img','published_at' ]
        else:
            raise Http404("you canot see this page")
        return super().dispatch(request, *args, **kwargs)   
    
class FormValidMixin():
    def form_vaild(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj=form.save(commit=False)
            self.obj.author=self.request.user
            self.obj.status='Draf'
        return super().form_vaild(form)
    
            
 