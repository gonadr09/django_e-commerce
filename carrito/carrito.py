class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get('carrito')
        if not carrito:
            carrito = self.session["carrito"] = {}
        #else:
        self.carrito = carrito

    def agregarProducto(self, producto):
        if(str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id] = {
                "id":producto.id,
                "nombre":producto.titulo,
                "precio":str(producto.precio),
                "imagen": producto.imagen.url,
                "cantidad": 1,
            }
        else:
            #self.carrito[producto.id]["cantidad"] = self.carrito[producto.id]["cantidad"] + 1  #mi propuesta
            for key, value in self.carrito.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad'] + 1
                    value['precio'] = float(value['precio']) + producto.precio 
                    break
        self.actualizarCarrito()
    
    def eliminarProducto(self, producto):
        producto.id = str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.actualizarCarrito()

    def restarProducto(self, producto):
        for key, value in self.carrito.items():
            if key == str(producto.id):
                value['cantidad'] = value['cantidad'] - 1
                value['precio'] = float(value['precio']) - producto.precio 

                if value['cantidad'] < 1:
                    self.eliminarProducto(producto) 
                break
        self.actualizarCarrito()

    def vaciarCarrito(self):
        self.session["carrito"] = {}
        self.session.modified = True

    def actualizarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True