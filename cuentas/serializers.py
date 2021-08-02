from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Perfiles, Comentarios_publicacion, Categorias, Articulos

#Serializadores

"""
    Clases serializadoras, toman el modelo y retornan la data en fomato Json
"""
class UserSerializer(serializers.ModelSerializer):
    """
        Serializador de usuarios que es manejado por django
    """
    class Meta:
        model = User
        fields = ('id','first_name','last_name','email','username','password','is_superuser')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('first_name','last_name','email','username')

class PerfilesSerializer(serializers.ModelSerializer):
    """
        Serializador de los perfiles de los usuarios
    """
    class Meta:
        model = Perfiles
        fields = ('id', 'foto', 'genero', 'biografia', 'fecNacimiento', 'rol', 'estatus', 'direccion','url_website', 'url_twitter','url_instagram','url_facebook')


class PerfilesConDatosUsuarioSerializer(serializers.ModelSerializer):
    """
        Serializador de los perfiles con el usuario 
    """
    usuario = UserGetSerializer(read_only=True)
    class Meta:
        model = Perfiles
        fields = '__all__'


class ArticulosSerializer(serializers.ModelSerializer):
    """
        Serializador de los comentarios que realiza un usuario
    """
    class Meta:
        model = Articulos
        fields = '__all__'


class ComentariosSerializer(serializers.ModelSerializer):
    """
        Serializador de los comentarios que realiza un usuario
    """
    perfil = PerfilesConDatosUsuarioSerializer(read_only=True)
    class Meta:
        model = Comentarios_publicacion
        fields = '__all__'

class ComentariosSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios_publicacion
        fields = '__all__'

"""class PublicacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicaciones
        fields = ('id', 'usuario', 'perfil', 'titulo', 'publicacion', 'creado', 'modificado', 'url', 'vistas', 'categoria')
"""
        
class CategoriasSerializer(serializers.ModelSerializer):
    """
        Serializador de las categorias de las publicaciones
    """
    class Meta:
        model = Categorias
        fields = ('id', 'nombre')

        