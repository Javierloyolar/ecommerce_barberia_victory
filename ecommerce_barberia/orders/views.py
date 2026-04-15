from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def add_to_cart(request, product_id):
    """
    Añade un producto al carrito almacenado en la sesión del navegador.
    """
    # 1. Obtener el carrito de la sesión. Si no existe, inicializa un diccionario vacío.
    cart = request.session.get('cart', {})
    
    # 2. Convertir el ID a string (Django guarda las llaves de sesión como strings en JSON)
    p_id = str(product_id)
    
    # 3. Sumar cantidad o inicializar en 1
    if p_id in cart:
        cart[p_id] += 1
    else:
        cart[p_id] = 1
    
    # 4. Guardar los cambios de vuelta en la sesión
    request.session['cart'] = cart
    
    # 5. IMPORTANTE: Notificar a Django que la sesión ha sido modificada manualmente
    request.session.modified = True
    
    # 6. Redirigir a la página anterior (o al catálogo si no hay anterior)
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

def view_cart(request):
    """
    Recupera los productos de la sesión para mostrarlos en el resumen del carrito.
    """
    cart = request.session.get('cart', {})
    items = []
    total = 0
    
    for product_id, quantity in cart.items():
        # Traer el objeto real de la base de datos para obtener nombre, precio e imagen
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        
from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    
    cart[p_id] = cart.get(p_id, 0) + 1
    
    request.session['cart'] = cart
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    
    for p_id, quantity in cart.items():
        product = get_object_or_404(Product, id=p_id)
        subtotal = product.price * quantity
        total += subtotal
        items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        
    return render(request, 'orders/cart_detail.html', {'items': items, 'total': total})