use ecommerce;

create table Customer(
cust_id int primary key,
email varchar(30),
password varchar(30),
phoneNum bigint,
cust_name varchar(30)
);

create table ordering(
customer_id int primary key,
order_id int,
order_date date,
shipmentDate date,
shipperId int
);

create table order_details(
orderID int primary key,
productId int,
unitPrice bigint,
quantity int,
orderNumber int,
discount bigint
);

create table shipper(
shipperID int primary key,
phonenum bigint,
companyName varchar(30),
shippername varchar(30)
);

create table billingInfo(
billingId int primary key,
billing_address varchar(60),
paymenttype varchar(30),
paymentID int
);

create table category(
categoryId int primary key,
categoryName varchar(30),
description varchar(70)
);

create table product(
productId int primary key,
productname varchar(40),
productDescription varchar(50),
unitPrice bigint,
discount bigint,
Quantityperunit int
);

create table admin(
adminId int primary key,
adminname varchar(30),
adminpasswd varchar(30)
);

create table supplier(
suppId int primary key,
contactId int,
contactname varchar(30),
companytitle varchar(30)
);

create table cart(
cartId int primary key,
totalprice bigint,
NoofProducts int
);
