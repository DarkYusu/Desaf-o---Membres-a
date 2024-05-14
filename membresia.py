from abc import ABC, abstractmethod

class Membresia(ABC):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        self._correo_suscriptor = correo_suscriptor
        self._numero_tarjeta = numero_tarjeta

    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia):
        pass

    def cancelar_suscripcion(self):
        return Gratis(self._correo_suscriptor, self._numero_tarjeta)

    def _crear_nueva_membresia(self, nueva_membresia: int):
        if nueva_membresia == 1:
            return Basico(self._correo_suscriptor, self._numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self._correo_suscriptor, self._numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self._correo_suscriptor, self._numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self._correo_suscriptor, self._numero_tarjeta)


class Gratis(Membresia):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 0
        self.max_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self


class Basico(Membresia):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 3000
        self.max_dispositivos = 2

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [2, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self


class Familiar(Membresia):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 5000
        self.max_dispositivos = 5
        self.dias_regalo = 7

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 3, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self

    def modificar_control_parental(self):
        pass  # Implementación futura


class SinConexion(Membresia):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 3500
        self.max_dispositivos = 2
        self.dias_regalo = 7

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 4]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self

    def incrementar_contenido_disponible(self):
        pass  # Implementación futura


class Pro(Membresia):
    def __init__(self, correo_suscriptor, numero_tarjeta):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.costo = 7000
        self.max_dispositivos = 6
        self.dias_regalo = 15

    def cambiar_suscripcion(self, nueva_membresia):
        if nueva_membresia in [1, 2, 3]:
            return self._crear_nueva_membresia(nueva_membresia)
        return self

    def modificar_control_parental(self):
        pass  # Implementación futura

    def incrementar_contenido_disponible(self):
        pass  # Implementación futura
