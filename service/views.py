from django.shortcuts import render,redirect
from .models import Item, SubItem
from .form import ItemForm,SubItemForm

# Create your views here.

def welcome(request):
    return render(request,'base.html')

# categories=Category.objects.filter(parent=None)
#     if parent_or_child is None:
#         products=Product.objects.all()
#
#     elif parent_or_child == 'child':
#         sub_cat=SubCategory.objects.get(pk=pk)
#         products=sub_cat.product_set.all()
#     elif parent_or_child == 'parent':
#         products=[]
#         sub_cats= Category.objects.get(pk=pk).children.all()
#         for sub_cat in sub_cats:
#             prds=sub_cat.product_set.all()
#             products+=prds
#     else:
#         products=[]




def show(request):
    item=Item.objects.all
    return render(request,'show.html',{'item':item})

def load_form(request):
    form=ItemForm
    return render(request,"itemForm.html",{'form':form})

def addItem(request):
    form=ItemForm(request.POST,request.FILES)
    form.save()
    return redirect('/show')


# for category

def showCat(request,parent_or_child=None,pk=None):

        if parent_or_child is None:
            subItem=SubItem.objects.all()

        elif parent_or_child == 'child':
            item=Item.objects.get(pk=pk)
            subItem=item.children.all()
        else:
            subItem=[]


        return render(request, 'showCategory.html', {'subItem': subItem, 'selected_pk': pk})

        # subItem=SubItem.objects.all

#
def load_cat_form(request):
    form=SubItemForm
    return render(request,"subItemForm.html",{'form':form})
#
def addsubItem(request):
    form=SubItemForm(request.POST,request.FILES)
    form.save()
    return redirect('/show')



# edit/update

def editItem(request,id):
    item=Item.objects.get(id=id)
    return render(request,'editItem.html',{'item':item})

def updateItem(request, id):
    item = Item.objects.get(id=id)
    form=ItemForm(request.POST,request.FILES, instance=item)
    form.save()
    return redirect('/show')
