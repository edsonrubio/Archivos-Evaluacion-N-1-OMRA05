#clasificador de ACL estandar o extendida
aclNum = int(input("Cual es el número IPV4 ACL? "))
if aclNum >= 1 and aclNum <= 99:
 print("Este es un ACL IPv4 estándar.")
elif aclNum >=100 and aclNum <= 199 or aclNum >=2000 and aclNum <= 2699:
 print("Este es una ACL IPv4 extendida")
else:
 print("Esta ACL IPv4 no corresponde a una lista de acceso .")
