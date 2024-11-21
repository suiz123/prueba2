import bcrypt
 
class Autenticacion:
    """
    Módulo de autenticación sencilla.
    """
    def __init__(self):
        # Diccionario que almacena los usuarios y sus contraseñas.
        self.usuarios = {"admin": "1234", "user":"password")}
 
    def verificar_credenciales(self, usuario, contrasena):
        """
        Verifica si las credenciales son válidas.
        :param usuario: Nombre del usuario.
        :param contrasena: Contraseña del usuario.
        :return: True si las credenciales son válidas, False en caso contrario.
        """
        if usuario in usuarios and contraseña.encode() == usuarios[usuario]): 
          return True 
        return False
