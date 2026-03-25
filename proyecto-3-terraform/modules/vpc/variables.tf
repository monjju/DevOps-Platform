variable "vpc_cidr" {
  description = "CIDR block de la VPC"
  type        = string
}

variable "public_subnets" {
  description = "Lista de CIDRs para subnets públicas"
  type        = list(string)
}

variable "private_subnets" {
  description = "Lista de CIDRs para subnets privadas"
  type        = list(string)
}

variable "azs" {
  description = "Availability zones"
  type        = list(string)
}

variable "project" {
  description = "Nombre del proyecto"
  type        = string
}

variable "environment" {
  description = "Entorno (dev/staging/prod)"
  type        = string
}
