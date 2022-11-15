# Defining CIDR Block for VPC
variable "vpc_cidr" {
  default = "10.100.0.0/16"
}
# Defining CIDR Block for 1st Subnet
variable "subnet_cidr" {
  default = "10.100.1.0/24"
}
# Defining CIDR Block for 2nd Subnet
variable "subnet1_cidr" {
  default = "10.100.2.0/24"
}
# Defining CIDR Block for 3rd Subnet
variable "subnet2_cidr" {
  default = "10.100.11.0/24"
}
# Defining CIDR Block for 4th Subnet
variable "subnet3_cidr" {
  default = "10.100.12.0/24"
}
# Defining CIDR Block for 5th Subnet
variable "subnet4_cidr" {
  default = "10.100.20.0/24"
}
# Defining CIDR Block for 6th Subnet
variable "subnet5_cidr" {
  default = "10.100.25.0/24"
}
