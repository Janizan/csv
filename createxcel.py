import csv
data = ["Name","Product Name","Product ID","Email id","Address","Phone Number"]
x = [
    ["Janani","Speakers","1a453","janu302000@gmail.com","48/5a, 1st Street, Tuticorin",9657413123],
    ["Gohula","Earphone","4a587","gohula45@yahoo.com","160a,Colony A,Tirunelveli",9453687412],
    ["Anitha","Mic","a135d","anima2@rediffmail.com","H10 Majestic Apartment 1:F,Tenkasi",8963214756],
    ["Dora","Charger Cable","8r6s2","dorach2000@gmail.com","16/01a,First floor,Chennai",7845963214],
    ["Christy","HMT Watch","4d56a","chrisro89@yahoo.com","45k,New Colony,Chennai",9845638745],
    ["Jemi","Clock","4f6c1","jemiru_563@gmail.com","16/06,Electronic City Phase 1,Bangalore",8856398744],
    ["Ruba","Mouse","6r1s5","ruba.789@yahoo.com","1A/2,Old Colony,Chennai",8536948852],
    ["Taylor","Speakers","8fgd3","taylor_r45@gmail.com","Door no: 28,Clever Apartments,Tuticorin",9636974685],
    ["John","Earphone","5g6e2","johnce78@hotmail.com","5/5A,South School Street,Chennai",8879663255],
    ["Vajeeha","Mic","s58r5","vaje_eeha453@hotmail.com","1/5a,1st Street,Tenkasi",9874156382],
]
y = "AprilData.csv"
with open(y,'w')as aprildata:
    z = csv.writer(aprildata)
    z.writerow(data)
    z.writerows(x)

