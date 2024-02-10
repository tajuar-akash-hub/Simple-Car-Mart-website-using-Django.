from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import car_model,purchase
from django.views.generic import DetailView
from posts.forms import Comment_form
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
# def details(request,id):
#     post_id_filter = car_model.objects.filter(id=id)
#     print("printing filted item",post_id_filter)
#     return render(request,"post_details.html",{'post_id_filter':post_id_filter})

@method_decorator(login_required,name='dispatch')
class PostDetailsView(DetailView):
    model = car_model
    pk_url_kwarg='id'
    template_name='post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = Comment_form(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.relation_with_car_model = post
            new_comment.save()
            return redirect("homepage") 
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object() # car model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = Comment_form()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    



def buy_now(request,id):
    filtered_car_model = car_model.objects.get(pk=id)
    if filtered_car_model.quantity > 0:
        filtered_car_model.quantity=filtered_car_model.quantity-1
        filtered_car_model.save()

        purchase_instance = purchase()
        purchase_instance.relation_with_car_model=filtered_car_model
        purchase_instance.relation_with_user=request.user

        purchase_instance.purchased_car_model_name=filtered_car_model.car_name
        purchase_instance.purchased_car_brand_name=filtered_car_model.car_brand_name
        purchase_instance.who_purchased_user_name=request.user
        purchase_instance.save()

    # print("priting purchase isntance",purchace_instance)
    return redirect("post_details",id=id) #redircting using id 




def order_history(request):
    purchase_all_history = purchase.objects.filter(relation_with_user=request.user)
    return render(request,"order_history.html",{'data':purchase_all_history})

   
    

    





    



    



