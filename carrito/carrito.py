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
        self.carro[producto_id]={
            'nombre': producto.nombre
        }
        self.guarda_carro()
        
    def guarda_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
        pass
    def eliminar_producto(self, producto):
        self.carro.remove(producto)
        self.guarda_carro()
        
    def vaciar_carrito(self):
        self.carro = {}
        
    def obtener_total(self):
        total = 0
        #iteramos sobre nuestra lista
        for producto in self.carro:
            total += producto.precio
        return total
                