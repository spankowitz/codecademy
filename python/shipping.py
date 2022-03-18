import sys

#package weight
weight = 41.5
charge = 0

# menu
print("Shippin Schitt, LLC Rates:")
print("For a package weighing " + str(weight) + " pounds, it'll cost you...")

# ground shipping
charge = 0
flat = 20

if weight <= 2:
  charge = flat + (1.50 * weight)
elif weight > 2 and weight <= 6:
  charge = flat + (3 * weight)
elif weight > 6 and weight <= 10:
  charge = flat + (4 * weight)
elif weight > 10:
  charge = flat + (4.75 * weight)
else:
  print("Error, invlaid weight of ", weight)

print("Ground shipping: $" + str(charge))

# premium ground shipping
charge = 0
p_shipping = 125.00
charge = p_shipping
print("Premium ground shipping: $" +str(p_shipping))

# drone shipping
charge = 0
d_flat = 0

if weight <= 2:
  charge = d_flat + (4.50 * weight)
elif weight > 2 and weight <= 6:
  charge = d_flat + (9 * weight)
elif weight > 6 and weight <= 10:
  charge = d_flat + (12 * weight)
elif weight > 10:
  charge = d_flat + (14.25 * weight)
else:
  print("Error, invalid weight of  ", weight)

print("Drone shipping: $" + str(charge))
