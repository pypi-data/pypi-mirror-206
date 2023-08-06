output "name" {
  value = var.name
}

output "description" {
  value = var.description
}

output "modified" {
  value = timestamp()
}

output "tf_state" {
  value = ""
}