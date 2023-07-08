#creamos el carrito como una clase 

class Carro():
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        
        if not carro:
            self.session['carro'] = {}
            self.carro = self.session['carro']
        else:
            self.carro = carro
    
    def agregar_producto(self, producto):
        producto_id = str(producto.id)
        categoria = producto.categoria.nombre
        
        if producto_id not in self.carro.keys():
            self.carro[producto_id]={
                'nombre': producto.nombre,
                'imagen': producto.imange.url,
                'categoria': categoria,
                'cantidad':1,
                'precio': producto.precio
            }
        
        #si ya existe esa key dentro de mi self.carro.keys entonces
        else:
            self.carro[producto_id]['cantidad'] += 1
            self.carro[producto_id]['precio'] += producto.precio
        
        self.guardar_carro()
        
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
        
    def restar_producto(self, producto):
        producto_id = str(producto.id)
        #if producto_id in self.carro.keys():
        self.carro[producto_id]['cantidad'] -= 1
        self.carro[producto_id]['precio'] -= producto.precio
            
        if self.carro[producto_id]['cantidad'] < 1:
            self.eliminar_producto(producto)
        
        self.guardar_carro()
        
    def eliminar_producto(self, producto):
        producto_id = str(producto.id)
        del self.carro[producto_id]
        self.guardar_carro()
        
    def vaciar_carrito(self):
        self.carro = {}
        self.guardar_carro()
        
    def obtener_total(self):
        total = 0
        #iteramos sobre nuestra lista
        for key in self.carro.keys():
            # print(self.carro[key]['precio'])
            total += self.carro[key]['precio']
        return total
                