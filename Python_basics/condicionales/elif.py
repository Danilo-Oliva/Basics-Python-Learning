ingreso_mensual = 7200000
gasto_mensual = 80000

#If aninados y elif
if ingreso_mensual > 10000:
  if ingreso_mensual - gasto_mensual < 0:
   print("Estas en deficit")
  elif ingreso_mensual - gasto_mensual > 3000:
    print("Estas bien")
  else:
    print("Estas gastando mucho")
    
elif ingreso_mensual > 1000:
  print("Estas bien en latinoamerica")
  
elif ingreso_mensual > 500:
  print("Estas bien en Argentina")
  
elif ingreso_mensual > 200:
  print("Estas bien en Santa Fe")
  
else: 
  print("sos pobre") 
  