variable "name" {
  type = string
  default = "{{ name }}"
}

variable "description" {
  type = string
  default = "{{ description }}"
}

variable "modified" {
  type = string
  default = null  #xia#
  #xia# default = {% if modified is defined and modified is not none %}"{{ modified }}"{% else %}null{% endif %}

}

