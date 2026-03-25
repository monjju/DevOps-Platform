variable "project" {
  type = string
}

variable "environment" {
  type = string
}

variable "kubernetes_version" {
  type    = string
  default = "1.28"
}

variable "private_subnet_ids" {
  type = list(string)
}

variable "node_instance_type" {
  type    = string
  default = "t3.medium"
}

variable "node_desired" {
  type    = number
  default = 2
}

variable "node_min" {
  type    = number
  default = 1
}

variable "node_max" {
  type    = number
  default = 4
}
