def ground_shipping(weight):
  if weight <= 2:
    cost = 1.50
  elif (weight >=2) and (weight <=6):
    cost = 3.00
  elif (weight >=6) and (weight <= 10 ):
    cost = 4.00
  else:
    cost = 4.75
  price = cost*weight + 20
  return price

def premium_ground_shipping(weight):
  premium_ground_shipping = 125.00
  price = premium_ground_shipping
  return price

def drone_shipping(weight):
  if weight <= 2:
    cost = 4.50
  elif (weight >=2) and (weight <=6):
    cost = 9.00
  elif (weight >=6) and (weight <= 10 ):
    cost = 12.00
  else:
    cost = 14.25
  price = cost*weight
  return price



def predictor(weight):
  drone = drone_shipping(weight)
  ground = ground_shipping(weight)
  prem_ground = premium_ground_shipping(weight)
  if (drone < ground) and (drone < prem_ground):
    return "Drone shipping is cheap and it costs: "+ str(drone)
  elif (prem_ground > ground) and (ground < drone):
    return "Ground shipping is cheap and it costs: "+str(ground)
  elif (prem_ground < ground) and (drone > prem_ground):
    return "Premium Ground shipping is cheap and it costs: "+ str(prem_ground)
  else:
    return "Similar Price go with any thing"

print(predictor(17))
print(predictor(4.8))
print(predictor(41.5))
  
    
  
    

