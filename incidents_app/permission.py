from rest_framework.permissions import BasePermission

class IsCitoyen(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role=="Citoyen"
    
class IsAdminstarateur(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role=="Adminstrateur"
    

class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
