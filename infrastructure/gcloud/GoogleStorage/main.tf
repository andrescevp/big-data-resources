provider "google" {
  credentials = file("credentials.json")
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_storage_bucket" "storage_bucket" {
  name     = var.bucket_name
  location = var.region
  force_destroy = true
}

resource "google_storage_bucket_object" "text" {
  name   = "download_repository.sh"
  source = "initialization_action_scripts/download_repository.sh"
  bucket = "${google_storage_bucket.storage_bucket.name}"
}