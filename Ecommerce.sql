use ecommerce;

insert into customer values(1020, 'asp@gmail.com', 'ASP123', 9766824513, 'ASP');
insert into customer values(1021, 'george@gmail.com', 'georgekelly', 9136264579, 'GEO');
insert into customer values(1022, 'posting@gmail.com', 'post123', 9763148562, 'POST');
insert into customer values(1023, 'best123@gmail.com', 'bestest', 9713256478, 'BEST');
insert into customer values(1024, 'small@gmail.com', 'biggie', 6479236812, 'TALL');
insert into customer values(1025, 'smart@gmail.com', 'smart123', 631297895, 'SMART');
insert into customer values(1026, 'rajeev@gmail.com', 'rajeev456', 647926894, 'RJ');
insert into customer values(1027, 'karunakaran@gmail.com', 'karun', 986312478, 'KK');
insert into customer values(1028, 'ismail@gmail.com', 'mailmail', 197821567, 'ISMAIL');

select * from customer;

insert into ordering values(100,4660,'2020-10-12','2020-10-14', 4529);
insert into ordering values(101,4661,'2020-10-15','2020-10-17', 3562);
insert into ordering values(102,4662,'2020-10-18','2020-10-20', 2945);
insert into ordering values(103,4663,'2020-10-21','2020-10-22', 5429);
insert into ordering values(104,4664,'2020-10-23','2020-10-25', 4623);

select * from ordering;

insert into order_details values(1028, 46623, 4500, 1, 769, 0);
insert into order_details values(1029, 56213, 8500, 1, 770, 0);
insert into order_details values(1030, 69315, 7000, 1, 771, 0);
insert into order_details values(1031, 62314, 5600, 1, 772, 0);
insert into order_details values(1032, 56891, 7200, 2, 773, 0);

select * from order_details;

insert into shipper values(1052, 9563286926, 'Bluedart', 'Samuel'); 
insert into shipper values(1053, 9568694213, 'Flipkart', 'Emmanuel'); 
insert into shipper values(1054, 9236987412, 'Amazon', 'Ron'); 
insert into shipper values(1055, 9156987632, 'BigBasket', 'Andrew'); 

select * from shipper;

insert into billingInfo values(6204, 'Hyderabad', 'Debit card', 5602);
insert into billingInfo values(6205, 'Delhi', 'Credit card', 2604);
insert into billingInfo values(6206, 'Kolkata', 'COD', 2036);
insert into billingInfo values(6207, 'Banglore', 'Debit card', 9201);

select * from billingInfo;

insert into category values(1234, 'Mobile', 'Android devivce');
insert into category values(4562, 'Clothes', 'For kids');
insert into category values(1532, 'TV', 'Smart TV');
insert into category values(2364, 'Earphones', 'Used for electronics');

select * from category;

insert into product values(46523, 'Sony Bravia', 'A smart TV', 65000, 5000, 1);
insert into product values(65489, 'Realme X', 'An Android Phone', 17000, 2500, 1);
insert into product values(68945, 'Samsung SCX3200', 'Laser Printer', 34000, 7500, 1);
insert into product values(62149, 'MI A3', 'Smartphone', 9900, 200, 1);

select * from product;

insert into admin values(1652, 'Shekhar','skr123');
insert into admin values(1347, 'Swamy','swamy007');
insert into admin values(1422, 'Reddy','Reddy456');

select * from admin;

insert into supplier values(987, 456, 'Rajasekhar', 'Amazon');
insert into supplier values(653, 123, 'Ramakrishna', 'Quickr');
insert into supplier values(159, 621, 'Viswanath', 'Flipkart');
insert into supplier values(673, 154, 'Karthik', 'OLX');

select * from supplier;

insert into cart values(645, 73000, 12);
insert into cart values(221, 67000, 10);
insert into cart values(267, 93250, 15);
insert into cart values(364, 83400, 14);

select * from cart;