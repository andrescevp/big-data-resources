variable "project_id" {
  type = string
}

variable "region" {
  type = string
}

variable "zone" {
  type = string
}

variable "cluster_name" {
  type = string
}

variable "disk_size" {
  type = string
}

variable "network" {
  type = string
}

//https://cloud.google.com/compute/docs/machine-types?hl=es-419
variable "machine_type_master" {
  type = string
}
variable "machine_type_worker" {
  type = string
}