# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
# ,and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?

no_of_potato_chips_packets = 9
each_packet_cost = 1.49
amount_to_shopkeeper = 20

total_purchase_cost = each_packet_cost * no_of_potato_chips_packets
print("Total Purchase Cost: ", total_purchase_cost)

amount_return_from_shopkeeper = amount_to_shopkeeper-total_purchase_cost
print("Amount shopkeeper to return back", amount_return_from_shopkeeper)
