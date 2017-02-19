job "codinggrace-backup" {
  type = "batch"

  datacenters = ["scaleway"]

  periodic {
    cron = "@daily"
    prohibit_overlap = true
  }

  parameterized {
    payload = "forbidden"
  }

  update {
    stagger = "10s"
    max_parallel = 1
  }

  group "codinggrace-backup" {
    count = 1

    restart {
      attempts = 10
      interval = "5m"
      delay = "25s"
      mode = "delay"
    }

    ephemeral_disk {
      size = 100
    }

    task "postgresql-backup" {
      driver = "docker"


        config {
            image = "gitlab.twomeylee.name:7443/twomeylee/postgresql-backup:latest"
            command = "/bin/sh"
            args = ["${NOMAD_TASK_DIR}/run.sh"]
        }

      logs {
        max_files     = 2
        max_file_size = 15
      }

      resources {
        cpu    = 500
        memory = 256
        network {
          mbits = 100
        }
      }

      template {
          destination = "${NOMAD_TASK_DIR}/run.sh"
          data = <<EOF
#!/bin/sh

{{if service "codinggrace-postgresql@scaleway"}}
{{with index (service "codinggrace-postgresql@scaleway") 0}}
export POSTGRES_HOSTNAME="{{.Address}}"
export POSTGRES_PORT="{{.Port}}"
{{end}}
{{end}}

export POSTGRES_DB="{{key "codinggrace/prod/postgresql/db"}}"
export POSTGRES_USER="{{key "codinggrace/prod/postgresql/user"}}"
export POSTGRES_PASSWORD="{{key "codinggrace/prod/postgresql/password"}}"

export AWS_ACCESS_KEY_ID="{{key "postgresql-backups/aws_access_key_id"}}"
export AWS_SECRET_ACCESS_KEY="{{key "postgresql-backups/aws_secret_access_key"}}"
export S3_BUCKET="{{key "postgresql-backups/bucket"}}"
export S3_PREFIX="codinggrace/"
export S3_FILENAME="codinggrace"

exec /usr/local/bin/backup
EOF
			}

    }
  }
}