class ConfiguracionGlobal:
    _instancia = None

    def new(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().new(cls)
        
        return cls._instancia

    def init(self):
        self.modo_oscuro = True

print("--- Probando Ejercicio 6 ---")

configuracion1 = ConfiguracionGlobal()
configuracion2 = ConfiguracionGlobal()

configuracion1.modo_oscuro = False

print("¿configuracion1 y configuracion2 son exactamente el mismo objeto?")

if configuracion1 is configuracion2:
    print("¡Sí! El patrón Singleton funciona correctamente (is devolvió True).")
else:
    print("No, son diferentes (algo salió mal).")

print(f"ID en memoria de configuracion1: {id(configuracion1)}")
print(f"ID en memoria de configuracion2: {id(configuracion2)}")

print(f"Valor de 'modo_oscuro' desde configuracion1: {configuracion1.modo_oscuro}")