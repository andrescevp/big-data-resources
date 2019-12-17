provider "google" {
  credentials = file("credentials.json")
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_dataproc_cluster" "mycluster" {
  name     = var.cluster_name
  region   = var.region
  labels = {
    foo = "bar"
  }

  cluster_config {
    //    staging_bucket = "dataproc-staging-bucket"
    gce_cluster_config {
      # One of the below to hook into a custom network / subnetwork
      network    = var.network
    }

    master_config {
      num_instances = 1
      machine_type  = var.machine_type_master
      disk_config {
//        boot_disk_type    = "pd-ssd"
        boot_disk_size_gb = var.disk_size
      }
    }

    worker_config {
      num_instances    = 3
      machine_type     = var.machine_type_worker
//      min_cpu_platform = "Intel Skylake"
      disk_config {
        boot_disk_size_gb = var.disk_size
//        num_local_ssds    = 1
      }
    }

//    preemptible_worker_config {
//      num_instances = 0
//    }

    # Override or set some custom properties
    software_config {
      image_version = "1.3-deb9"
//      override_properties = {
//        "dataproc:dataproc.allow.zero.workers" = "true"
//      }
    }

//    gce_cluster_config {
//      tags = ["foo", "bar"]
//      service_account_scopes = [
//        "https://www.googleapis.com/auth/monitoring",
//        "useraccounts-ro",
//        "storage-rw",
//        "logging-write",
//      ]
//    }

    # You can define multiple initialization_action blocks
    initialization_action {
      script      = "gs://big-data-resources-store-bucket/download_repository.sh"
      timeout_sec = 500
    }
  }
}