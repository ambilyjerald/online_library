
def add_book(request):
    current_user=request.user
    seller_object=Seller.objects.get(user=current_user)
    data=mobileproduct_form()
    if request.method=="POST":
        data=mobileproduct_form(request.POST,request.FILES)
        if data.is_valid():
            product= data.save(commit=False)
            product.seller = seller_object
            product.save()
            return redirect("product_table")
    return render(request,"seller_dash/mobileproduct.html",{'data':data})
